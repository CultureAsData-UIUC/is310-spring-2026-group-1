"""
scrape_kd.py
IS 310 — Adam Orencia — Spring 2026

Collects real Kevin Durant headlines from Google News (2019–2026),
resolves real article URLs, scrapes article text, then uses Groq AI
to classify each article's Narrative Theme and Tone.

Methodology mirrors the approach used by Maya in the group's NFL dataset.

HOW TO RUN:
  1. Open VS Code → Terminal → New Terminal
  2. Install packages:
       pip3 install GoogleNews googlenewsdecoder trafilatura groq pandas scikit-learn lxml_html_clean
  3. Run:
       python3 scrape_kd.py
  4. Wait ~20–30 minutes. Progress prints to the terminal.
  5. Final output: kd_scraped_dataset.csv in this folder.
"""

import os, time, re
import pandas as pd
from GoogleNews import GoogleNews
from googlenewsdecoder import new_decoderv1
import trafilatura
from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ─── 1. LOAD GROQ API KEY ───────────────────────────────────────────────────
key_path = os.path.expanduser("~/Desktop/IS310/groq_key.txt")
with open(key_path) as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)
print("✅ Groq API key loaded.")

# ─── 2. LOAD MANUAL DATASET AS ANCHOR CORPUS ────────────────────────────────
script_dir   = os.path.dirname(os.path.abspath(__file__))
manual_csv   = os.path.join(script_dir, "kd_finalized_dataset.csv")
manual_df    = pd.read_csv(manual_csv)
manual_headlines = manual_df["Headline"].dropna().tolist()
print(f"✅ Loaded {len(manual_headlines)} manual headlines as anchor corpus.")

# ─── 3. SCRAPE GOOGLE NEWS YEAR BY YEAR ─────────────────────────────────────
# Uses get_news() — same method as Maya's NFL notebook.
# Year-by-year search gives more varied results and avoids rate limits.
# Google limits how far back results go; 2019 onward is reliable.

YEARS = [
    ("01/01/2019", "01/01/2020"),
    ("01/02/2020", "01/01/2021"),
    ("01/02/2021", "01/01/2022"),
    ("01/02/2022", "01/01/2023"),
    ("01/02/2023", "01/01/2024"),
    ("01/02/2024", "01/01/2025"),
    ("01/02/2025", "05/15/2026"),
]

SEARCH_QUERIES = [
    "Kevin Durant",
    "Kevin Durant trade",
    "Kevin Durant legacy",
    "Kevin Durant social media"
]

raw_results = []

for start, end in YEARS:
    year_label = start[-4:]   # e.g. "2019"
    for query in SEARCH_QUERIES:
        try:
            gn = GoogleNews(lang='en', region='US', start=start, end=end, encode='utf-8')
            gn.get_news(query)             # ← Maya's exact method
            results = gn.results()

            count = 0
            for r in results:
                if isinstance(r, dict) and r.get("title"):
                    raw_results.append({
                        "title": r["title"],
                        "link":  r.get("link", ""),
                        "date":  r.get("date", ""),
                        "media": r.get("media", ""),
                        "year":  year_label,
                        "query": query,
                    })
                    count += 1
            print(f"  {year_label} | '{query}' → {count} results")
        except Exception as e:
            print(f"  ⚠️  {year_label} | '{query}' error: {e}")

        time.sleep(1.5)   # polite pause between requests

print(f"\n✅ Raw results collected: {len(raw_results)}")

if len(raw_results) == 0:
    print("\n❌ Google blocked all requests (common on cloud/VPN IPs).")
    print("   Try running this script on your home network without a VPN.")
    exit()

# ─── 4. DEDUPLICATE BY TITLE ────────────────────────────────────────────────
seen = set()
unique_results = []
for r in raw_results:
    if r["title"] not in seen:
        seen.add(r["title"])
        unique_results.append(r)

print(f"✅ After deduplication: {len(unique_results)} unique articles")
MAX_ARTICLES = 500
unique_results = unique_results[:MAX_ARTICLES]

print(f"✅ Capped to {len(unique_results)} articles for processing")

# ─── 5. RESOLVE REAL URLs ────────────────────────────────────────────────────
# Google News wraps links in redirect URLs; new_decoderv1 resolves them.
print("\n🔗 Resolving real article URLs...")

def resolve_url(url):
    try:
        result = new_decoderv1(url)
        if result.get("status"):
            return result["decoded_url"]
        return url
    except Exception:
        return url

for i, r in enumerate(unique_results):
    r["resolved_url"] = resolve_url(r["link"])
    if i % 20 == 0:
        print(f"  Resolved {i}/{len(unique_results)}...")
    time.sleep(0.05)

print(f"✅ URLs resolved.")

# ─── 6. SCRAPE ARTICLE TEXT ─────────────────────────────────────────────────
print("\n📰 Scraping article text...")

def get_article_text(url):
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            text = trafilatura.extract(downloaded)
            return text if text and len(text) > 100 else None
        return None
    except Exception:
        return None

for i, r in enumerate(unique_results):
    r["website_text"] = get_article_text(r["resolved_url"])
    if i % 20 == 0:
        success = sum(1 for x in unique_results[:i+1] if x.get("website_text"))
        print(f"  Scraped {i}/{len(unique_results)}... ({success} successful)")
    time.sleep(0.1)

scraped_results = [r for r in unique_results if r.get("website_text")]
scraped_df = pd.DataFrame(scraped_results)
print(f"✅ Successfully scraped text: {len(scraped_df)} articles")

if len(scraped_df) == 0:
    print("❌ No article text retrieved. Check internet connection.")
    exit()

# Save interim
interim_path = os.path.join(script_dir, "kd_scraped_interim.csv")
scraped_df.to_csv(interim_path, index=False)
print(f"✅ Interim saved: kd_scraped_interim.csv")

# ─── 7. COSINE SIMILARITY FILTER ────────────────────────────────────────────
# Filter out off-topic articles using manual entries as anchor corpus.
# Maya used threshold=0.14 against full article text; we use 0.05 because
# our anchor is headlines (shorter = lower raw similarity scores).
print("\n🔍 Filtering by relevance to KD narrative corpus...")

vectorizer = TfidfVectorizer(max_features=5000, stop_words="english", ngram_range=(1, 2))
vectorizer.fit(manual_headlines)

anchor_matrix = vectorizer.transform(manual_headlines)
news_matrix   = vectorizer.transform(scraped_df["website_text"].fillna(""))

chunk_size = 50
max_sims = []
for start_idx in range(0, news_matrix.shape[0], chunk_size):
    chunk = news_matrix[start_idx:start_idx + chunk_size]
    sims  = cosine_similarity(chunk, anchor_matrix)
    max_sims.extend(sims.max(axis=1).tolist())

scraped_df["similarity_score"] = max_sims

THRESHOLD = 0.05
filtered_df = scraped_df[scraped_df["similarity_score"] >= THRESHOLD].reset_index(drop=True)
print(f"✅ After filter (threshold={THRESHOLD}): {len(filtered_df)} articles kept")

# ─── 8. GROQ AI CLASSIFICATION ──────────────────────────────────────────────
print(f"\n🤖 Groq AI classification on {len(filtered_df)} articles...")
print("   (Progress every 10 articles)\n")

THEMES = ["Rising Superstar", "Superstar", "Villain Narrative",
          "Social Media Drama", "Redemption", "Legacy Debate"]
TONES  = ["Positive", "Neutral", "Negative"]

def classify_article(title, text):
    excerpt    = str(text)[:1500] if text else ""
    themes_str = "\n".join(f"- {t}" for t in THEMES)
    tones_str  = "\n".join(f"- {t}" for t in TONES)

    prompt = f"""You are analyzing sports media coverage of NBA player Kevin Durant.

Article headline: {title}

Article excerpt: {excerpt}

Task 1 — Classify the NARRATIVE THEME into exactly one of these categories:
{themes_str}

Definitions:
- Rising Superstar: Early career, draft, rookie years, emerging talent
- Superstar: Dominant performance, MVP, scoring titles, elite play
- Villain Narrative: Criticism of Warriors decision, snake label, ring-chaser, controversy
- Social Media Drama: Twitter/Instagram activity, burner account, online feuds
- Redemption: Comeback from injury, proving critics wrong, reclaiming reputation
- Legacy Debate: All-time ranking, championship validity, career retrospectives

Task 2 — Classify the TONE:
{tones_str}

Respond in EXACTLY this format, nothing else:
THEME: [theme here]
TONE: [tone here]"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=50,
        )
        raw = response.choices[0].message.content.strip()
        theme_match = re.search(r"THEME:\s*(.+)", raw)
        tone_match  = re.search(r"TONE:\s*(.+)",  raw)
        theme = theme_match.group(1).strip() if theme_match else "Legacy Debate"
        tone  = tone_match.group(1).strip()  if tone_match  else "Neutral"
        if theme not in THEMES: theme = "Legacy Debate"
        if tone  not in TONES:  tone  = "Neutral"
        return theme, tone
    except Exception as e:
        print(f"    ⚠️  Groq error: {e}")
        return "Legacy Debate", "Neutral"

ai_themes, ai_tones = [], []

for i, row in filtered_df.iterrows():
    theme, tone = classify_article(row["title"], row.get("website_text", ""))
    ai_themes.append(theme)
    ai_tones.append(tone)
    if (i + 1) % 10 == 0:
        print(f"  Classified {i+1}/{len(filtered_df)}...")
    time.sleep(0.1)

filtered_df["AI_Narrative_Theme"] = ai_themes
filtered_df["AI_Tone"]            = ai_tones
print(f"\n✅ Groq classification complete.")

# ─── 9. CAREER PHASE ────────────────────────────────────────────────────────
def get_career_phase(year_str):
    try:
        y = int(str(year_str)[:4])
        if   y <= 2007: return "Pre-NBA"
        elif y <= 2015: return "Thunder"
        elif y <= 2019: return "Warriors"
        elif y <= 2022: return "Nets"
        elif y <= 2024: return "Suns"
        else:           return "Rockets"
    except:
        return "Unknown"

filtered_df["Career_Phase"] = filtered_df["year"].apply(get_career_phase)

# ─── 10. BUILD FINAL OUTPUT ─────────────────────────────────────────────────
output_df = pd.DataFrame({
    "Date":                   filtered_df["date"],
    "Outlet":                 filtered_df["media"],
    "Headline":               filtered_df["title"],
    "URL":                    filtered_df["resolved_url"],
    "Source_Type":            "Traditional Media",
    "Career_Phase":           filtered_df["Career_Phase"],
    "Manual_Narrative_Theme": "",
    "Manual_Tone":            "",
    "Auto_Narrative_Theme":   filtered_df["AI_Narrative_Theme"],
    "Auto_Tone":              filtered_df["AI_Tone"],
    "Theme_Agreement":        "N/A",
    "Tone_Agreement":         "N/A",
    "Similarity_Score":       filtered_df["similarity_score"].round(4),
    "Notes":                  "Scraped via GoogleNews; classified by Groq llama3-8b",
    "Collection_Method":      "GoogleNews-Scraped + AI-Labeled",
})

# ─── 11. COMBINE WITH MANUAL ENTRIES ────────────────────────────────────────
manual_df["Similarity_Score"]    = 1.0
manual_df["Collection_Method"]   = "Manual"

for col in output_df.columns:
    if col not in manual_df.columns:
        manual_df[col] = ""

manual_subset = manual_df[output_df.columns]
combined_df   = pd.concat([manual_subset, output_df], ignore_index=True)

out_path = os.path.join(script_dir, "kd_scraped_dataset.csv")
combined_df.to_csv(out_path, index=False)

print(f"\n{'='*55}")
print(f"✅ DONE. Saved: kd_scraped_dataset.csv")
print(f"{'='*55}")
print(f"  Manual entries:  {len(manual_subset)}")
print(f"  Scraped + AI:    {len(output_df)}")
print(f"  TOTAL:           {len(combined_df)}")
print(f"\nTheme distribution:")
print(combined_df["Auto_Narrative_Theme"].value_counts().to_string())
print(f"\nTone distribution:")
print(combined_df["Auto_Tone"].value_counts().to_string())
print(f"\nCareer phase distribution:")
print(combined_df["Career_Phase"].value_counts().to_string())

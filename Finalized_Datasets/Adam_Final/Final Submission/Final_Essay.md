# Media Narratives as Data: Tracking Kevin Durant Coverage Across a Decade of Sports Media
## Adam Orencia | IS 310 

As a former athlete and sports fan, I have always been interested in what it is like to be a professional athlete. Beyond the money and fame, there is a less visible side shaped by constant media attention. With the rise of social media and 24/7 sports journalism, professional athletes exist under continuous public scrutiny.

This project treats sports narratives as data, focusing on future NBA Hall of Famer Kevin Durant. Durant is one of the most documented and debated athletes in the modern social media era. He is known not only for his elite basketball career, but also for controversies, Twitter feuds, and shifting public narratives that have followed him for years. Starting in 2016, when he left the Oklahoma City Thunder, he was widely condemned and labeled a “snake,” sparking a long-running conversation about loyalty, competition, and legacy in professional sports. Tracking how media outlets covered these moments over time offers a way to examine how public perception shifts across an athlete’s career.

My final dataset contains 482 rows, combining manually selected articles with computationally scraped and labeled news coverage. However, getting there was more difficult than I initially expected, and the challenges along the way became one of the most interesting parts of the project.

## Building the Dataset: Manual Curation + Computation

I began with 49 manually curated entries drawn from outlets such as ESPN, Bleacher Report, and other major sports publications. Each entry was hand-coded with a narrative theme (e.g., Villain Narrative, Social Media Drama, Redemption) and a tone classification of Positive, Neutral, or Negative. This initial dataset helped establish the structure of my analysis, but it was not large enough to identify patterns across a decade of coverage. To reach at least 500 entries, I needed to build an automated data collection pipeline.

My first approach used the Groq API, a free large language model service, to classify articles scraped from Google News. The idea was to pass each article’s headline and excerpt into the model and receive a predicted theme and tone, simulating human judgment at scale. I implemented a full scraping pipeline (scrape_kd.py) using the GoogleNews Python package, the googlenewsdecoder library to resolve redirect URLs, and trafilatura to extract article text.

However, I did not anticipate how much content trafilatura would extract from each page. Instead of short excerpts, it often pulled full article bodies, sidebars, and related content sections. As a result, the scraping process took over an hour and a half, and the Groq API quickly ran into rate limits. I ultimately abandoned the LLM-based classification approach but retained the scraped dataset, which still contained valuable article text without labels.

The final approach used two simpler methods:
VADER sentiment analysis for tone classification
A keyword-based classifier for narrative themes

VADER is a rule-based sentiment tool designed for social media and journalistic text. It assigns a compound sentiment score to each text, which I mapped as follows: scores above 0.05 were labeled Positive, below -0.05 Negative, and everything in between Neutral. The keyword classifier scanned article headlines and the first 500 characters of text for theme-related terms. For example, words like “snake,” “ring-chaser,” and “betrayal” mapped to Villain Narrative, while “burner,” “Twitter,” and “feud” mapped to Social Media Drama. Although less sophisticated than an LLM, this approach was fast, interpretable, and reproducible.

The scraping process used the GoogleNews package with year-by-year queries from 2019 to 2026, allowing collection without hitting major API limits. The googlenewsdecoder library resolved Google News redirect links into real article URLs, replacing earlier researcher-approximated links that were not functional. The final scrape produced 433 articles with verified URLs from outlets including ESPN, Yahoo Sports, CBS Sports, and The New York Times. These were combined with the 49 manual entries to produce the final 482-row dataset.

## Scale 

At 49 entries, meaningful patterns were difficult to identify. Expanding the dataset to 482 made broader trends visible. Legacy Debate emerged as the dominant theme, which aligns with Durant’s public narrative since 2016, largely centered on questions of legacy, legitimacy, and historical ranking. Neutral tone also dominated, reflecting how sports journalism often operates in an informational register even when underlying narratives are critical.

The agreement rate between manual labels and the automated classifier was 55.1% for theme and 59.2% for tone, measured on the original 49 entries. These rates highlight an important limitation: keyword-based classification captures explicit signals but often misses context. For example, an article describing Durant’s return from injury may be labeled as Redemption by the system, while a human reader might interpret it as closer to Legacy Debate or even skepticism. This gap between human and automated classification is itself a finding, showing that cultural categories in sports journalism are highly context-dependent.

## Limitations 
The dataset has two main limitations. First, it is heavily weighted toward 2019 onward. Google News becomes less reliable for older coverage, meaning Durant’s early career (2007–2016)—where the “Rising Superstar” narrative was most prominent—is largely missing. As a result, the dataset overrepresents his Warriors, Nets, and Suns eras.

Second, the dataset only includes traditional news media indexed by Google News. It excludes Reddit, fan communities, podcasts, and social media, which are often where narratives like the “snake” label originated and spread. This means the dataset reflects institutional journalism rather than the full ecosystem of public discourse.

There is also query bias. Searches such as “Kevin Durant social media” primarily return journalistic coverage of his posts, not his actual posts. As a result, the dataset captures how media interprets his digital presence, not the presence itself.

## Considerations

Assigning narrative labels such as “Villain Narrative” or “Redemption” introduces interpretive bias. These categories reflect my own analytical framework and research focus. A different researcher with different theoretical assumptions could reasonably produce a different labeling system.

## Lessons Learned

The most important lesson from this project is that computational methods are not shortcuts. They introduce their own forms of labor and failure. Building the scraping pipeline, handling unexpected text volume from trafilatura, and switching from an LLM-based approach to rule-based classification all required iterative debugging and redesign.

Another key takeaway is the importance of real, verifiable URLs. Earlier versions of the dataset used approximated links, which often did not work. Building a functioning scraping pipeline that resolved actual article URLs was essential for making the dataset reproducible and credible.

Ultimately, this project reinforced that computational analysis does not eliminate interpretive decisions—it redistributes them across different stages of the pipeline.
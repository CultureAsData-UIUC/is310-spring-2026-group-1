# Initial Dataset Documentation

### Cultural Materials and Project Scope

For my project, I'm working with professional men's tennis culture. This is done by analyzing how audiences talk about and react to the rather better ATP players online after matches. Tennis is interesting as cultural data because it's seen as more of a gentlemans sport. The reactions are not only to the skill, but the emotions of the players, and their growth. There is a reaction heavily tied to performance, personality, nationality, and how the media shapes the player, but also the emotional side of the fans to a player, no matter the characteristics. I wanted to explore whether the tone of online posts made by fans about the matches reflect how players are perceieved after these big performances. The goal would be to see whether the reactions are linked to match outcomes and statistics, or rather just a projection of the player and their popularity. 

My initial dataset combines two forms of data. The first is an existing ATP match dataset I got from [Kaggle](https://www.kaggle.com/code/jockeroika/atp-tennis-dataset-2000-2025/input) that covers men's ATP matches from 2000 to 2025. Rather than auditing an already competed dataset about social media from Kaggle, I used the tennis dataset as the core, and then added onto it manually. I collected YouTube comments from highlight videos of specific matches that matched the ones found in the tennis dataset. I collected the comments, and wrote my own sentiment classification for each comment. 

I satarted by filtering the tennis data to five of the top ATP tennis players:

- Jannik Sinner
- Carlos Alcaraz
- Alexander Zverev
- Novak Djokovic
- Ben Shelton

I selected these players from personal experience, social media coverage, and their ranks. They represent different generations, countries, and fanbases which will allow for a wide variety of fans that will be commenting on their performance. 

---

### How I Collected the Data

I began by filtering the Kaggle ATP dataset for matches that involved those five specific players. I filtered for:

- recent matches
- high average rankings between the players
- unique matches that weren't between the same couple of players

After finding the three matches for a player, I manually searched youtube for highlight videos with the same search scheme:

**{Player} vs {Opponent} {Tournament Name} {Year} highlights**

Thankfully, the first video that came up every time was usually from trusted tennis media outlets, or even the tournament channel themselves. I then manually recorded the following infomation from the video:

- Video Title
- Top five visible comments

Then for each comment, I assigned one of the three following sentiments:

- Positive
- Neutral 
- Negative

These labels were interpreted by me rather than generated computationally. Positive comments were often prasiing a player or performance, improvement, etc. Neutral comments often said a good thing about one player and bad about another or focused on a detail not correlating to the match/players. A negative comment usually was a critique of a player, the tournament outcome, or the channel. 

All of the information was entered into a Google Sheet, with each row being a unique comment. The sheet was then exported to a csv file.

---

### Computational Tools and the Limitations

The main computational tool I used was python, alongside the already existing KAggle dataset. Python made it possible to filter the ATP dataset by the number of constraints I was looking for. I could sort by date, create an average rank variable to help find matches with high ranking opponents, and find matches where the player I was loking for was marked as the opponent. I manually checked to make sure I didn't record two of the same match. 

One limitation is the structure of YouTube comment sections. Sometimes, the first comment may be a pinned comment made by the channel itself. These comments are often promoting something, or not relating to the match at all, so it wwouldn't serve a purpose to record. Also, the order fo the comments could technically change over time. The most recent matches in the dataset happened 9-10 months ago from the time of this project, so there are likely not a lot of new comments being left on the YouTube videos. Still, it's technically possible that another comment could be left and could get enough likes/responses that it moves up above the comments I manually recorded. This wouldn't really affect analysis that much, and the chances are so small, but because my logic of collecting comments was by order of appearance, it's a small risk if this were to be recreated at a different time. 

Another limitation is manually labeling the sentiment. It's rather subjective when I'm labeling manually, because my view of a positive/negative comment might be different from someone else's. There's also the matter of does a positive comment towards the opponent technically count as a negative comment towards the main player I was filtering on. I chose to make that false, and just go with any positive comment about the match be positive. The later logic mentioned would make the analysis too unnecessarily complicated. There are still only three choices to be labeled, though, so the results would hopefully be general. 

When getting matches from Ben Shelton, I noticed there were only 10 matches that came through the filter. This was concerning, as it made the data for him more scarce. Looking ahead, I will likely be using a different player. He was the only American player I had, so it seemed like a good choice at first. 

I also considered trying to scrape data using an API, when creating the dataset, but felt like the initial dataset should be manually curated so I could understand the data more deeply, and also learn what other variables I may want to compute/include in the final dataset.

---

### Organization Choices and Interpretive Choices

I made a lot of decisions about what to include and what not to include. 

Only used mens tennis matches

- This just helped centralize the topic, instead of making it too broad

Focused on recent matches

- Just in case there was more recent news about a player, or major shifts in rankings. I didn't want to be exploring a comment from 2015 compared to 2025. 
- YouTube wasn't created at the initial dates on this dataset. If I chose a match from 2000, it would be more unlikely to have a historical highliight reel of a match than one played in the early 2020s.

Prioritized matches with higher ranking players

- There is more social media content around these players
- Better chance of quality videos from trusted channels 

Used highlight videos from YouTube instead of full match recordings

- This was due to popularity/availability of highlight videos comapred to full matches

Only used three classifications of sentiment

- The more classifications there were, the more subjective it got
- Also based this off of the sentiment NLP I planned on using for the full dataset

I chose to just take the top five comments from each vid. I knew I was aiming for between 50-100 datapoints, rows. I couldve have taken a ton of comments frmo a couple of vids, or 1-2 comments from a ton of videos. I chose to settle towards the middle. Total of five players, and chose three matches per player. Each match got five comments from the video. That was a total of fifteen comments per player, which came out to 75 rows. 

---

### Patterns and Questions

I noticed a couple of patterns while I was collecting data. 

Comments are often heavily related to the overall player popularity and identity. Some players got positive comments no matter what, win or lose. Other players got more attention and positive comments if they upset a match as an underdog. The comments had a relatively strong correlatin to match outcome, but there were more rare occurences of negative comments for sure. This is why making the sentiment more numerical may help differentiate comments, becaise instead of relying on a classification, I can actually see the difference between two positive comments. 

The most high ranked matches had the most comments by far, which makes sense. Those matches will receive more attention, but it confirmed the theory that people will tend to think well of those that are ranked higher. If those athletes do really bad, though, the fans turn on them quickly, which is where the negative comments come out. 

These both raised the question whether fan sentiment really relied on the outcome of a match or the broader fan narratives/reputations the player had. This connects to the idea of culture as data, because the comments are not simply opinions. They reflect the collective audience behavior and emotions surrounding mens tennnis.

---

### Scaling the Dataset with Computation: Next Steps

for the next steps of the project, I plan to take the process I used to manually create the data and use it algorithmically. I'm going to start with the ATP tennis dataset, and apply filters five times, for each player. I will create a match selection process, likely by choosing the first match in the filter, ad then continuing to filter the dataset based on the matches selected for that player so far. I will also be checking to make sure each match hasn't already been selected from another player's batch, because I don't want to have duplicate data. 

I'll be using the YouTube API to find the video, and then get comments from that video. Then i'll run all of the comments thorugh a Natural Language Processor, VADER, to assign a numerical sentiment value. That numerical sentin=ment value can also be used to make a sentiment classification like "Positive" or "Nagetive", but that probably won't be needed. 

The full process looks like this:

1. Programatically filter ATP tennis matches based on rankings, recency, player, etc
2. Automatically generate a YouTube search schema based on the ATP tennis data selected
3. Retrieve the link and video details for the match with YouTube API
4. Scrape the comments from the video using YouTube API
5. Apply sentiment analysis to comments
6. Merge the data from YouTube searches and analysis back to the chosen tenis matches

When scaling the project, a lot of the interpretive decisions I made will likely need to be automated. I anticipate there being some challenges when it comes to this, but also the overall scope of scaling a dataset. First, I have to make sure I don't exceed the Google API rate limits when I get the YouTube data. Searching for YouTube videos with the API uses 100 credits, which means I will liely be scaling the amount of comments taken from each video instead of scaling up the amount of matches. Scraping a comment only uses one credit. I also have to think of how comments are formatted. I had the ability to make sure they were in english, make sure they were structured correctly, and I knew what emojis meant. I will have to fugure out a way to clean the comments and make sure they are ready for analysis. There will also likel be comments that are not related to the matches, or even tennis. From what I saw, majority of comments are relevant. So hopefully, if there are some bad comments, they won't overtake the ammount of usable comments. I will also have to trust that the YouTueb API is returning the best fitting video to the search, just as I was getting trusted videos in my search. 
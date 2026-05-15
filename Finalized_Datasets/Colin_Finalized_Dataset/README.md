# Data Documentation

### Dataset Overview

This dataset explores the relationship between professional Men's tennis matches and online fan reactions through YouTube video comments. The project combines already structures tennis match data from [Kaggle](https://www.kaggle.com/code/jockeroika/atp-tennis-dataset-2000-2025/input) with YouTube video metadata and comment sentiment. 

The data isn't all about tennis performance and being analyzed. It more closely represents the role and narrative that tennis fans create, and the cultural event that continues for the sport beyond everythig that happens on the court. 

To begin, here is the breakdown of all of hte variables found in the final computed dataset:

| **Column Name** | **Purpose** | **Source** |
| ----------- | ------- | ------ |
| *Tournament* | Tournament at which match was played | Tennis Kaggle Data |
| *Date* | Date match was played | Tennis Kaggle Data |
| *Series* | Tournament category or level | Tennis Kaggle Data |
| *Court* | Whether the match was played indoors or outdoors | Tennis Kaggle Data |
| *Surface* | Playing surface used for the match | Tennis Kaggle Data |
| *Round* | Tournament round in which the match occurred | Tennis Kaggle Data |
| *Best of* | Maximum number of sets in the match format | Tennis Kaggle Data |
| *Player_1* | First listed player in the match | Tennis Kaggle Data |
| *Player_2* | Second listed player in the match | Tennis Kaggle Data |
| *Winner* | Player who won the match | Tennis Kaggle Data |
| *Rank_1* | ATP ranking of Player_1 at the time of the match | Tennis Kaggle Data |
| *Rank_2* | ATP ranking of Player_2 at the time of the match | Tennis Kaggle Data |
| *Pts_1* | ATP ranking points for Player_1 | Tennis Kaggle Data |
| *Pts_2* | ATP ranking points for Player_2 | Tennis Kaggle Data |
| *Odd_1* | Betting odds for Player_1 | Tennis Kaggle Data |
| *Odd_2* | Betting odds for Player_2 | Tennis Kaggle Data |
| *Score* | Final match score by set | Tennis Kaggle Data |
| *Rank_Mean* | Average ranking of the two players in the match | Derived Data |
| *Upset* | Indicates whether the lower-ranked player won | Derived Data |
| *Selected_Player* | Main player used for the YouTube search and comment analysis | Derived Data |
| *Opponent* | Opposing player matched against the selected player | Derived Data |
| *match_index* | Numeric identifier for each match in the dataset | Derived Data |
| *youtube_search_query* | Search phrase used to find the related YouTube video | Derived Data |
| *youtube_video_id* | Unique YouTube identifier for the selected video | YouTube API Scraping |
| *youtube_video_title* | Title of the selected YouTube video | YouTube API Scraping |
| *youtube_channel_title* | Name of the YouTube channel that posted the video | YouTube API Scraping |
| *youtube_published_at* | Date and time when the YouTube video was published | YouTube API Scraping |
| *youtube_url* | Web link to the selected YouTube video | YouTube API Scraping |
| *comment_number* | Sequential number assigned to each scraped comment | Derived Data |
| *comment_text* | Text content of a YouTube comment | YouTube API Scraping |
| *comment_likes* | Number of likes received by the comment | YouTube API Scraping |
| *comment_published_at* | Date and time when the comment was published | YouTube API Scraping |
| *sentiment_score* | Full sentiment score output for the comment text | Derived Data |
| *negative_score* | Negative sentiment proportion for the comment | Derived Data |
| *neutral_score* | Neutral sentiment proportion for the comment | Derived Data |
| *positive_score* | Positive sentiment proportion for the comment | Derived Data |
| *compound_score* | Overall compound sentiment score for the comment | Derived Data |
| *sentiment_label* | Final sentiment category assigned to the comment | Derived Data |

Overall, this project uses tennis data, YouTube data, and sentiment analysis to explore how professional tennis matches are talked about and discussed by online audiences.

---

### Tools and Libraries Used

The main tools and libraries included:

- Python
- Pandas
- Requests
- YouTube Data API
- VADER Sentiment Analyzer
- time Library
- os Library

Python was used to clean the tennis match data, generate search queries, request data from the YouTube API, collect comments, and run sentiment analysis.

Pandas was used to organize and merge datasets. The YouTube Data API was used to collect video and comment data. VADER was used to convert comment text into numerical sentiment scores.

Majority of the workflow was computational. I did some manual checks on things like the videos that were selected, or why there were missing comments. Occasionally, there weren't as many strong videos on a match and therefore not many comments on the videos. The data still turned out high quality, there were just some instances where there wasn't as much data to collect.

---

### Research Focus

The main focus of this project is understanding how tennis fans react to professional matches through YouTube comments. Instead of only asking who won or lost, this project asks how audiences respond emotionally to different players and match outcomes.

Questions that could go on to be answered include:

- Do closer matches create more emotional reactions?
- Do certain players generate stronger sentiment?
- How do fans emotionally react to wins and losses?
- Are comments more positive for underdog victories?
- How do fan communities construct narratives around players?

This felt connected to the idea of **culture as data**, as the YouTube comments did not just represent plain text. They represent fan behavior, sports culture, and emotional investment into the sport. It's an entire base of people ultimately connecting and discussing on the same topic. 

---

### How the Data was Collected

The data collection process began with a professional tennis match dataset. This match data served as the foundation of the project because each row represented a real tennis match.

From there, I used match information to search for related YouTube highlight videos. For each match, I created a search query using the player names, tournament name, year, and the word “highlights”.

The search query was built like this:

**{Player} vs {Opponent} {Tournament} {Year} highlights**

An example search query would be:

**Alcaraz vs Sinner Wimbledon 2025 highlights**

Once a relevant YouTube video was found, I collected video information and comments from that video. The comments were then analyzed using VADER sentiment analysis to measure the emotional tone of each comment.

The final dataset combines:

- structured tennis match data
- YouTube video metadata
- YouTube comment data
- sentiment analysis scores

Each of these sources will now be discussed.

#### Match Dataset Source

The base match dataset came from publicly available professional mens tennis match data, the professional league known as ATP. This data provided the structured match-level information needed to connect tennis matches to online fan reactions.

The match dataset included important fields such as player names, tournament names, dates, and match results. These fields were necessary for generating YouTube search queries and matching each tennis match to a related highlight video.

This match data acted as the backbone of the project. The YouTube and sentiment data were added later as cultural and digital layers on top of the original sports data.

#### YouTube Data Collection Workflow

YouTube data was collected using the YouTube Data API. The workflow involved creating a search query for each match, retrieving a relevant highlight video, and then collecting comments from that video.

The general workflow was:

1. Start with a tennis match from the match dataset
2. Extract the last names of both players
3. Extract the tournament name
4. Extract the match year from the match date
5. Build a YouTube search query
6. Use the YouTube Data API to search for a highlight video
7. Store the video ID, title, and other metadata
8. Use the video ID to collect comments
9. Merge the comments with the match and video data
10. Run sentiment analysis on each comment

One challenge was that player names in the original dataset were sometimes stored in abbreviated formats, such as:

- Alcaraz C.
- Sinner J.
- Fritz T.
- De Minaur A.

Because of this, I had to clean the player names so the search query used only the last names. This made the YouTube searches more natural and more likely to return relevant highlight videos.

The process for how to use the YouTube API calls were found from these useful lessons:

- Python Quickstart: https://developers.google.com/youtube/v3/quickstart/python
- Scraping Video Data: https://developers.google.com/youtube/v3/docs/videos/list
- Scraping Comment Data: https://developers.google.com/youtube/v3/docs/commentThreads/list


#### Comment Collection and Sentiment Analysis

After collecting YouTube video IDs, I used the YouTube Data API to collect comments from each highlight video. These comments represent how fans reacted to the match after watching or discussing the highlights.

Each comment was processed using Valence Aware Dictionary and sEntiment Reasoner, or VADER. VADER is a sentiment analysis model designed for social media text. This made it useful for analyzing YouTube comments because comments often include casual language, slang, punctuation, capitalization, jokes, and even emojis.

VADER assigns four scores to each comment:

- positive
- neutral
- negative
- compound sentiment

The compound score ranges from -1 to 1:

- values near -1 indicate strongly negative sentiment
- values near 0 indicate neutral sentiment
- values near 1 indicate strongly positive sentiment

For this project, the compound score is especially important because it provides one overall sentiment value for each comment.

However, these scores need to be interpreted carefully. A positive comment does not necessarily mean the commenter supports the winner. A negative comment may reflect disappointment, frustration, controversy, or criticism. Some comments may praise one player while criticizing another in the same sentence. I found many of the sports fan language is emotionally complicated, so sentiment scores should be understood as approximations of audience emotion rather than perfect measurements of fan opinion.

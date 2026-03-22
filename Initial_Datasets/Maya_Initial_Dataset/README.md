### Initial Dataset Information

#### Initial Dataset

Dataset Name: nfl_media

Number of Records: 75

Unit of Analysis: Individual media-covered events involving NFL players' public statements, social media posts, interviews, podcast, or public appearances. 

Columns/Variables: ID, Player Name, Player Status, Year of Event, Statement Made, Event Description, Platform, Event Type, Media Tone, Post Status, Media Coverage, Sources

| Column Name | Description | Possible Values / Notes |
|------------|------------|------------------------|
| **ID** | Unique identifier for each event | 1, 2, 3, … |
| **Player Name** | Name of the NFL player involved in the event | e.g., Travis Kelce, Aaron Rodgers |
| **Player Status** | Player's professional status at the *time of the event* (media-reported) | Playing, Retired, Free Agent |
| **Year of Event**| Year the event occurred | 2020–2026 |
| **Statement Made** | Direct quote, post, or statement made by the player | Text of social media post, interview quote, podcast snippet |
| **Event Description** | Context or explanation of what happened | e.g., “Apologized for controversial tweet,” “Postgame reaction to teammate” |
| **Platform** | Where the statement appeared | Twitter/X, Instagram, Podcast, Press Conference, Public Appearance |
| **Event Type** | Type of statement or reaction | Controversy, Apology, Support, Reflection, Humor |
| **Media Tone** | Overall tone of news coverage framing the event | Positive, Negative, Mixed |
| **Post Status** | Status of the original statement | Active, Deleted, Available, Unavailable |
| **Media Coverage** | Extent of coverage in digital news media | Low, Medium, High (based on number of articles/outlets & prominence of sources) |
| **Sources** | Examples of news outlets or publications covering the event | Fox News, ESPN, Yahoo Sports, People, etc. |

#### Initial Documentation

##### Cultural Materials

The dataset is composed of NFL players' social media posts, statements from interview, podcasts, and public appearances that were covered by digital news outlets (e.g. Yahoo Sports, ESPN, US Weekly) from 2020-2026. I constructed the dataset from scratch of events that attracted media attention. These kinds of events may reveal how digital news media interpret, amplify, or contextualize players' behavior and action. This not only allow me to analyze the content of the posts but also how the media frames the event. 

##### Computational Tools & Limitations

I manually inputted the data in an Excel sheet, which is a limitation itself because it was time-consuming. Also by adding the entries myself, the framing does risk at involving subjective interpretation, especially with variables like Event Type and Media Tone. 

##### Decisions on Inclusion/Exclusion

First, when deciding what kind of variables/pieces of information I want my dataset to include, I thought about different kinds of analysis can be taken and discovered about NFL players in regards to how their activities were covered by the digital news outlets. Questions arose about whether retired players would appear more than current players, the proportion of platforms in which the statements were said, whether the post was removed after it has garned negative attention, etc. These kinds of questions aid in me deciding what kind of variables I want to include. But when it comes to making decisions of the values of these variables, I think majorly about whether the event received media attention. If the event is very niche to the point there was no media covering it, then I didn't include it in my dataset. I didn't want to include a social media post or an interview that can merely be found online; there has to be some kind of media coverage aside them to better understand the digital news realm of sports.

##### Categorization Choices

Looking at my dataset, there are visible categorization of the variables. For the event type, I was curious to see if the nature of the statement can be relevant in the story in which the outlet tells about the event. For media tone, after looking at different number of outlets that I could find about the event, I noted whether the overall framework of the statement used was positive, negative, or mixed. Upon that with the post status, I can uncover if there is a connection between the tone of the various media to whether a post is still available to view on whatever platform it was released. Another variable I would like to mention would be media coverage, which I categorized from low to high to add naunce of whether the amount an event is covered can influence public perception further on the corresponding NFL player depicted. 

##### Challenges 

The challenges I have encountered with collecting the data has included subjectivity and platform ambiguity. With subjectivity, it can arise both from media coverage and from the process of translating that coverage into structured data. Different media outlets may portray the same player or event in varying ways, and some players may receive more favorable or critical coverage depending on the outlet. 

To address this, I included a Sources variable to track which outlets covered each event. This allows for greater transparency and mkaes it possible to identify patterns in coverage, such as differences between team-afflicted media and larger national outlets. For example, an official team outlet may frame a player more positively than a national outlet such as Yahoo Sports. 

Additionally, variables like Event Type and Media Tone can help create a more structured and consistent framework for interpretation. While these categories could be interpretive themselves, they help standardize how events are classified across the dataset. For instance, events that are categorized as "Controversy" may be more likely to be framed negatively in media coverage, which provides a basis for comparison across cases. 

For platform ambiguity, when looking to see if a social media post is still active, some required manual searching or replying on the embedded links in the news coverage. If the links did not bring me to, for example, a tweet, I worked around the problem by labeling the post status as "Unavailable" rather than assuming it was "Deleted." 

When it comes to statements made from non-social media platforms, the concept of a "post" is not directly applicable when saying if an interview is still active or deleted by the NFL player themselves. So to work around this challenge and remain consistent for these 'platform,' I have included labels like "Available" and "Unavailable" if those interviews and such could be found at their original source. 

##### Patterns, Questions, or Tensions Emerged

Working closely with this dataset revealed several patterns, questions, and tensions related to how digital news media frame NFL players' public statements. 

One clear pattern is that emerged is that player prominence influences the level of media coverage. More "popular" NFL players, such as Travis Kelce, tend to receive greater media attention for their public statements. This could be evident in cases where their visibility extends beyond sports, such as Kelce's relationship with Taylor Swift, which relates in coverage from non-sports media outlets. 

Timing is recognized as a possible significant factor in determining the level fo media coverage. Statements that align with ongoing or highly visible events at the time like the Super Bowl or broader social issues, they tend to receive more attention than statements made outside of these contexts. For example, comments about game performance made in close proximity to playoff games or other high-stakes moments tend to receive greater media attention, as they intersect with heightened public interest and ongoing discourse. To further explain, if a player comments on another player's performance during these moments, coverage is more likely to appear in prominent outlets such as ESPN, where audience engagement is already elevated. This suggests that media attention could be amplified when player statements align with emotionally charged and widely followed events. 

Also along that line, any statements that has been framed as a "Controversy" tend to receive more media attention than "non-controversial" comments. This may reveal that media visibility may not be evenly distributed across types of content, but instead driven by what is considered newsworthy or engaging. 

This dataset raises broader questions about whose voices and statements become more visible through media coverage. Like whether the player's prominence and team afflication put them in a brighter and critical spotlight than others. 


#### Next Steps

##### Generating more data computationally 
To generate more data computationally, I will use Option 1: scale up to 500+1,000+ items using automation. I plan to use web scraping of digital news outlets to collect articles covering NFL player statements, along with pattern matching to extract key features such as Media Tone, Event Type, Platform, and Post Status. The limitations may include the risk of missing nuances, sacasm, or mixed framing, as well as web scraping not fully capturing all relevant sources. 

##### Interpretive decisions to automate
I plan to automate decisions such as identifying the platform (Twitter/X, Instagram, podcast, interview), extracting quotes or statements from the media text, and approximating media tone using the keyword-based sentiment analysis. I will also use pattern matching to classify events into categories like "Controversy," "Support," "Reflection," "Apology," or "Humor" based on linguistic cues. For ambiguous framing or possible edge cases, there may be a struggle with using automation to accurately computate these values. There could be other challenges like data quality (duplicate events, incomplete coverage, or misclassification), media accessibility, and ambiguity in tone and framing.
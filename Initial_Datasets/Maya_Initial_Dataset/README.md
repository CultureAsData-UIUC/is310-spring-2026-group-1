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
The dataset is composed of NFL players' social media posts, statements from interview, podcasts, and public appearances that were covered by digital news outlets (e.g. Yahoo Sports, ESPN, US Weekly) from 2020-2026. I constructed the dataset from scratch of events that attracted media attention. These kinds of events may reveal how digital news media interpret, amplify, or contextualize players' behavior and action. This not only allow me to analyze the content of the posts but also how the media frames the event. 

I manually inputted the data in an Excel sheet, which is a limitation itself because it was time-consuming. Also by adding the entries myself, the framing does risk at involving subjective interpretation, especially with variables like Media Tone. 


- What computational tools did you use to assist your work? How did they help? What were their limitations?
- What decisions did you make about what to include, exclude, or how to categorize? Why? What challenges did you encounter? How did you address them? What patterns, questions, or tensions emerged from working closely with this data?


#### Next Steps. 
After creating this bespoke dataset, after Spring Break, you will work on scaling or expanding your dataset with computation. This plan should outline how you will address the following questions:
- How will you generate more data computationally (Option 1: scale up to 500-1,000+ items using automation)? Or will you combine your bespoke data with an existing large dataset (Option 2: audit, merge, and analyze)? What computational methods will you use? (APIs, web scraping, LLMs, pattern matching, etc.)
- What will change when you scale? What interpretive decisions will you try to automate? What technical challenges do you anticipate?
- This plan is your roadmap for understanding how scale transforms data work. You don’t need to implement it yet—but you should be thinking critically about what happens when you move from 75 carefully crafted items to 1,000 algorithmically generated ones. Your initial dataset should be submitted in your group’s GitHub repository and you should update any collective documentation to help users navigate the files and folders.
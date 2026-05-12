# Documentation #

### Dataset Overview ###

This dataset examines the relationship between professional volleyball players, digital visibility, and sports culture through social media metrics and institutional indicators. The project focuses on how athletes are represented and circulated through online platforms, particularly Instagram, and how that visibility may relate not only to athletic success, but also to broader cultural systems such as nationality, league prominence, branding, and international recognition.

The finalized dataset contains 80 professional volleyball players from multiple countries and professional leagues around the world. Rather than focusing only on athletic performance statistics, the dataset was expanded to include variables connected to cultural visibility and institutional recognition. The dataset includes:

<li>gender</li>
<li>nationality</li>
<li>league country</li>
<li>team name</li>
<li>position</li>
<li>years active</li>
<li>Olympian status</li>
<li>national team membership</li>
<li>award count</li>
<li>championships won</li>
<li>Instagram following count</li>
<li>Instagram post count</li>

The project ultimately shifted from a simple “performance versus followers” framework into a broader exploration of how social media visibility in sports is shaped by global sports infrastructure, national popularity, branding, and athlete identity.

### Research Focus ###

The central focus of this project is understanding how social media visibility functions within professional volleyball culture. Initially, the project explored the possibility that athletic performance might directly correspond to social media popularity. However, during the collection process, it became clear that digital popularity appears to be influenced by much more than athletic ability alone.

Instead, the dataset increasingly pointed toward larger cultural and institutional systems that shape athlete visibility online. Factors such as nationality, Olympic participation, league prominence, international recognition, and fan culture appeared to influence social media popularity in ways that athletic statistics alone could not fully explain.

As a result, the project evolved into a broader cultural analysis examining how athletes become visible digital figures through the interaction of:

<li>sports media systems</li>
<li>national fan cultures</li>
<li>institutional prestige</li>
<li>globalization</li>
<li>online branding</li>
<li>and social media engagement</li>

Rather than treating follower counts as purely objective indicators of athletic skill, this project approaches digital popularity as a socially constructed form of visibility shaped by multiple overlapping systems.

### How the Data Was Collected ###

I began by manually constructing a list of 80 professional volleyball players. I intentionally selected players from different countries, genders, positions, and professional leagues in order to create a globally representative sample rather than focusing on only one country or one volleyball system. National team rosters, Olympic rosters, professional league rosters, and internationally recognized athletes were used as starting points for player selection.

For each athlete, I manually verified their identity before collecting any social media information. This step was especially important because volleyball athletes often have:

<li>fan pages</li>
<li>duplicate accounts</li>
<li>inactive profiles</li>
<li>repost accounts</li>
<li>outdated usernames</li>

To reduce the possibility of incorrect data collection, accounts were verified through several methods:

<li>Instagram verification badges when available</li>
<li>official team or federation links</li>
<li>consistent posting history and player imagery</li>
<li>cross references with club or national team accounts</li>

Only accounts that could reasonably be identified as official athlete accounts were included in the dataset.

After verification, Instagram statistics were collected and entered into a spreadsheet. Additional institutional and cultural variables such as Olympian status, national team membership, award count, championships won, nationality, and league country were collected manually using publicly available player information.

### The Tools I Used ###

Several tools were used throughout the construction and organization of the dataset.

The dataset was initially organized using Apple Numbers before later being exported into CSV format for computational analysis and cleaning. Python scripts and web scraping workflows were explored for automating portions of the data collection process, particularly social media statistic retrieval and data organization from websites like Instastatistics.

The primary tools explored included:

<li>Python</li>
<li>BeautifulSoup</li>
<li>Requests</li>
<li>Instaloader</li>
<li>third-party Instagram statistics websites</li>
<li>spreadsheets and CSV processing tools</li>

These tools helped automate portions of the workflow, especially data cleaning and attempted retrieval of social media statistics. However, many scraping methods proved unreliable because social media platforms frequently block scraping attempts or fail to distinguish between official athlete accounts and fan pages.

Because of this, the project ultimately used a hybrid methodology:

computational tools assisted with searching, organization, and cleaning
manual verification ensured account authenticity and dataset accuracy

This allowed the project to satisfy the computational requirements of the assignment while still maintaining methodological rigor.

### Methodological Decisions ###

Several important methodological decisions shaped the final dataset.

#### Geographic Representation ####

Players from multiple countries were intentionally included because volleyball popularity and media visibility vary significantly across regions. Countries such as Japan, Brazil, Turkey, Italy, and Poland often have stronger volleyball fan cultures and more visible media ecosystems, which can substantially affect athlete popularity online.

Nationality and league country were therefore treated as meaningful cultural variables rather than neutral background information.

#### Gender Representation ####

Both men’s and women’s volleyball players were included because digital visibility and branding may operate differently across gendered sports spaces. Gender was included not simply to “remove bias,” but because it may shape sponsorship opportunities, audience engagement, and athlete visibility.

#### Verification Standards ####

Account verification became one of the most important parts of the project. Fully automated scraping methods proved unreliable because many athletes have unofficial fan accounts or accounts with the same name.

For this reason, manual verification remained necessary even when computational tools were used.

#### Social Media Metrics ####

Only permanent Instagram feed posts were counted. Temporary stories and disappearing content were excluded because they are difficult to archive consistently and would reduce reproducibility.

Follower and post counts were also standardized into numerical values to make computational analysis possible.

#### Cultural Context and Relevance ####

One of the most important realizations during this project was that social media popularity in professional volleyball is deeply connected to culture rather than performance alone.

Volleyball operates very differently across countries. In some countries, volleyball is a major spectator sport with strong fan communities and extensive media coverage, while in others it receives far less cultural attention. Because of this, athletes from countries with stronger volleyball media ecosystems often accumulate substantially larger online audiences regardless of whether their athletic ability is objectively higher.

For example:

Japanese volleyball players often had extremely large follower counts due to strong domestic fan culture and media attention.
Brazilian and Turkish players also tended to have significantly larger audiences because volleyball has major cultural visibility in those countries.
Athletes from countries where volleyball is less commercially visible often had much smaller online audiences despite competing at similarly high professional levels.

This suggests that digital popularity is shaped not only by athletic performance, but also by:

<li>national identity</li>
<li>media infrastructure</li>
<li>institutional prestige</li>
<li>globalization of sports media</li>
<li>sponsorship visibility</li>
<li>fan culture</li>
<li>and league prominence</li>

The dataset therefore became less about identifying “the best players” and more about understanding how sports culture and digital media shape athlete visibility online.

### Challenges I Faced ###

One major challenge was identity verification. Many athletes had multiple social media accounts, fan pages, or inactive profiles, which made it difficult to determine which account was official. This became especially difficult for international athletes whose accounts existed in different languages or naming formats.

Another challenge was automation. While computational tools were helpful for organization and attempted scraping, Instagram and related websites frequently blocked requests or returned incomplete data. Fully automated scraping workflows proved unreliable for account verification, requiring manual confirmation for many entries.

The constantly changing nature of social media metrics was another limitation. Follower counts and post counts change daily, meaning the dataset only captures a snapshot of a particular moment in time rather than a permanently fixed dataset. To address this issue, data collection dates were recorded alongside the dataset.

Finally, popularity itself proved difficult to define. Some athletes posted constantly but maintained relatively modest audiences, while others rarely posted yet still attracted extremely large followings due to Olympic participation, national recognition, or institutional prestige.

### What I Noticed During Collection ###

Several patterns became noticeable during the collection process.

The strongest pattern was that nationality appeared to heavily influence social media visibility. Athletes from countries with stronger volleyball fan cultures consistently had substantially larger audiences than athletes from countries where volleyball receives less media attention.

I also noticed that posting frequency did not necessarily correspond to popularity. Some athletes posted frequently without gaining exceptionally large audiences, while others posted rarely yet maintained extremely large followings. This suggested that audience size may depend more on institutional prestige, national recognition, and media visibility than simply online activity levels.

Another noticeable trend was the relationship between international competition and visibility. Olympians and national team players often appeared to have significantly larger audiences than players who primarily competed only at the club level.

These observations gradually shifted the project away from a simplistic “better performance equals more followers” assumption and toward a broader cultural framework focused on digital visibility and sports identity.

### Preliminary Analysis and Inferences ###

Although the dataset is still exploratory, several early inferences can already be drawn from the collection process.

The dataset suggests that social media visibility in professional volleyball is shaped more strongly by cultural, institutional, and national factors than by athletic performance alone. Athletes who compete in globally visible volleyball systems or represent countries with large fan cultures often maintain significantly larger online audiences regardless of whether their athletic statistics are objectively higher.

For example, athletes from Japan, Brazil, Turkey, and Italy frequently appeared to have disproportionately large followings relative to players from countries where volleyball receives less media attention. This suggests that fan culture and national sports infrastructure may influence digital popularity as much as individual athletic achievement.

Olympic participation and national team membership also appeared to increase visibility substantially. Players associated with international competition often maintained stronger digital presence even when their posting frequency remained relatively low. This may indicate that institutional prestige and symbolic national representation contribute heavily to audience formation.

The dataset also suggests that online visibility is not determined solely by content production. Some athletes who posted frequently did not necessarily maintain large audiences, while others with minimal activity still attracted substantial followings. This implies that visibility may emerge from broader systems of media circulation, branding, sponsorship, and institutional recognition rather than simply from posting behavior itself.

Overall, these observations support the idea that professional athletes function not only as competitors, but also as digital cultural figures whose popularity is shaped through globalization, national identity, media systems, and online fan communities.

### What the Dataset Can and Cannot Tell Us ###

This dataset is useful for examining patterns of digital visibility, institutional recognition, and sports culture within professional volleyball. It can help explore relationships between:

<li>nationality and social media popularity</li>
<li>institutional prestige and online visibility</li>
<li>league prominence and audience size</li>
<li>gender and athlete branding</li>
<li>national team participation and follower growth</li>
<li>globalization and digital fan culture</li>

However, the dataset cannot directly determine causation. A large follower count does not necessarily mean an athlete performs better, and athletic performance alone cannot fully explain digital popularity. Social media visibility is shaped by multiple overlapping cultural, institutional, and economic systems.

The dataset should therefore be interpreted as a study of sports culture and digital visibility rather than a purely statistical ranking of athletic ability.

### Final Reflection ###

Building this dataset significantly changed the direction of the project. What initially began as a simple comparison between social media activity and athletic performance evolved into a broader investigation of how athletes become visible cultural figures online.

The project also demonstrated the importance of methodological transparency in digital research. Automated systems alone were insufficient because identity verification, cultural context, and platform ambiguity required human judgment. At the same time, computational tools still played an important role in organizing, scaling, and cleaning the dataset.

Overall, this dataset suggests that social media popularity in professional sports is not determined by performance alone. Instead, athlete visibility appears to emerge from the interaction between digital media platforms, national sports cultures, institutional prestige, globalization, and personal branding.

## Individual Component — SportsBuddy

**Authors:** Tica Lin, Ruxun Xiang, Gardenia Liu, Divyanshu Tiwari, Meng-Chia Chiang, Chenjiayi Ye, Hanspeter Pfister, Chen Zhu-Tian
**Title:** SportsBuddy: Designing and Evaluating an AI-Powered Sports Video Storytelling Tool Through Real-World Deployment
**Year:** 2025
**URL:** https://arxiv.org/abs/2502.08621


---

### Part 1: AI Summary

**Prompt:** In one to two paragraphs, please summarize the following article: "SportsBuddy: Designing and Evaluating an AI-Powered Sports Video Storytelling Tool Through Real-World Deployment," in terms of how it uses computational methods and what it is trying to accomplish in the context of sports.

"SportsBuddy is an AI-powered sports video authoring tool that aims to lower the barrier for coaches, athletes, content creators, and fans who want to create engaging sports highlight videos. The system uses several computational methods — player tracking via MixSort, pose estimation via MMPose, foreground-background segmentation via Mask R-CNN, and AI captioning via GPT-4o — to automatically process uploaded sports videos. Instead of manually placing graphics frame by frame, users can attach visualizations directly to tracked players, annotate tactical breakdowns, and add narrative captions with minimal technical skill.

The paper evaluates SportsBuddy through a real-world deployment over three months, attracting over 150 users across different sports roles. Case studies with Harvard Athletics and basketball content creators on YouTube and Instagram show the tool's impact on coaching communication, game analysis, and fan engagement. The article argues that domain-specific AI tools are more valuable than general generative tools for sports contexts because they center human expertise and require precise synchronization of data visualizations with dynamic footage."

---

### Part 2: Critical Assessment

**What is the Data?**

The data in this paper is sports video footage uploaded by the tool's users: coaches, athletes, content creators, and fans — across sports like basketball, soccer, volleyball, lacrosse, and tennis. This isn't a fixed dataset, it heavily relies on its user base which makes it interesting but also harder to evaluate. Over three months, 1,021 videos were uploaded and 814 highlights were exported. The case focus mainly on Harvard Athletics and a handful of basketball influencers, which skews the evaluation toward more fortunate, high-visibility users. What the data misses is a lot, the paper treats sports video as a neutral medium for communicating insight, but it doesn't get too deep into the actual insights, or what kinds of moments and players get highlighted versus ignored. 

**How is Computation Used and Why?**

The computational methods here cover: MixSort tracks players across frames, MMPose estimates poses, Mask R-CNN segments players from the background, and GPT-4o generates captions from sampled frames. These all run in a parallel pipeline built for the user. The primary purpose is augmentation and communication. Computation prepares the video and executes how insights are visualized and shared. This is different from papers that use computation to make an argument. SportsBuddy is more like infrastructure that lets users make their own arguments with examples. Computation is definitely necessary here since no one could do frame-by-frame tracking manually at scale. 

---

### Part 3: What AI Missed

The AI summary did a decent job covering the computational parts and the deployment context, but it mostly just reproduced the paper's own perspective without 'critically' thinking about it. It didn't flag that the case studies are hand-picked and the user feedback is almost entirely positive, with no real serious counters. It also missed the question of what it means for computation to be making interpretive decisions on behalf of users — the GPT-4o captioning pipeline is deciding what's "relevant" in each video frame, and the paper never questions that. It also had no language for the gap between what the paper actually measures (upload rates, export counts, follower numbers) and the broader claims it makes about storytelling and coaching effectiveness, which is a meaningful gap but one that's easy to miss if you're just summarizing at face value.

---
layout: post
title: "Three That Talk"
date: 2026-10-08 11:30:00 +0000
excerpt: "Three agents sharing a folder match a dozen working alone. Agreement between them still isn't evidence."
---

![Three desk lamps lit around one shared notebook, a wall calendar behind with a day circled](/assets/images/2026-10-08-three-that-talk.webp)

Last week an agent told me, with some confidence, why our GitHub bill had gone up. Old launchers on people's laptops were re-downloading packages. It had the numbers, it had a report, and it was wrong. By Monday morning the same agent had found the real cause: a mirror I'd built, running hourly on one of our boxes and fetching about two gigabytes of packages it already had on every pass. Twenty-odd dollars a day. The first report had been plausible enough that we'd nudged the whole team to update their launchers.

So on Tuesday I started mobbing. There's a paper from September, [Scaling Discovery through Test-Time Communication](https://arxiv.org/abs/2609.21032), with a result I'd half remembered as three that talk beat thirteen alone. The real figure is close enough. A team of agents that can talk to each other matches about four times as many working independently, and the gap widens as you scale. The catch is in the abstract too: it needs enough compute and a clear measure of progress. Without those, the loners do better.

The setup is a folder on the compute box. One subfolder per question, with a brief in it, which can be as rough as I like. Three seats, one Claude in the chair and two GPTs, all running at once in the same folder. Each writes its first take before reading anyone else's, so the first takes stay independent. After that each keeps a running log and appends to it, a timestamped entry for every finding, challenge or change of mind. Every couple of minutes they read the other two logs and respond by name: check the numbers, challenge what looks wrong, concede what's right. At about twenty-five minutes the chair writes a verdict under 350 words, with actions and owners, and any disagreement left over is marked by seat. The others sign off, agree or disagree, until it settles.

<img class="drawing-light" src="/assets/images/2026-10-08-three-that-talk-drawing.webp" alt="One folder on the compute box. Three seats, Claude in the chair and two GPTs, each writing its own log and reading the other two every couple of minutes. Below them a verdict under 350 words ending with How we will know, a reading and a date, and an arrow to you taking that reading on the day">
<img class="drawing-dark" src="/assets/images/2026-10-08-three-that-talk-drawing-dark.webp" alt="One folder on the compute box. Three seats, Claude in the chair and two GPTs, each writing its own log and reading the other two every couple of minutes. Below them a verdict under 350 words ending with How we will know, a reading and a date, and an arrow to you taking that reading on the day">

I ran two that first morning while I got on with other things. The chair's log reads like a decent meeting. "To astra-1: conceded. I was wrong to call it a single disk in the same office." A few minutes later it corrected its own figures against the live data, the object store being 665 megabytes rather than the three gigabytes it had claimed, having conflated two numbers. Both verdicts landed within a quarter of an hour of the seats starting. One raised a budget cap that was days from freezing everyone's merges. The other told me I was half right about the mirror: running it hourly was pointless, but keeping it wasn't.

That second one was my favourite. I'd read the diagnosis and gone off on one about whether a ten-person startup had baked in a load of redundancy it didn't need, and finished with "I'm probably wrong about loads of this, aren't I?" Then it occurred to me that I could feed exactly that into a mob, doubts and all, as the brief. The question doesn't have to be tidied up before it goes in. That is more fun than it sounds.

Within two days there had been six. The bill, the budget, the mirror, what to do about shared Wi-Fi, whether to put everyone on the VPN. I've stopped thinking of it as a thing to set up. If a question is murky, it goes in a folder.

Then, while I was out, the obvious worry. We'd had a confident wrong answer on Monday, so how would I know when the mob was wrong? Three seats agreeing doesn't tell you much. They've read the same documents, they share the same blind spots, and models are agreeable by nature. What caught Monday's error was a number rather than a second opinion: the bill matched the mirror's download volume to within one percent.

So every verdict now ends with a line that starts "How we will know", naming a reading and a date that would prove it wrong. For the Wi-Fi one, a test sheet by the 14th showing no traffic outside the tunnel on all three operating systems, and an invoice under twenty dollars. For the mirror, a full day's bill after the fix. Someone, usually me, takes the reading on the day. Agreement is a feeling, and a prediction that reality can check is evidence.

The first readings fall due next week. I'll find out then whether three that talk beat thirteen alone, or whether they just agreed with each other faster.

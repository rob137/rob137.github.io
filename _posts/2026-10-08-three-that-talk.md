---
layout: post
title: "Three That Talk"
date: 2026-10-08 11:30:00 +0000
excerpt: "Three agents in one folder, and a line at the end of every verdict saying how we'd know it was wrong."
---

![Three desk lamps lit around one shared notebook, a wall calendar behind with a day circled](/assets/images/2026-10-08-three-that-talk.webp)

Last week an agent told me why our GitHub bill had gone up. Old launchers on people's laptops were re-downloading packages. It had a report with numbers in it and we acted on it, nudging everyone to update. On Monday morning the same agent came back and said that was wrong. The real cause was a mirror I'd built, which runs hourly on one of our boxes and was fetching about two gigabytes of packages it already had, every pass. Twenty-odd dollars a day.

So on Tuesday I started mobbing. There's a paper from September, [Scaling Discovery through Test-Time Communication](https://arxiv.org/abs/2609.21032), which I'd half remembered as three agents that talk beat thirteen working alone. The actual figure is that a team of agents that can talk to each other matches about four times as many working independently, and the gap grows as you add more. There's a caveat in the abstract: you need enough compute and a clear measure of progress, otherwise the loners do better.

Here's how I run it. A folder on the compute box, one subfolder per question, with a brief in it. The brief can be as rough as I like. Three seats, one Claude in the chair and two GPTs, all running at once in the same folder. Each writes its own first take before reading anyone else's. After that each keeps a log and adds to it as it goes, a timestamped entry for every finding or change of mind. Every couple of minutes they read each other's logs and respond by name, checking the numbers and conceding where they're wrong. After about twenty-five minutes the chair writes a verdict under 350 words, with actions and owners, and the other two sign off, or say why not.

<img class="drawing-light" src="/assets/images/2026-10-08-three-that-talk-drawing.webp" alt="One folder on the compute box. Three seats, Claude in the chair and two GPTs, each writing its own log and reading the other two every couple of minutes. Below them a verdict under 350 words ending with How we will know, a reading and a date, and an arrow to you taking that reading on the day">
<img class="drawing-dark" src="/assets/images/2026-10-08-three-that-talk-drawing-dark.webp" alt="One folder on the compute box. Three seats, Claude in the chair and two GPTs, each writing its own log and reading the other two every couple of minutes. Below them a verdict under 350 words ending with How we will know, a reading and a date, and an arrow to you taking that reading on the day">

I ran two that first morning while I got on with other stuff. The chair's log reads like a decent meeting. "To astra-1: conceded. I was wrong to call it a single disk in the same office." A bit later it corrected its own numbers against the live data, 665 megabytes rather than the three gigabytes it had claimed. Both verdicts were in within a quarter of an hour. One raised a budget cap that was a few days from freezing everyone's merges. The other said I was half right about the mirror. Running it hourly was pointless, but keeping it wasn't.

I enjoyed the second one. I'd read the diagnosis and gone off on one about whether a ten-person startup needed any of this redundancy, and finished with "I'm probably wrong about loads of this, aren't I?" Then it occurred to me that I could just feed that in as the brief, doubts and all. That's fun. You don't have to tidy the question up first.

By Wednesday there had been six. The bill, the budget, the mirror, what to do about the office Wi-Fi, whether to put everyone on the VPN. It's stopped feeling like a thing to set up. If something's murky it goes in a folder.

One thought I had while I was out: how do I know they're right? We'd had a confidently wrong answer on Monday. Three seats agreeing doesn't tell you much, because they've read the same documents and share the same blind spots, and models tend to agree with each other anyway. What actually caught Monday's mistake was a number. The bill matched the mirror's download volume to within one percent.

So each verdict now ends with a line starting "How we will know", which names a reading and a date that would prove it wrong. For the Wi-Fi one it's a test sheet by the 14th showing nothing leaving the laptops outside the tunnel, and an invoice under twenty dollars. For the mirror it's a full day's bill after the fix. Someone takes the reading on the day, usually me.

The first ones fall due next week. I'll say how they go.

---
layout: post
title: "Vestigial Patterns"
date: 2026-01-08 11:00:00 +0000
tags: [ai, llm, github, tailwind, workflow]
excerpt: "I pushed a repo to GitHub out of habit. Then I wondered why."
---

I wanted to detect plosives in audio recordings. I'm having early thoughts about podcasting, and I figured I'd record into QuickTime and listen back.

But why settle for that when I can point Claude at the file and ask it to highlight any plosives? Which it does, gleefully.

![Claude's plosive analysis](/assets/images/plosive-analysis.png)

After a few iterations I had something useful. At this point I naturally thought: *this is where I'd make a GitHub repository*. Crystallize the work. So I did.

Then I pushed, and realised: I hadn't written any code. Claude is marked as a contributor. The whole thing was generated just-in-time. The [repository](https://github.com/rob137/plosifs) exists, but it's really just a little script.

Why did I push?

## The Ritual

The user interfaces are still there, acting as if nothing has changed. GitHub still invites you to create repositories. The green contribution graph still fills up. The star count still exists.

But the value of a GitHub repository as a marker of competence is declining. Below a certain level of complexity, code is increasingly generated. The ritual persists after the meaning has drained out.

I followed the same patterns that made sense two years ago, when they've become somewhere between redundant and absurd.

## The Tailwind Case

This week, a [PR was closed](https://github.com/tailwindlabs/tailwindcss.com/pull/2388) on the Tailwind CSS repository. Someone wanted to add an `llms.txt` endpoint - optimized docs for LLM consumption.

Adam Wathan, the maintainer, [explained](https://github.com/tailwindlabs/tailwindcss.com/pull/2388#issuecomment-3717222957) why he couldn't prioritize it:

![Adam Wathan's comment on the Tailwind PR](/assets/images/tailwind-layoffs.png)

Tailwind is more popular than ever. But the traffic that used to flow through docs - where people discovered paid products - now flows through LLMs that have already ingested those docs. The business model assumed a world where humans read documentation. That assumption broke.

## The Flood

There's a flood of traffic using LLMs and code, undermining loads of assumptions.

My plosive detector didn't need a repository. Tailwind's docs don't need human visitors anymore. GitHub's contribution graphs don't signal what they used to.

The interfaces are still sitting there, as if nothing has changed. We keep following the same patterns. But the ground has shifted underneath them.

I'm not sure what the new patterns are. I'm not sure anyone is yet. But I'm trying to notice when I'm doing something out of habit rather than because it still makes sense.

This pattern is playing out again. AI is becoming [the great attractor](/2026/01/05/the-great-attractor/) for all computer tasks.

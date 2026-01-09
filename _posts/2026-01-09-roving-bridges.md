---
layout: post
title: "Roving Bridges"
date: 2026-01-09 10:00:00 +0000
tags: [ai, llm, workflow, testing, agents]
excerpt: "The bridge was a workaround for a dumb horse. But the horse is getting smarter."
---

![Bridge 77, Macclesfield Canal](/assets/images/roving-bridge.jpg)
*Bridge 77 on the Macclesfield Canal - a roving bridge*

On the Macclesfield Canal, there's a type of structure called a roving bridge. When the towpath changes sides, the bridge lets the horse cross without being untethered from the barge. The horse doesn't need to understand the bridge's design. It just follows the path.

Yesterday, Doug O'Laughlin on the [Transistor Radio](https://www.semianalysis.com/) podcast was talking about his recent discovery of how useful Claude Code with Opus 4.5 is. Something he said stuck with me:

> "It's a skill issue now. Like, I'm really telling you, it's all a skill issue... I think everything that is a problem is a skill issue on my end. I believe that... for the first time in my life, there is nothing - it is completely on me, it's a skill issue. I deeply believe that."

Everything is a skill issue now. Master the tools or get left behind.

## Task vs Purpose

In 2016, Geoffrey Hinton made a famous prediction:

> "People should stop training radiologists now. It's just completely obvious within five years deep learning is going to do better than radiologists."

Hinton was right about the task. AI now powers essentially all radiology applications. But the number of radiologists *increased*.

Why? Jensen Huang, on [No Priors](https://www.youtube.com/@NoPriorsPodcast) the same day as Doug's podcast, offered a framing:

> "A job has tasks and has purpose. In the case of a radiologist, the task is to study scans. But the purpose is to diagnose disease."

When radiologists could study more scans more deeply, hospitals became more productive. More patients, more revenue, more demand for radiologists. The task got automated. The purpose expanded.

Huang extended this to software engineers:

> "The purpose of a software engineer is to solve known problems and to find new problems to solve. Coding is one of the tasks. If your purpose literally is coding - somebody tells you what to do, you code it - all right, maybe you're gonna get replaced by the AI. But most of our software engineers, their goal is to solve problems."

## Building Bridges

At work, I'm on a skunk works team. We have a project called Briefcase - named after Will from [The Inbetweeners](https://en.wikipedia.org/wiki/The_Inbetweeners) - that uses git worktrees to parallelise small units of work across multiple LLM instances.

I also have an "octopus" prompt that sets up a central LLM as a coordinator: it creates worktrees, spawns worker instances, then pulls branches back and runs tests. The pattern is everywhere right now - people building infrastructure to work around model limitations.

This is bridge-building. The horse is too stupid to cross the canal on its own, so you build an elegant structure that routes it where it needs to go.

## The Crystallisation Hierarchy

There's an old idea from [Alistair Cockburn](https://en.wikipedia.org/wiki/Alistair_Cockburn) about preferring richer communication channels. Paper is worse than email, email is worse than a call, a call is worse than being in the room together. Higher bandwidth, faster feedback, fewer misunderstandings.

I've started thinking about AI workflows the same way:

1. **Manual**: Use the browser yourself. Click around. Understand what's happening.
2. **Agentic**: Have a coding agent use browser automation tools - Playwright MCP, Chrome DevTools MCP. It figures things out dynamically.
3. **Deterministic**: Crystallise what matters into a script or test. If you liked it, put a test on it - [the Beyoncé rule](https://landing.google.com/sre/sre-book/chapters/testing-reliability/).

Early on at work, I tried using LLMs to handle deployment tasks. It was okay-ish at first, but became a disaster. You could never get it to 100%. The models would come up with their own ideas about how things could be better, or misunderstand instructions. It mattered.

So we wrote a script. Wrong reliably, therefore right reliably once fixed.

The temptation is to skip straight to agentic. Everyone's excited about agents managing things dynamically. But you probably want to start with manual understanding before escalating. And if something matters - if you'd be upset when it breaks - you shouldn't skip the crystallisation step.

## The Horse Is Getting Smarter

Here's the thing though. As models get better at tool calling and figuring things out on the fly, I'm becoming more comfortable doing things the agentic way. The elaborate scaffolding starts to feel unnecessary.

The roving bridge was a clever workaround for a dumb horse. You wouldn't build it today. If the horse could figure out how to cross on its own, the bridge would just be a curiosity - beautiful, perhaps, but antiquated.

I think we're in an awkward middle period. The "skill issue" framing is real: there's genuine alpha in mastering the current tooling, building the bridges, understanding how to route the horse. But the half-life of that knowledge is shrinking.

The bridges I'm building now may be obsolete in months. The octopus prompt, the worktree orchestration, the crystallised scripts - all workarounds for limitations that are actively being eroded.

Maybe the real skill isn't building bridges. Maybe it's knowing when to stop.

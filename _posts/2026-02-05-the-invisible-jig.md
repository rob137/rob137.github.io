---
layout: post
title: "The Invisible Jig"
date: 2026-02-05 10:00:00 +0000
tags: [ai, tools, workflow]
excerpt: "Orchestrator apps hide context from the thing doing the work."
---

Good week for OpenAI. GPT 5.2 Codex is 40% faster than last week. They're offering 2x rate limits if you use the macOS desktop app. I gave it a spin.

However.

A colleague switched from Claude Code to the Codex app because of the higher limits. Within a week he messaged me: "Codex is an absolute pain to talk to compared to Claude Code." It keeps questioning his decisions. Claude Code just gets him.

I think the Codex Desktop app is basically a poor man's Claude Code prompt.

Here's what I mean. The Codex app lets you click to start new conversations that spin up fresh worktrees. At first that seems elegant - each ticket gets its own isolated environment, everything wired up automatically.

Until you realise the models have no clue what workflow they're in.

The context is implicit in the harness code. The model can't see it. So you keep having to explain what's actually happening, which comes as a surprise to them. You're educating the models about their own environment.

A harness is great for improving today's workflow. But it's behavior you can encode through natural language instead. And when you do, the model can actually reason about it. Notice conflicts. Adapt to edge cases. A prompt is visible to the thing doing the work. A GUI isn't.

So I'm back to using Claude Code as my concierge with an [orchestrator prompt](/2026/01/21/orchestrator) - it manages worktrees and coordinates headless Codex instances running in the background. Better at talking anyway. More flexible than hard-coded buttons. With the caveat that none of my workflows seem to last very long given the rate of progress.

And in the meantime, I'm conscious that the bitter lesson is coming for all of this. Models will absorb these workflows. I'd be loath to become reliant on scaffolding I don't control when it's only a matter of time till the models consume the majority of it anyway.

![METR task duration graph](/assets/images/metr-task-duration.jpeg)

The Codex app isn't bad because it's OpenAI. It's bad because it puts the intelligence in the wrong place - in code the model can't see, rather than language it can reason about.


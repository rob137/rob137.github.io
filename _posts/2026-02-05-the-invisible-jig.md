---
layout: post
title: "The Invisible Jig"
date: 2026-02-05 10:00:00 +0000
tags: [ai, tools, workflow]
excerpt: "Orchestrator apps hide context from the thing doing the work."
---

Good week for OpenAI. GPT 5.2 Codex is 40% faster than last week. They're offering 2x rate limits if you use the macOS desktop app. I gave it a spin.

However.

James Whiting, a colleague, switched from Claude Code to the Codex app because of the higher limits. Within a week he messaged me: "Codex is an absolute pain to talk to compared to Claude Code." It keeps questioning his decisions. Claude Code just gets him.

I think the Codex Desktop app is basically a poor man's Claude Code prompt.

Here's what I mean. I built an orchestrator workflow for a client project - worktrees, naming conventions, delegation commands, the works. At first I was excited: click new conversation, get a fresh worktree, everything wired up. Elegant.

Until I realised the models had no clue what workflow they were in.

The context was implicit in the harness code. The model couldn't see it. So I kept having to explain what was actually happening, which came as a surprise to them. I was educating the models about their own environment.

A harness is great for improving today's workflow. But it's behavior you can encode through natural language instead. And when you do, the model can actually reason about it. Notice conflicts. Adapt to edge cases. A prompt is visible to the thing doing the work. A GUI isn't.

So now I use Claude as my concierge with an orchestrator prompt. Better at talking anyway. More flexible than hard-coded buttons.

And in the meantime, I'm conscious that the bitter lesson is coming for all of this. Models will absorb these workflows. I'd be loath to become reliant on scaffolding I don't control when it's only a matter of time till the models consume the majority of it anyway.

The Codex app isn't bad because it's OpenAI. It's bad because it puts the intelligence in the wrong place - in code the model can't see, rather than language it can reason about.


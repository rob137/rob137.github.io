---
layout: post
title: "To-Do Lists as Prompts"
date: 2026-01-02 15:30:00 +0000
tags: [ai, llm, productivity, workflow, prompts]
---

I keep finding to-do items in my notes that look like this:

> **Mission:** build the local PoC for the legal-doc-task-engine-prototype.
>
> **Success looks like:** from localhost you can drop an old scanned PDF and, within minutes, hit `http://localhost:8000/docs` to see the Markdown OCR output and a JSON extraction returned by `GET /contract/{id}`.
>
> No Azure subscription is required yet; we use Azurite, SQLite and local Azure Functions Core Tools to emulate the cloud.

That's not a to-do item. That's a prompt.

## Writing vs Speaking

Here's what changed: writing something down is harder than saying it out loud.

When I type a to-do, I optimise for brevity. "Build legal doc PoC" - three words, move on. The friction of typing makes laconic notes feel efficient.

When I dictate, I explain. I talk as if to a new person joining my project. I describe what success looks like. I mention the constraints. I think out loud about the scope.

Speech-to-text flipped the economics. Detailed specifications are now cheaper to produce than terse ones.

## The paradigm shift

If you're explaining something as if to a new person with a view of your project, you're a hop and a skip away from opening a terminal and typing it there instead of into your notes file.

Why keep prompts when you could send them?

The latency on prompt completion these days is usually several minutes for a meaningful task. In some ways you're better off parking them in a language model harness - Claude Code, Codex, the ChatGPT web UI - and letting it run. The thing will pop out of the microwave in 15 minutes. Intellectually you're free to think about other things.

## Multiple work streams

Of course, you might want to keep things for later. Maybe you're using Git in a way that doesn't permit multiple agents running on the same codebase. Or maybe the idea of [multiple worktrees](https://code.claude.com/docs/en/common-workflows) doesn't appeal to you for whatever reason.

That's fine. Keep your prompts.

But consider: rather than keeping to-do items, you're keeping prompts. And rather than keeping prompts, you might just send them.

## What needs to be baked in

If you're going to fire and forget, a few things need to be either baked into the environment or stated explicitly in the prompt:

**What success looks like.** Not just "build the thing" but "success looks like: from localhost you can drop an old scanned PDF and see the JSON extraction."

**How you might validate.** Tests that pass. A smoke test that runs. A URL you can hit.

**The scope.** This is something you figure out dynamically by working with models. After a while you develop intuitions about what size a common task ought to be. Too big and the agent loses coherence. Too small and you're micromanaging.

## The workflow

1. Talk. Explain what you want as if to a new team member.
2. Capture. Speech-to-text drops it into a note or directly into a terminal.
3. Send. Park it in a harness and let it run.
4. Review. Come back when it's done. Check the output.

The to-do list becomes a prompt queue. The notes file becomes a backlog of specifications waiting to be executed.

It's a small shift in framing. But it changes how you think about what you're writing down.

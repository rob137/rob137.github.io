---
layout: post
title: "Vibe Orchestration"
date: 2026-01-06 14:00:00 +0000
tags: [ai, metaphors, workflow, agents]
excerpt: "Justin Bieber conducting an orchestra by humming. That might be closer to where we're heading."
---

There's a [video of Justin Bieber](https://x.com/reidhoffman/status/1873756306013901051) conducting an orchestra by humming fragments of tunes and explaining how he wants them combined. No sheet music. No formal notation. Just vibes, translated into something precise by people who know how.

That might be closer to where we're heading than our current metaphors suggest.

## The chairs we sat in

In [The Music Stopped](/2026/01/02/the-music-stopped/), I wrote about how the IDE versus terminal debate was becoming irrelevant. Not because one side won, but because the underlying activity changed. We sat down in whatever chairs were closest when the music stopped.

But I think what's actually lacking is better metaphors for what we're doing now.

[near](https://x.com/nearcyan/status/2008321468397220174) put it well: "coding a la factorio or starcraft is cool, but what if instead it felt more like playing an instrument."

[Karpathy agreed](https://x.com/karpathy/status/2008351926350737699): "Yep exactly, just like this. Better analogy because it's not effortful."

[Michael Nielsen](https://en.wikipedia.org/wiki/Technologies_in_Minority_Report) noted that Steven Spielberg's instruction to the interface designers for Minority Report was: "Make it like conducting an orchestra."

The metaphor keeps surfacing. Maybe there's something to it.

## Ralph Wiggum

[Geoff Huntley](https://ghuntley.com/) has been advocating for an approach he calls Ralph Wiggum, after the Simpsons character. You put a change request in an agent-operated loop that only quits when the agent is satisfied things are done. You might set an upper limit to prevent infinite runs, but basically you're setting success criteria and forcing it to run at the problem until tests pass.

This was in papers as early as 2024. Models turned out to be much better at completing problems when forced to keep going against tests. The early examples were performance optimisation - the models could hill-climb pretty well. But that didn't get much attention.

Ralph Wiggum sticks, though. Now everyone's talking about it. Names matter. Metaphors matter. The technical capability was there before the framing arrived to make it legible.

## What's missing

We're still reaching for the right language. Factorio implies effort. Starcraft implies micromanagement. Playing an instrument implies flow. Conducting an orchestra implies directing without doing.

The activity is new. The words will catch up. But until they do, we're stuck describing the thing in terms of whatever came before.

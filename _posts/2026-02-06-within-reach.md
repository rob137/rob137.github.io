---
layout: post
title: "Within Reach"
date: 2026-02-06 12:00:00 +0000
tags: [ai, learning, mental-models]
excerpt: "Transformer research is full of physicists. The barrier to entry is lower than it looks."
---

A colleague shared a screenshot today. Someone had asked Claude why it hallucinated, and Claude produced this confident explanation about "training data contamination" - how the model saw a filename, matched it to patterns from training, and reported issues without reading the actual content.

Sounds plausible. Except models don't actually have a little library in their head where they can look up training documents. They have a tangle of learned associations. When someone says "it's using its training data," that's misleading. The model isn't referencing a source. It's generating what feels right based on similarity to patterns it has seen before.

What you can observe is that certain prompts land the model in a region of its internal representation associated with "getting started docs" or "typical documentation voice." That's a map of patterns, not the territory of actual documents. I've [written about this before](/2026/01/24/thinking-out-loud/) - when you ask a model how it came up with an answer, that explanation is also just a generated guess.

Here's the thing though. This stuff sounds esoteric. The diagrams look intimidating. But a quirk of transformer research these days is it's full of physicists rather than computer scientists. Turns out you can wander in and grok a surprising proportion of the concepts fast with a few minutes of sustained attention. It's basically become a filter for formidable people because the barrier to entry is so low.

A corollary: normies like us can get it much faster than you might think.

I really recommend sitting down with one of the shorter [3Blue1Brown videos](https://www.youtube.com/watch?v=LPZh9BOjkQs). It's going to seem esoteric and boring at first, but anyone can get it pretty fast. The mental model you build has high economic value.

It's disturbing to me that non-ML tech people aren't writing about this stuff much. It's either AI researchers who take it all for granted, or people in HR and marketing on LinkedIn. The middle bit is totally under-served.


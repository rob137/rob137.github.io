---
layout: post
title: "The Upside Down"
date: 2026-01-12 12:00:00 +0000
tags: [ai, llm, coding, culture, economics]
excerpt: "When you scale LLMs to 50 concurrent agents, best practices start to feel sacrilegious."
---

I'm not a best-practices fanatic, but I find them fascinating as cultural artefacts. I've collected the usual books - Gang of Four, Bob Martin, Joel Spolsky, Continuous Delivery, TDD - and toyed with most of the paradigms. Same with religion, honestly. I can listen to any of it anthropologically without getting bound up in doctrine.

From that vantage point, it's interesting how scaled LLM practices feel kind of *sacrilegious*.

## The Industrialists

Ben Holmes asking a reasonable question:

> How do yall manage 10 Claude Codes running at once? Worktrees? Multiple repo clones?

[Jeffrey Emanuel](https://x.com/doodlestein/status/2010395079937040487):

> More like 40-50 at once with no issues. Worktrees suck and just kick the can down the road. Advisory file reservations and messaging ftw.

[Geoff Huntley](https://x.com/GeoffreyHuntley/status/2009970301501911076) on accidentally wiping worktrees:

> I monkey patched git to remove force push. In the end I don't really care cause code is cheap and free now.

## A Reshuffling

The jarring thing is that it's not uniform inversion. It's a reshuffling.

Some practices become *more* important. I recently drifted into TDD for database constraints - not from religious conviction, but because it was the safest approach and didn't require any more energy. Why not? Fast test suites with good coverage matter more now because human testing is the bottleneck. LLMs can push you *toward* best practices, not just away from them.

Some become weirdly malleable. "Do all the work, then split it into separate branches per concern" - absurd to ask of a human, perfectly natural for an LLM.

And some break entirely. Worktrees were fine for parallel work. At 50-agent scale, you need file reservations and inter-agent messaging. Risks we considered solved come back when you scale up.

The quotes above are jarring. But the jarring thing isn't that everything inverts - it's that you can't predict which way each practice will go.

## Factory Farming

This favours people with capital - either their own, or license to spend their employer's.

You can treat software spend as something to minimise, or something to exploit. If spending is how you make money, spend more. But not everyone does spreadsheets that way.

A 30K token budget isn't hobbyist territory. The bedroom tinkerer running 50 concurrent agents is hard to imagine. This is factory farming - industrialising something no individual could do for fun.

If this approach wins, things centralise again. New capability emerges, briefly chaotic and accessible, then capital industrialises it, and scale wins. We've seen this pattern before.

Handmade sandwiches to factory sandwiches. Some people will always prefer artisanal; the economy often picks scale. If this approach wins, the meaning of good craft may change significantly - approaches that once seemed silly or outright forbidden might become reasonable. That's not obviously bad. It's just different.

## The Present Moment

Right now it's fun. SimCity meets Mario Kart - optimisation loops at racing-game pace.

Probably a phase. But I could do this for a while and not get bored.

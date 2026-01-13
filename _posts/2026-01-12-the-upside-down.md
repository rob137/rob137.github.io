---
layout: post
title: "The Upside Down"
date: 2026-01-12 12:00:00 +0000
tags: [ai, llm, coding, culture, economics]
excerpt: "When you scale LLMs to 50 concurrent agents, best practices start to feel sacrilegious."
---

I find best practices fascinating as cultural artefacts. I've collected the usual books - Gang of Four, Bob Martin, Joel Spolsky, Continuous Delivery, TDD - and toyed with most of the paradigms. Same with religion, honestly. I can listen to any of it anthropologically without getting bound up in doctrine.

From that vantage point, scaled LLM practices feel kind of *sacrilegious*.

## The Industrialists

Ben Holmes asking a reasonable question:

> How do yall manage 10 Claude Codes running at once? Worktrees? Multiple repo clones?

[Jeffrey Emanuel](https://x.com/doodlestein/status/2010395079937040487):

> More like 40-50 at once with no issues. Worktrees suck and just kick the can down the road. Advisory file reservations and messaging ftw.

[Geoff Huntley](https://x.com/GeoffreyHuntley/status/2009970301501911076) on accidentally wiping worktrees:

> I monkey patched git to remove force push. In the end I don't really care cause code is cheap and free now.

## A Reshuffling

Not uniform inversion. More of a reshuffling.

Some practices become *more* important. I recently drifted into TDD for database constraints, not from religious conviction, but because it was the safest approach and didn't require any more energy. Why not? Fast test suites with good coverage matter more now because human testing is the bottleneck. LLMs can push you *toward* best practices, not just away from them.

Some become weirdly malleable. "Do all the work, then split it into separate branches per concern." Absurd to ask of a human. Perfectly natural for an LLM.

Others break entirely. Worktrees were an obscure git feature until LLMs came along, then became ubiquitous among the LLM-obsessed. Now, at 50-agent scale, they're seen as having a low ceiling. File reservations and inter-agent messaging replace them. Alien to essential to abandoned in under two years.

## Factory Farming

This favours people with capital - either their own, or license to spend their employer's.

You can treat software spend as something to minimise, or something to exploit. If spending is how you make money, spend more. But not everyone does spreadsheets that way.

A 30K token budget puts this outside hobbyist territory. The bedroom tinkerer running 50 concurrent agents is hard to imagine. This is factory farming - industrialising something no individual could do for fun.

If this approach wins, things centralise again. New capability emerges, briefly chaotic and accessible, then capital industrialises it, and scale wins. We've seen this pattern before.

Handmade sandwiches to factory sandwiches. Some people will always prefer artisanal; the economy often picks scale. If this approach wins, the meaning of good craft may change significantly. Approaches that once seemed silly or outright forbidden might become reasonable.

## The Present Moment

Right now it's fun. SimCity meets Mario Kart - optimisation loops at racing-game pace.

Probably a phase. But I could do this for a while and not get bored.

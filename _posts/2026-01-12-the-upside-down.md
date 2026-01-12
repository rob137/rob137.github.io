---
layout: post
title: "The Upside Down"
date: 2026-01-12 12:00:00 +0000
tags: [ai, llm, coding, culture, economics]
excerpt: "When you scale LLMs to 50 concurrent agents, best practices start to feel sacrilegious."
---

I'm not a best-practices fanatic, but I find them fascinating as cultural artefacts. I've collected the usual books - Gang of Four, Bob Martin, continuous delivery, TDD - and toyed with most of the paradigms. Same with religion, honestly. I can listen to any of it anthropologically without getting bound up in doctrine.

From that vantage point, it's interesting how scaled LLM practices feel kind of *sacrilegious*.

## The Industrialists

[Ben Holmes](https://x.com/BHolmesDev/status/2010189144123998669) asking a reasonable question:

> How do yall manage 10 Claude Codes running at once? Worktrees? Multiple repo clones?

[Jeffrey Emanuel](https://x.com/doodlestein):

> More like 40-50 at once with no issues. Worktrees suck and just kick the can down the road. Advisory file reservations and messaging ftw.

[Geoff Huntley](https://x.com/GeoffreyHuntley) on accidentally wiping worktrees:

> I monkey patched git to remove force push. In the end I don't really care cause code is cheap and free now.

## A Reshuffling

It's not uniform inversion. More of a reshuffling.

Some practices become *more* important. Fast test suites with good coverage matter more now because human testing is the bottleneck.

Some become weirdly malleable. "Do all the work, then split it into separate branches per concern" - absurd to ask of a human, perfectly natural for an LLM.

And some break entirely. Worktrees were fine for parallel work. At 50-agent scale, you need file reservations and inter-agent messaging. Risks we considered solved come back when you scale up.

## Factory Farming

This favours people with capital - either their own, or license to spend their employer's.

You can treat software spend as something to minimise, or something to exploit. If spending is how you make money, spend more. But not everyone does spreadsheets that way.

A 30K token budget isn't hobbyist territory. The bedroom tinkerer running 50 concurrent agents is hard to imagine. This is factory farming - industrialising something no individual could do for fun.

If this approach wins, things centralise again. New capability emerges, briefly chaotic and accessible, then capital industrialises it, and scale wins. We've seen this pattern before.

Handmade sandwiches to factory sandwiches. Lower quality, but economics wins. Look at how companies feel about code quality versus bottom lines. You can see which way it goes.

I'm not complaining. Just describing how the world works.

## The Present Moment

Right now it's fun. SimCity meets Mario Kart - optimisation loops at racing-game pace.

Probably a phase. But I could do this for a while and not get bored.

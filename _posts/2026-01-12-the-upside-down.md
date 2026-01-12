---
layout: post
title: "The Upside Down"
date: 2026-01-12 12:00:00 +0000
tags: [ai, llm, coding, culture, economics]
excerpt: "When you scale LLMs to 50 concurrent agents, best practices start to feel sacrilegious."
---

I consider myself intellectually flexible and not especially prone to fanaticism around best practices. But I do find them utterly fascinating as cultural artefacts, and have gradually accrued all the usual books in software engineering as well as some more esoteric ones. TDD, doctrinally pure Agile, pair programming, game programming patterns as per Robert Nystrom, continuous delivery, old school Unix stuff, the Java way of seeing the world, refactoring, microservices, Gang of Four, Bob Martin, low-level game dev, Conway's Law and the inverse Conway manoeuvre, best practices around handling legacy code - the list goes on.

There's something similar for me with religious and spiritual practices. I find them equally interesting and can happily listen to points of view in a sort of anthropological and intellectual exploratory fashion without finding myself particularly bound up with them.

From that vantage point, it's fascinating how the practices being discussed when you scale LLMs feel kind of *sacrilegious*.

## The Industrialists

Here's [Ben Holmes](https://x.com/BHolmesDev/status/2010395079937040487) asking a reasonable question:

> I'll be real: I haven't juggled more than 2-3 coding agent instances at a time (locally anyways). How do yall manage 10 Claude Codes running at once? Worktrees? Multiple repo clones? Something else?

And [Jeffrey Emanuel](https://x.com/doodlestein) replying:

> More like 40-50 at once with no issues. And a mixture of CC, Codex, and Gemini-cli. Worktrees suck and just kick the can down the road. Advisory file reservations and messaging ftw.

Elsewhere, [Geoff Huntley](https://x.com/GeoffreyHuntley) on accidentally wiping worktrees:

> now i don't use worktrees and i monkey patched git to remove force push. in the end i don't really care cause code is cheap and free now. i just ralphed the missing parts.

That last bit references his [Ralph](https://ghuntley.com/ralph) pattern - energetic coding loops with verification steps.

## A Reshuffling

It's not that best practices get uniformly inverted. It's more of a reshuffling.

Some practices become *more* important. A test suite that runs quickly but gives you solid coverage suddenly matters a lot more, because human testing is now the bottleneck. When you're running agents in parallel, the feedback loop that tells you whether something worked has to be automated.

But other things become weirdly malleable. The idea that you might do all your work in one place and then prompt "now make separate branches for each of these concerns" - that's not something I would ever ask a human to do. It's perfectly natural to ask an LLM.

And some things get subverted entirely. Worktrees, which were a perfectly sensible solution for parallel work, start breaking down at 50-agent scale. You end up with advisory file reservations and inter-agent messaging instead. Monkey-patching git to remove force push. The risks we considered a solved numbers game come back to bite you when you scale things up.

## Factory Farming

There's another theme here: this is heading towards agentic practices that favour people who have either cash in the bank they're willing to spend, or license to burn quite a substantial amount of money on behalf of their employer.

You can either treat software spend as something to be minimised or something to be exploited. If spending money on software is how you make money, then it's obviously the right thing to do. But not everyone does spreadsheets that way.

A 30K token budget isn't something tinkerers really expect to take on as a matter of course. The bedroom hobbyist scaling up to 50 concurrent agents is hard to imagine, outside of really well-paid enthusiasts or someone YOLOing on what they hope will be a widely adopted framework.

This is factory farming. You're industrialising something that no individual could do on their own, certainly not for fun. Without capital, you probably can't even get things spinning.

And if this approach turns out to be fruitful, I see things centralising again quite soon. The pattern is familiar: new capability emerges, briefly chaotic and accessible, then capital figures out how to industrialise it, and scale wins.

There are certain compromises we accepted when going from handmade sandwiches to factory-made sandwiches. Arguably, they're far lower quality. But it's clearly what the economy pushed us towards. Now move away from the unrefined culinary habits of office workers and commuters, and look at how companies feel about code quality versus bottom lines. You can kind of see which way things are going to go.

I'm not complaining. I'm just describing the way the world works.

## The Present Moment

Right now, though? It's extremely fun. The kinds of things that agent coding allows you to do, the way of working you have day to day - it's like playing SimCity meets Mario Kart. The optimisation loops of building something complex, but at racing-game pace with that dopamine hit.

I'm sure whatever we're doing right now is just a phase and it will move on again quite soon. But I could trot this out for a while and not get bored.

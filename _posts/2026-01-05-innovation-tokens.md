---
layout: post
title: "Innovation Tokens"
date: 2026-01-05 13:30:00 +0000
tags: [ai, software-engineering, architecture]
excerpt: "Addy Osmani's advice about boring technology choices applies doubly when you're working with AI agents."
---

[Addy Osmani](https://addyosmani.com/blog/21-lessons/) just published a post collecting 21 lessons from his career. The whole thing is worth reading, but this part jumped out:

> Novelty is a loan you repay in outages, hiring, and cognitive overhead.
>
> Treat your technology choices like an organization with a small "innovation token" budget. Spend one each time you adopt something materially non-standard. You can't afford many.
>
> The punchline isn't "never innovate." It's "innovate only where you're uniquely paid to innovate." Everything else should default to boring, because boring has known failure modes.
>
> The "best tool for the job" is often the "least-worst tool across many jobs" - because operating a zoo becomes the real tax.

This is a restatement of Dan McKinley's [Choose Boring Technology](https://mcfunley.com/choose-boring-technology), which has been bouncing around the industry for a decade now. But I think the framing of "innovation tokens" makes it stickier.

## The AI angle

The advice was already good. But I think it applies even more strongly when you're building with AI agents.

I wrote recently about [staying unsurprising for the models](/2026/01/03/position-before-submission/#principle-of-least-surprise). The core idea: every time you deviate from what a model expects - directory structure, naming conventions, architectural patterns - you're spending cognitive overhead in every conversation. The models have to be told, repeatedly, that actually things work differently here.

Osmani's framing sharpens this. You have a limited budget of innovation tokens. Every non-standard choice burns one. And now you're burning it twice: once for human comprehension, once for model comprehension.

The tax compounds. You're "operating a zoo" not just across your human team, but across every agent session that joins your project. And unlike humans, the agents don't gradually learn your quirks. Each session starts fresh.

## Where to spend

The implication: be even more conservative than you would have been. Default to boring harder. Save the innovation tokens for where you're genuinely paid to innovate - probably the domain logic, not the infrastructure.

The payoff is velocity. Boring projects move fast with AI assistance because the models already know how everything works. They're in the middle of the training distribution. No explanations needed.

Position before submission.

---
layout: post
title: "Unneeded Features Are Loans"
date: 2026-07-31 09:00:00 +0000
tags: [software, engineering, ai, llm, language]
excerpt: "We nearly kept a feature because calling it insurance made it sound prudent."
---

This week at work we nearly talked ourselves into keeping a feature because it sounded like insurance.

We have a process that is run repeatedly while a user shapes the result. At points the user can constrain it: this input is fixed now, so do not choose it afresh on the next run. That part is real and useful. The question was what guarantee should surround the constraint.

We had built things so that every accepted constraint was immediately made durable. If the program died before the next natural save point, the human choice would survive.

There is a clean argument for doing this. Generated state can be recomputed; human judgement cannot. If someone has made twenty-five careful choices, asking them to reconstruct the lot after a crash would be bloody annoying. But we did not know whether that was the real workflow. In the use we had actually seen, the loop was short. A crash might mean rerunning the process and entering one or two recent answers again. Nobody had complained, because the workflow barely existed yet.

We had implemented protection against a plausible future rather than an observed problem.

The feature itself had survived a great deal of review and was now rather robust. This made keeping it feel sensible, although money already spent making something robust is gone and should not get a vote. The live question appeared when the next tranche of work was about to make the guarantee spread. Every new route through the system that could apply or alter a constraint would have to honour the same durability promise. Awkward cases would need special handling, and that handling would itself become part of the design.

What had looked like a small safety affordance was beginning to decide the architecture around it.

I had been describing the feature as insurance. Pay a modest premium now and you are protected against a bad day later. This made keeping it sound prudent. Removing it sounded reckless, or at least like penny-pinching.

But software affordances are not much like insurance. The implementation is closer to the principal on a loan, in the sense Addy Osmani meant when he wrote that [novelty is a loan you repay in outages, hiring, and cognitive overhead](/2026/01/05/innovation-tokens/). Interest arrives whenever somebody extends the feature, tests around it, explains it to a new colleague, keeps it compatible with a new abstraction or teaches an agent not to break it. Several of these loans interact, so the cost does not merely add up. Each makes the others harder to service.

This is the cost of carry that gets missed when a feature is described as already built. It is never merely sitting there. It is narrowing the space in which later work can move.

The correct threshold is therefore not whether an affordance could be useful. Nearly everything could be useful. The question is whether it matters enough to become a permanent fact about the system, one that every relevant piece of future work must honour. Where the answer is unclear, it is often cheaper to omit it and follow the screams. A real user losing half an hour of careful input would be strong evidence. A room of engineers and language models imagining that this might happen is not the same thing.

What surprised me was how much changed when we replaced one metaphor with another. No code had changed and we had not discovered a new requirement. We simply stopped calling the feature insurance and started calling it a loan, at which point its future costs became difficult to ignore.

This can sound like prattling about words while practical work waits, but a [mental model](/2026/01/24/thinking-out-loud/) determines which costs are visible, which questions seem natural and which parts of a design appear to belong together.

We had another version of this on the same project. For weeks we developed our own language for the system, including game-like metaphors, diagrams and reams of Markdown intended to teach people and models how to think about it. The design gradually converged on a recognisable shape. Eventually we realised that we had wandered into the established territory of recompute engines and build systems.

That recognition made a lot of our private vocabulary disposable. The established terms were not merely tidier labels for ideas we already had. They connected the work to a mature body of thought about dependencies, caching, invalidation and reproducibility. We could stop stretching local metaphors over familiar territory and use language that had already been sharpened on many similar problems.

This matters even more now that much of the cognitive work is being done with language models. Every new conversation is a fresh joiner. You can give it pages of Markdown explaining private terms, historical compromises and the special meaning you have assigned to ordinary words, but all of that sits in the active context beside the problem itself.

A model can have a very large context window and still become less useful as you fill it. There may be enough room for all the material, but reading it is not free. The model has more relationships to keep straight, more local exceptions competing with its general knowledge and more chances to retrieve the wrong part of the story. Some of its apparent intelligence disappears into bookkeeping.

An established concept is compressed onboarding. Say "recompute engine" and a capable model can draw on material already present in its training. Say the name of an entirely private metaphor and every conversation needs another long introduction. I wrote before about [books as compressed prompts](/2026/01/02/books-as-compressed-prompts/); domain language works in much the same way. It lets us spend the context window on what is genuinely unusual about our problem rather than reconstructing ideas that already have names.

There are therefore two kinds of simplification here. Removing a speculative affordance reduces the obligations carried by the software. Finding the established name for the shape of a system reduces the explanation carried by the people and models working on it. Both leave more room for the thing we actually wanted to build.

The argument over metaphors was not a detour from implementation. Calling the feature a loan may prevent us from spreading it through the codebase, while recognising a recompute engine has already allowed us to throw away some of the conceptual scaffolding around the work. The right language can remove code before it is written and remove context before it has to be read, which is about as practical as a change of mind gets.

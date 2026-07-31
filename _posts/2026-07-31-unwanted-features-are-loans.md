---
layout: post
title: "Unwanted Features Are Loans"
date: 2026-07-31 09:00:00 +0000
tags: [software, engineering, ai, llm, language]
excerpt: "We nearly kept a feature because calling it insurance made it sound prudent."
---

This week at work we nearly talked ourselves into keeping a feature because it sounded like insurance.

We are building a design system that repeatedly reconstructs a model from a recipe. Between runs, a user can fix one of the generated values: this wall must remain 12mm thick, this component must stay at 50kW, and so on. We had implemented a mechanism that wrote each accepted constraint to disk immediately. If the process crashed after a user had made several decisions, those decisions would survive.

We spent rather a lot of time making this work properly: validating an edit before it touched disk, keeping memory and disk in agreement, rolling back cleanly when something failed, and proving that a fresh process restored the same constraints. By the end it felt hardened, which is an emotionally compelling reason not to remove something and not an economically relevant one.

The question came up because we were about to extend the constraint system across the rest of the codebase. Immediate persistence meant every new kind of edit would have to fit the same machinery. Some edits touch several things at once. Some setters have side effects. Supporting them safely would require ways to rehearse changes on isolated copies before committing them. An issue already existed solely because one class of setter did not fit the persistence contract.

What had looked like a small safety feature was beginning to decide the architecture around it.

I had been describing the feature as insurance. Pay a modest premium now and you are protected against the unpleasant day when the program crashes after someone has entered a lot of constraints. This made keeping it sound prudent. Removing it sounded reckless, or at least like penny-pinching.

But software affordances are not much like insurance. The cost of an insurance policy is legible and largely external to the thing insured. A just-in-case feature is closer to a loan, in the sense Addy Osmani meant when he wrote that [novelty is a loan you repay in outages, hiring, and cognitive overhead](/2026/01/05/innovation-tokens/). The implementation is only the principal. Interest arrives whenever somebody extends it, tests around it, explains it to a new colleague, keeps it compatible with a new abstraction or teaches an agent not to break it. A collection of these loans begins to determine what you are able to build, and the costs compound because the features interact with one another.

This is also why "we have already spent so much making it robust" is the wrong argument. That money is gone. The live question is whether the system should keep servicing the debt.

In our case, a crash might cost the user one or two recently entered constraints, followed by a rerun of the recipe and entering them again. Perhaps the real workflow involves twenty-five carefully considered decisions and this would be intolerable. We did not know. Nobody had complained, because nobody was using the system that way yet. We had borrowed against the future to protect a workflow that might never exist.

The correct threshold is not whether an affordance could be useful. Nearly everything could be useful. The question is whether it is important enough to become a permanent fact about the system, one that every relevant piece of future work must honour. Where the answer is unclear, it is often cheaper to omit it and follow the screams. A real user losing half an hour of work would be strong evidence. A room of engineers and language models imagining that it might happen is not the same thing.

What surprised me was how much changed when we replaced one metaphor with another. No code had changed and we had not discovered a new requirement. We simply stopped calling the feature insurance and started calling it a loan, at which point its future costs became difficult to ignore. This can sound like prattling about words while practical work waits, but a [mental model](/2026/01/24/thinking-out-loud/) determines which costs are visible, which questions seem natural and which parts of a design appear to belong together.

We had another version of this recently. For weeks we developed our own language for the system, including metaphors, diagrams and reams of Markdown intended to teach people and models how to think about it. The design gradually converged on a particular shape. Eventually we realised that the shape already had a well-developed language: it was a recompute engine, with much in common with build systems.

That recognition made a lot of our private vocabulary disposable. Dependency graphs, invalidation, fixed inputs, cached outputs and reproducible rebuilds were not merely neater labels for ideas we already had. They connected the project to a mature body of thought. We could stop bending local metaphors until they covered the design and instead use language that had been sharpened on many similar systems.

This matters even more when much of the cognitive work is being done with language models. Every new conversation is a fresh joiner. You can give it pages of Markdown explaining private terms, historical compromises and the special meaning of ordinary words, but all of that sits in the active context alongside the problem itself. Context windows may be large, but context is not free. The obvious cost is token count; the more important one is that, as the conversation fills with accumulated local explanation, the model has more to keep straight and less room to work cleanly on the thing in front of it.

An established concept is a compressed instruction. Say "recompute engine" and a capable model can draw on material already present in its training: build graphs, caching, dependency tracking, incremental work, invalidation and reproducibility. Say the name of an entirely private metaphor and every conversation requires another onboarding session. I wrote before about [books as compressed prompts](/2026/01/02/books-as-compressed-prompts/); domain language works the same way. It lets us use the context window for what is unusual about our problem rather than spending it reconstructing ideas that already have names.

There are therefore two kinds of simplification here. Removing a speculative affordance reduces the obligations carried by the software. Finding the established name for the system reduces the explanation carried by the people and models working on it. Both leave more room for the thing we actually wanted to build.

The argument over metaphors was not a detour from implementation. Calling the feature a loan may prevent us from spreading it through the codebase, while calling the system a recompute engine has already allowed us to throw away some of the conceptual scaffolding around it. The right language can remove code before it is written and remove context before it has to be read, which is about as practical as a change of mind gets.

---
layout: post
title: "Position Before Submission"
date: 2026-01-03 14:30:00 +0000
tags: [ai, bjj, expertise, workflow]
excerpt: "What ten years of Brazilian Jiu-Jitsu taught me about working with AI agents. It's all about where you expect things to be."
---

A good proportion of people starting BJJ will overexert in ways that aren't obvious to them at the time. I was absolutely one of these.

I remember when I first started training, I would often come away with my hands shaking from over-gripping. It doesn't really matter what your athletic background is - the nature of the sport defeats whatever fitness you bring. I'd done a bunch of triathlons, P Company, an Ironman, about ten marathons. I was still totally exhausted, again and again, for the first few weeks. It stays hard for the first few years.

About five years in, I reached the point where I could start experimenting with how much I could get away with relaxing. That's when things started to get easy. I don't think I could have done it earlier for the same benefit - you need the reps - but it would have been smart to try.

When you look higher up the belt grades, it's hard to ignore that some of the brown and black belts are actually pretty overweight. In large part, this is because they spend most of their time training with people who are just far less efficient when "rolling" (sparring). They barely need to exert themselves. The efficiency gap is that wide.

## Ten years in

I've now been training for nearly ten years. Lots of things that are natural to me are getting harder to explain to beginners. I actually suspect the best time to teach would have been about two years in - while you still have a grasp of what it's like to be new, empathy for ignorance, memory of scaling the same walls.

The feeling now isn't of being extremely knowledgeable, or of power. It just feels like things are roughly where you'd expect them to be.

The adage in the sport is *position before submission*. Before you attempt to submit your opponent, you want to get the most secure position you can - because then it's simply easy. You focus your energy on a form of body chess: taking their back, getting a top position that stops them escaping. Then the submission is almost incidental.

At the beginning, it was all about thinking through each minor movement you might need to make to build an advantage. Now it feels more like explaining why you're already doing something that seems obvious. Flow, not calculation. Things being where you expect them to be, rather than flights of inspiration.

It's exactly the same activity. But my brain - and probably my body - has moved to meet it where it is. There's latent knowledge I can't even articulate unless I'm forced to.

## The new game

So what does any of this have to do with AI?

Every conversation with a coding agent is a new joiner on your team. A new starter on the project in front of you.

This means there's a new form of debt. Not technical debt, not social debt. I've been trying to find the right term. "Comprehension debt" isn't quite right - that might be better reserved for humans losing track of what's going on when they over-delegate to models.

The closest I've got is *spending surprise*.

The idea: stay in the middle of the training distribution for the models. Only leave when there's absolutely a good reason, because it's expensive. When a model joins your project, it expects things to be where they typically are in the type of project you're writing.

Directory structures don't matter - except they do, if they hurt LLM performance. Because LLM performance is progress now.

Architectural decisions either boost the models or act as headwinds, depending on how surprising they are. You can waste minutes in every conversation explaining that actually the tests live over here, or that you have a library that does X so don't re-roll it yourself. `AGENTS.md` is a hack intended to ameliorate this. It has varying degrees of success and can't really be relied on - especially if we [scale the abstraction ladder](/2026/01/03/first-contact.html) and aren't at a low enough level to catch the models as they work.

It's all about bottlenecks now. Anticipating where they'll be in a few months, when everything else gets sanded down by scaling laws.

## Principle of least surprise

There used to be a part of me, on a subconscious level - maybe even an emotional level - that was tied to the testability and testedness of a project. I knew where the safe bits and unsafe bits were.

Now there's a part of me that's an advocate for the [principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment). I've typed "principle of least surprise" into my terminal while working with models more than almost anything else in the last few weeks. A quick grep through my Claude Code and Codex chat history shows 162 mentions in the last few months.

And to be honest, nothing has really changed. Surprising a human will slow them down too. If your project was staffed by contractors coming in temporarily to complete a feature, the marginal cost would go up for any surprises.

We're in that world now. It's different if you want to get things done fast.

This means you have to seem a bit weird to anyone who hasn't gotten the joke yet. It looks like over-fussing minor details. But it's the compound interest that makes you rich - small amounts, saved consistently. As soon as someone understands compound interest, they immediately understand saving. Maybe payday loans are a better analogy for the alternative.

For existing projects, it might even be worth worrying less about this week's Jira tickets and more about how to make the project more boring. Dan McKinley's [Choose Boring Technology](https://mcfunley.com/choose-boring-technology) made the case for conservative technology choices. But it's not just about technologies - it's about structures, use of libraries, directory layouts, naming conventions. All of it. The less surprising, the faster the models move.

## Back to BJJ

The connection is expertise. The feeling of things being just what you expect.

In BJJ, you spend years building up an intuition for where bodies go, what positions lead where, when to exert and when to relax. Eventually it stops feeling like calculation and starts feeling like the obvious thing.

Working with AI agents rewards the same instinct. Build projects where things are where you'd expect them to be. Position before submission. Make the architecture so obvious that when a model joins your project, it just... knows. No explanation needed. No minutes wasted.

Get the position right, and the submission is easy.

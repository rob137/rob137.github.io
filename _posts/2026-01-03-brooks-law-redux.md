---
layout: post
title: "Brooks' Law Redux"
date: 2026-01-03 18:00:00 +0000
tags: [ai, software, teams, bottlenecks]
excerpt: "The optimal number of engineers on a project is falling fast. It might be approaching zero."
---

I think I'm making a trivial point, but the implications feel big and not fully understood.

Each premise is simple. The inference between each premise is simple. But when you view them together, things are radically different.

## The premises

We're scaling compute in support of AI at a ridiculous rate. Gigawatt-plus clusters are coming online over the next year, with no end to investment in sight. We have thirty years of roughly 4x improvements every eighteen months behind us, and the expectation that they'll continue.

This is felt most intensely in software. Partly because reinforcement learning makes coding tasks particularly tractable. Partly because nerds are going to nerd - GitHub Copilot arrived early, software engineers fed in lots of training data, and here we are. Partly because the nature of software work involves bumping against reality until you figure it out, which made early LLM use as an unlocking function immediately valuable.

It's enough to say: software is where this is hitting first.

And it's not just happening inside the code editor. The whole cycle is speeding up - architectural decisions, technological trade-offs, grokking codebases, turning ideas into tickets, deploying prototypes to hit decision points faster. Time-to-done on each fragment of a task is asymptoting toward something very small.

## The bottleneck

There's a book called [The Goal](https://en.wikipedia.org/wiki/The_Goal_(novel)) about projects and bottlenecks. The insight: if everything is getting more efficient, eventually the things that *aren't* getting more efficient will stick out as the constraint.

The main invariant in AI engineering isn't the AI. The AI is changing at a ridiculous clip. The invariant is the people using the tools.

Communication between individuals on a team hasn't changed pace anywhere near as much as the rest of the work. You can ChatGPT your emails together a bit quicker now, sure. But ultimately it still comes down to a biological brain reading something, deciding what to do, processing it, taking lunch, losing track, coming back. All the things I do on a normal workday as a homo sapien.

The AI isn't bounded in this way.

Which means interpersonal communication, situational awareness, coordination - these are becoming the bottleneck. Not least because the decisions still sit with humans.

## The inversion

I'm noticing something hard now: whenever I take on a feature, the worst thing anyone could say is that someone else is going to work on it with me.

I used to love collaboration. Now it means enormous mental overhead I otherwise wouldn't have. The models are chopping through tasks at a crazy rate. It's the coordination with other engineers that becomes the focal point for slowdowns and surprises. The bump in the road.

Where collaboration used to be how you got things done faster, now it's often the opposite.

## Brooks' Law

Of course, it was never as simple as "collaboration gets things done faster." [Brooks' Law](https://en.wikipedia.org/wiki/Brooks%27s_law) - adding people to a late software project makes it later - has been known since 1975.

It's funny: in every job I've had, managers have only a fuzzy idea of what this means, while software engineers typically nod along. But there's a shadow side I've never reconciled. You could shout "Brooks' Law!" whenever an engineer is added to anything. When exactly does it kick in?

What I can see is that the threshold has come right down. It might be approaching zero.

The scary thing: the optimal number of engineers on a project might be less than one, in the broadest view of time.

## Jevons Paradox

For now, organisations will think in terms of cost gains on a per-project basis. But the usual adages about [Jevons Paradox](https://en.wikipedia.org/wiki/Jevons_paradox) do apply. Given the ability to do more with less, any company that can see a profit will simply want to do more. And if they can't mobilise, someone else will come along and eat their lunch.

I'm not worried about the socioeconomic implications of supposedly needing fewer workers on projects. The number of projects is dynamically influenced by the amount a person can get done. Whether something is worth starting determines whether you ever bother. There's survivor bias already, and that will only continue.

I'm not worried in that way.

## The exclamation mark

But when someone says they're bringing in people to help, I notice a [Metal Gear Solid exclamation mark](https://www.youtube.com/watch?v=2P5qbcRAXVk) popping up above my head.

The moment when I realise: now we have two problems.

Maybe the worrying thing, though, is this: the LLMs - while not conscious - might be meaningfully characterised as feeling the same way about me.

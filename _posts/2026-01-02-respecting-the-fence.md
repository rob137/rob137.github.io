---
layout: post
title: "Respecting the Fence"
date: 2026-01-02 14:00:00 +0000
tags: [ai, bureaucracy, llm, government, productivity]
---

A retired vicar asked me for help with some paperwork. What happened next made me rethink my entire relationship with bureaucracy.

I've always been temperamentally allergic to bureaucracy. Small systems, low friction, get out of the way - that's my instinct. Forms feel like obstacles. Processes feel like make-work. The word "bureaucracy" itself is almost universally pejorative.

And yet.

## Worn Smooth by Use

Here's the thing I've come to appreciate: a lot of bureaucratic processes exist for good reasons.

Unintended consequences multiply at scale. Edge cases that seem absurd turn out to protect real people from real harm. Governments are the embodiment of this wicked problem - you can't coordinate millions of people without process, and you can't have process without friction.

Chesterton's fence is the classic formulation: don't tear down a fence until you understand why it was built. The bureaucratic form you're frustrated by might be protecting something important. The checkbox that seems pointless might exist because someone, somewhere, got hurt when it wasn't there.

I still prefer the idea of minimal friction. But I've learned to hold that preference loosely. Some friction is scar tissue. Scar tissue exists for a reason.

## The Vicar's Problem

So: the vicar. A local parish church that does a lot of what is effectively social work - helping people in the community navigate complex systems. One parishioner needed to apply for support, which meant completing a dense government form backed by hundreds of lines of documentation about their circumstances.

This had become a bottleneck. The paperwork was genuinely onerous. Not because anyone designed it to be cruel, but because the system needs to protect against fraud, ensure resources go where they're needed, and satisfy various legal requirements. The friction was there for reasons.

The church team could help, but they're volunteers with limited time. The parishioner was overwhelmed. The form sat incomplete.

I'm a software engineer and father of three. I have no background in social care or benefits systems. I had about an hour to spare.

We got permission to use an LLM - being explicit about the privacy implications, making clear that we couldn't guarantee data wouldn't end up in training sets, letting the person decide if they were comfortable proceeding. They were.

Then I did something very simple. I put the documentation in a directory, pointed [Claude Code](https://docs.anthropic.com/en/docs/claude-code) at it, and said: "This is a well-known government form. Based on these materials, fill out sections X, Y, and Z with appropriate detail."

It worked.

The domain experts reviewed the output, found almost nothing substantive to change - a few style tweaks - and submitted. The application went through.

Total effort from me: maybe an hour. Total expertise in the domain: zero.

## Not Subverting the Process

Here's what I want to emphasize: we didn't circumvent anything. The form still got filled out. The requirements still got met. The system's checks and balances remained intact.

What changed was the friction.

The form exists to ensure the right information reaches the right people in the right format. That's legitimate. What's *not* legitimate - what's not actually serving anyone - is the hours of human anguish spent translating life circumstances into bureaucratic language.

The LLM handled the translation. The substance remained human.

This is what I mean by respecting the fence. We didn't tear it down. We didn't argue it shouldn't exist. We just... walked through it more quickly. The fence is still there, doing whatever the fence does. We just stopped being slowed down by it.

## Text Ingestion at Scale

In a previous life, I was an intelligence corps officer in the British Army. Running an intelligence cell is, at its core, a text ingestion and pattern matching problem. You're drowning in information. You're trying to synthesise it into something actionable. The bottleneck is never the information itself - it's the cognitive load of processing it.

But it wasn't just the primary work. It was the pastoral stuff too. Finding out how to fund an adventurous training trip for my section. Discovering what career opportunities might be lurking in the far corners of the defence intranet. Working out which obscure process applied to a given soldier's situation.

All of this was bureaucracy. All of it was legitimate - the military has good reasons for its processes. And all of it was friction that consumed time I could have spent on the actual mission.

I would have killed for an LLM back then.

## Climbing the Abstraction Ladder

Software engineers have been climbing an abstraction ladder for decades. Binary to assembly. Assembly to C. C to Python. Python to "just describe what you want and let the model write the code."

Each rung lets you think at a higher level. You stop worrying about register allocation and start worrying about system design. You stop worrying about memory management and start worrying about user needs.

It's not obvious to me that this ladder is restricted to code.

So much work is fundamentally bureaucratic: there's a process you need to follow, information you need to ingest, a format you need to output. You're translating between what you know and what the system requires. You're satisfying constraints that exist to protect something - even if you can't see what.

LLMs let you climb that ladder too. You stop worrying about form fields and start worrying about whether you actually have the right information. You stop translating and start thinking.

The substance remains. The friction evaporates.

## 2026

I think this is the year people realise the payoff isn't restricted to code.

Developers have been living in LLM-augmented workflows for a while now. We know what it feels like when the friction disappears. We've adjusted our intuitions about what's possible.

Everyone else is about to find out.

The vicar didn't need to become a benefits expert. The parishioner didn't need to learn bureaucratic language. I didn't need any domain knowledge at all. We just needed to describe the situation clearly and let the model handle the translation.

That pattern works for a *lot* of problems. Benefits forms. Insurance claims. Legal correspondence. Medical paperwork. Tax returns. Grant applications. Visa documentation.

All of these are text ingestion problems. All of them have friction that exists for legitimate reasons. And all of them are about to get dramatically easier - not by tearing down the fences, but by making it trivial to walk through them.

The processes remain. The protection remains. The anguish disappears.

That's the revolution. Not subverting bureaucracy. Respecting it - without being crushed by it.

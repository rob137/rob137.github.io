---
layout: post
title: "Thinking Out Loud"
date: 2026-01-24 11:00:00 +0000
tags: [ai, cognition]
excerpt: "Models don't remember their train of thought. They only remember what they've said out loud."
---

A friend at a local startup told me they've been playing 20 questions with reasoning models—but with the model as the answerer. They'd ask it to think of something, then pepper it with yes/no questions while reading its thinking traces.

In one round, the model picked "apple." The humans could see this in the trace. But partway through, the model got confused and started answering as though it had picked "pear." The humans knew it was wrong about its own secret. The model didn't—it couldn't see the trace showing what it had originally chosen.

---

We're well into the era of inference-time compute. The "reasoning traces" you see in ChatGPT, Claude, and the terminal-based tools are summaries of thinking tokens—output the model generates to work through a problem before giving you its final answer.

But here's the thing: those thinking tokens work exactly like regular output tokens. The model produces them one at a time, each token informed by everything that came before. When it's done thinking and starts writing the actual response, it can see what it "thought"—but only because those thoughts are now part of the text.

There's no separate scratchpad. No persistent internal state. The model's "train of thought" exists only to the extent that it's been written down.

A human playing 20 questions as the answerer remembers what they picked. Even without saying it out loud, they hold the answer in mind and check each response against it. The reasoning persists independently of whether it was spoken.

Models don't have this. They only remember what they've said out loud. The model that picked "apple" had no way to check its later answers against that choice—the thinking trace where it decided on "apple" was invisible to it by the time it started answering "pear." It had no privileged access to its own prior reasoning. Just the text of its responses.

---

Uncle Bob Martin [put it well](https://x.com/unclebobmartin/status/2014311028972994582) this week:

> Claude codes faster than I do, by a significant factor. Claude can hold more details in its "mind" than I can—again by a significant factor.
>
> But Claude cannot hold the big picture in its mind. It doesn't really even understand the concept of a big picture. Architecture is likely beyond its capacity.

He's right, but I'd frame it differently. It's not that Claude can't understand big pictures. It's that Claude can't *hold* anything. Every response starts from scratch, reconstructing context from the transcript. The "mind" that holds more details than Uncle Bob is an illusion created by the context window—a finite text buffer, not a persistent understanding.

This is why architecture is hard for models. Architecture requires holding invariants across a codebase while making local changes. It requires remembering *why* you structured something a certain way, not just *that* you did. Models can see the code, but they don't remember the reasoning that shaped it—unless that reasoning was written down somewhere they can read.

The 20 questions game revealed this starkly: the humans had better access to the model's "mind" than the model did. They could read the trace; the model couldn't. Its own prior reasoning was invisible to it.

When you understand this, a lot of model behavior makes more sense. The tendency to agree with corrections even when the original answer was right. The way extended conversations drift. The benefit of writing explicit reasoning into prompts rather than assuming the model will "figure it out."

They think out loud because that's the only way they think at all.

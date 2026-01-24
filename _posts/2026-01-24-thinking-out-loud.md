---
layout: post
title: "Thinking Out Loud"
date: 2026-01-24 11:00:00 +0000
tags: [ai, cognition]
excerpt: "Models don't remember their train of thought. They only remember what they've said out loud."
---

A friend at a local startup told me they've been playing 20 questions with reasoning models—reading the thinking traces as the model narrows in on its guess. Once they could tell it had basically figured out the answer, they lied. Told it the guess was wrong.

The model believed them. It abandoned the correct answer and kept searching.

---

We're well into the era of inference-time compute. The "reasoning traces" you see in ChatGPT, Claude, and the terminal-based tools are summaries of thinking tokens—output the model generates to work through a problem before giving you its final answer.

But here's the thing: those thinking tokens work exactly like regular output tokens. The model produces them one at a time, each token informed by everything that came before. When it's done thinking and starts writing the actual response, it can see what it "thought"—but only because those thoughts are now part of the text.

There's no separate scratchpad. No persistent internal state. The model's "train of thought" exists only to the extent that it's been written down.

A human playing 20 questions remembers their reasoning even if they don't say it out loud. They can get told they're wrong and think: *wait, that doesn't match what I worked out*. The reasoning persists independently of whether it was spoken.

Models don't have this. They only remember what they've said out loud. If the thinking tokens say "I'm confident the answer is apple," but the conversation history says "User told me apple was wrong," the model will trust the history. It has no privileged access to its own prior confidence—just the text.

---

Uncle Bob Martin [put it well](https://x.com/unclebobmartin/status/2014311028972994582) this week:

> Claude codes faster than I do, by a significant factor. Claude can hold more details in its "mind" than I can—again by a significant factor.
>
> But Claude cannot hold the big picture in its mind. It doesn't really even understand the concept of a big picture. Architecture is likely beyond its capacity.

He's right, but I'd frame it differently. It's not that Claude can't understand big pictures. It's that Claude can't *hold* anything. Every response starts from scratch, reconstructing context from the transcript. The "mind" that holds more details than Uncle Bob is an illusion created by the context window—a finite text buffer, not a persistent understanding.

This is why architecture is hard for models. Architecture requires holding invariants across a codebase while making local changes. It requires remembering *why* you structured something a certain way, not just *that* you did. Models can see the code, but they don't remember the reasoning that shaped it—unless that reasoning was written down somewhere they can read.

The startup's 20 questions trick worked because the model's "confidence" isn't confidence at all. It's just text. And text can be contradicted by newer text.

When you understand this, a lot of model behavior makes more sense. The tendency to agree with corrections even when the original answer was right. The way extended conversations drift. The benefit of writing explicit reasoning into prompts rather than assuming the model will "figure it out."

They think out loud because that's the only way they think at all.

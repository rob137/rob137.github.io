---
layout: post
title: "A New Proof Point"
date: 2026-01-06 10:00:00 +0000
tags: [ai, practices, engineering, testing]
excerpt: "Software's religious wars over best practices might finally get some data."
---

Software engineering has its religious wars. Inlining versus decomposition. [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) as one tome, [Carmack's email on inlining](http://number-none.com/blow/john_carmack_on_inlined_code.html) as scripture for another. [Continuous delivery](https://www.davefarley.net/). [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development). Pair programming in the [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck), pure Agile sense.

These debates are always framed in terms of productivity and robustness. But the feedback loops are slow. You only complete so many projects in a decade. So attitudes diverge. People pattern-match to their own experience and declare victory for whichever practices happened to correlate with their successes.

I suspect LLMs are going to force convergence.

## The race

When you're writing so much so fast, it becomes obvious whose race car is quickest. The human bits are becoming the bottleneck. Manual testing doesn't scale. Reacting to bugs is still largely a human domain. Suddenly robustness sticks out.

[Gergely Orosz](https://x.com/GergelyOrosz/status/2008272970041409579):

> "Most change that AI tools will bring for software engineers are likely to be making the practices that the best eng teams did until now, the baseline for those that want to stay competitive + move fast. Things like product-minded engineers, testing, o11y, CD etc."

[Simon Willison](https://x.com/simonw/status/2008298185962512763):

> "This seems like a good bet to me - coding agents make it no longer remotely excusable to skip out on quality engineering processes like good issue tracking, thorough QA, automated testing, up-to-date documentation, CI, deployment automation etc."

Simon put it more directly in [Your job is to deliver code you have proven to work](https://simonwillison.net/2025/Dec/18/code-proven-to-work/). The proving is still on you.

## 200-engineer practices at 3 engineers

[Patrick McKenzie](https://x.com/patio11/status/2008306035522449453):

> "There are a lot of 200 engineer practices you can now implement at 3 engineers and a lot of 12 engineer practices you can implement on day one just by mentioning them in a sentence or three."

He followed up with an example: "The only blessed way for writing code at this company is against Docker. All dependencies are installed only in Docker. Any Docker box can be shot in the head at any time and we don't lose more than minutes of work."

Then: "I thought I was insufficiently Cool Kid to ever get Docker running until I realized Claude is easily sufficiently Cool Kid and the entire spec for this behavior is the above tweet."

The cost of good practices just collapsed. The excuses are vanishing.

## Which practices?

The interesting question is which practices win. LLMs aren't humans. They might react differently to the same constraints. TDD? Tests before refactoring? Decomposition into small functions, or Carmack's argument that inlining can actually reduce bugs by making control flow visible?

We're about to find out. The sample size is no longer "however many projects you shipped in your career." It's "however many projects got shipped this quarter, globally, with AI assistance."

The religious wars might finally get some data.

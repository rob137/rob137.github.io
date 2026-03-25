---
layout: post
title: "Talking Spreadsheets"
date: 2026-03-25 12:00:00 +0000
tags: [ai, software, tools, interfaces]
excerpt: "We keep adding applications to LLMs. The thing that's actually happening is the reverse."
---

![Talking Spreadsheets](/assets/images/2026-03-25-the-talking-sheet.png)

I'm a software engineer. My days run on something close to Paul Graham's [maker's schedule](https://www.paulgraham.com/makersschedule.html): terminal, plain text files, long unbroken stretches. I avoid Outlook and Excel the way a cat avoids water. But I spend a lot of time talking to managers across the business, and over the past few weeks something has shifted. They're in a sugar rush. The cause is [Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel).

The feature list isn't the interesting part. What's interesting is that the more useful mental model has quietly shifted. This isn't an LLM that can reference a spreadsheet. It's a spreadsheet that can reason, update itself, search the web, and kick off actions. Intelligence added to Excel, not Excel added to an LLM.

That inversion matters. We're over three years past ChatGPT and most applications are still fundamentally static. Same flows, same expectations of users, same interfaces. The interesting frontier isn't chatbot intelligence. It's intelligence showing up inside the applications people already live in, doing work where the data already is.

---

This is happening at a larger scale too. [OpenClaw](https://github.com/openclaw/openclaw), an open-source personal AI agent you run on your own devices, went from zero to 250,000 GitHub stars in under four months. It surpassed React, which took a decade to get there.

![OpenClaw star history vs React and Linux](/assets/images/openclaw-stars.png)

OpenAI [hired the author](https://en.wikipedia.org/wiki/OpenClaw) and is now [merging ChatGPT, Codex, and their Atlas browser into a single desktop application](https://creati.ai/ai-news/2026-03-20/openai-desktop-superapp-chatgpt-codex-atlas-browser-merge/). Anthropic released [Dispatch](https://www.cnbc.com/2026/03/24/anthropic-claude-ai-agent-use-computer-finish-tasks.html), a continuous conversation that runs across your phone and your Mac, and Claude can now open apps, navigate browsers, and complete workflows on your computer while you're away from it. Both companies are converging on the same idea: a single application that is your point of contact for everything you'd use a computer for.

People are calling these "super apps", borrowing the term from WeChat and its descendants. But the old super apps bundled existing services into one place: payments, shopping, messaging. The new ones are different in kind. They bundle a frontier model with a thin harness wired to your operating system. The closest precedent in computing is probably Emacs, the old joke about an operating system in search of a good text editor. Emacs was a Lisp interpreter with an editor bolted on. The editor was the thin harness; the runtime was the point. Same shape here, wildly different capability.

---

My five-year-old can use a computer you talk to. She couldn't use a computer from the 1990s without serious coaching. The natural interface won, and the direction of travel is clear: intelligence goes into the tools, not the other way around. The chatbot era was a detour. The managers on my team figured this out before I did, because they never left Excel in the first place.

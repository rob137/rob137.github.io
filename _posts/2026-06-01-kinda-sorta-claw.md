---
layout: post
title: "Kinda-Sorta Claw"
date: 2026-06-01 09:00:00 +0000
tags: [ai, agents, github]
excerpt: "ChatGPT quietly became a coding agent. It's on a different billing rail."
---

ChatGPT asked me this week if I wanted it to create a GitHub issue, open a PR, push a commit, comment on a review. The chat interface, sitting in its own cloud-based sandbox, taking real actions on my repositories rather than just reading them like I'd assumed when the GitHub integration first shipped. It's a coding agent, just not labelled as one.

OpenAI [hired Peter Steinberger](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/) in February, the creator of [OpenClaw](https://github.com/openclaw/openclaw), to lead their next-generation personal AI agents. Whether the ChatGPT GitHub integration is a downstream consequence of that hire or just product teams independently converging on the same idea, I don't know. The result is the same.

---

Everyone working with coding agents right now is token-constrained. Codex burns through budget. Claude Code burns through budget. The hard ceiling on any given day is usually "I ran out of tokens", not "I ran out of ideas."

ChatGPT draws from a different pool, and a much more generous one. I can have 5.5 Pro review a pull request, leave inline comments, suggest refactors, the kind of work that would chew through Codex credits in minutes, and it barely registers against my ChatGPT allocation. Same models, just a different meter.

---

For the past few months I've been running a setup I'm fairly proud of: Termux on a phone, Tailscale to a Mac mini, tmux sessions, an AI coding harness wired into everything. Small sharp tools, Unix philosophy, the kind of thing that appeals to me on a deep level. It works. But there is overhead, and I've started noticing it.

The thing ChatGPT is becoming feels less like a collection of small tools and more like emacs: a single large platform that's mouldable enough to absorb whatever you throw at it. I've always been a small-tools person, but when the platform handles the compute, the audit trail, the sandbox, the permissions, and the billing in one place, the overhead of stitching your own version together starts to look like a cost rather than a virtue. Suddenly paying a bit more for a ChatGPT Pro subscription and letting it handle the plumbing feels more sensible than maintaining the bespoke rig, or at least worth trying for a month.

There's a security angle here too, though not the one people usually mean. I've never been able to install Claude Code or OpenClaw or any of the local claw setups. I'd get to the install screen and just stop. Not because I was worried about prompt injection or data exfiltration in the way the discourse usually frames it, but because running one of these things makes you personally responsible for an unbelievably complex risk surface, and if something goes wrong with a free tool you have no leverage at all. GitHub is different: the audit trail, the permissions model, the APIs are already institutionally understood. You're piggybacking on someone else's operating surface rather than inventing your own.

---

The question is whether OpenAI has noticed the economics of what they've built. There are two readings.

One: this is deliberate. Pull developers deeper into ChatGPT, make the Pro subscription indispensable, and create the kind of individual dependency that makes enterprise pricing easier to push later. Pro is pitched at users, not organisations, and there's something of the freemium sleeper cell about it: get the individual engineer hooked on their personal plan, wait for the company to follow them in asking about compliance and zero data retention.

Two: it's a blindspot. The team building ChatGPT's tool integrations added GitHub because GitHub is an obvious integration target, and nobody paused to notice they'd built a coding agent on a different billing rail. Product teams at big companies miss cross-cutting effects like this all the time.

Either way, the effect is the same: ChatGPT has quietly become the cheapest and most accessible coding agent available, without ever being positioned as one.

---

I've been calling it vibe delegating, which I think is closer to what's actually happening here than vibe coding. I don't care how the work gets done so long as it shows up as a PR I can review, in a trail I can inspect. The compute lives at OpenAI, the audit trail lives on GitHub, and the risk is distributed across institutions with reputations to protect and support contracts to honour. ChatGPT plus GitHub already does that, and it happened quietly enough that I nearly missed it.

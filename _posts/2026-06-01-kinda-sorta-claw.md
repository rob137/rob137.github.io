---
layout: post
title: "Kinda-Sorta Claw"
date: 2026-06-01 09:00:00 +0000
tags: [ai, agents, github]
excerpt: "The ChatGPT app quietly became a claw. It's on a different billing rail."
---

ChatGPT asked me this week if I wanted it to create a GitHub issue, open a PR, push a commit, comment on a review. The chat app, sitting in its own cloud-based sandbox, taking real actions on my repositories rather than just reading them. It's a coding agent, just not labelled as one, and even that label is too narrow for what it's becoming: a general-purpose computer use agent that happens to have developer tools wired in first.

OpenAI [hired Peter Steinberger](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/) in February, the creator of [OpenClaw](https://github.com/openclaw/openclaw), to lead their next-generation personal AI agents. Whether the ChatGPT GitHub integration is a downstream consequence of that hire or just product teams independently converging on the same idea, I don't know. The result is the same.

---

Everyone working with coding agents right now is token-constrained. Codex burns through budget, Claude Code burns through budget, and the hard ceiling on any given day is usually "I ran out of tokens", not "I ran out of ideas."

ChatGPT draws from a different pool, and a much more generous one. I can have 5.5 Pro review a pull request, leave inline comments, suggest refactors, the kind of work that would chew through Codex credits in minutes, and it barely registers against my ChatGPT allocation. Same models, just a different meter.

---

For the past few months I've been running a setup I'm fairly proud of: Termux on a phone, Tailscale to a Mac mini, tmux sessions, an AI coding harness wired into everything. Small sharp tools, Unix philosophy, the kind of thing that appeals to me on a deep level. It works. But there is overhead, and I've started noticing it.

The Codex desktop app now [does the same thing](https://openai.com/index/work-with-codex-from-anywhere/). It runs on your Mac or Windows machine, always on, and the ChatGPT app on your phone can reach it remotely. My Tailscale rig gave me exactly this: phone in pocket, real machine at home, agent running in the background. The difference is that OpenAI maintains the tunnel, the agent process, and the billing, and the credits come from an existing ChatGPT subscription rather than a separate Codex budget. Same architecture, organisational backing instead of duct tape.

The thing the ChatGPT app is becoming feels less like a collection of small tools and more like emacs: a single product surface mouldable enough to absorb whatever you throw at it. GitHub integration, remote machine access via Codex, a cloud sandbox for when you don't need your own hardware. I've always been a small-tools person, but when one app handles the compute, the audit trail, the sandbox, the permissions, and the billing, the overhead of stitching your own version together starts to look like a cost rather than a virtue.

There's a security angle here too, though not the one people usually mean. I've never been able to install Claude Code or OpenClaw or any of the local claw setups. I'd get to the install screen and just stop. Not because I was worried about prompt injection or data exfiltration in the way the discourse usually frames it, but because running one of these things makes you personally responsible for an unbelievably complex risk surface, and if something goes wrong with a free tool you have no leverage at all. The ChatGPT app is different: GitHub's audit trail and permissions model are already institutionally understood, Codex desktop runs under OpenAI's own process management, and you're piggybacking on existing operating surfaces rather than inventing your own.

---

The question is whether OpenAI has noticed the economics of what they've built. There are two readings.

One: this is deliberate. Pull developers deeper into one app, make the Pro subscription indispensable, and create the kind of individual dependency that makes enterprise pricing easier to push later. Pro is pitched at users, not organisations, and there's something of the freemium sleeper cell about it: get the individual engineer hooked on their personal plan, wait for the company to follow them in asking about compliance and zero data retention.

Two: it's a blindspot. The team building ChatGPT's tool integrations added GitHub because GitHub is an obvious integration target, added remote Codex because desktop apps want remote access, and nobody paused to notice they'd assembled a full claw on a different billing rail. Product teams at big companies miss cross-cutting effects like this all the time.

Either way, the effect is the same: the ChatGPT app has quietly become the cheapest and most accessible coding agent available, without ever being positioned as one. And since "coding agent" is really just "computer use agent" aimed at developers first, this is likely just the beginning of what that surface absorbs.

---

I've been calling it vibe delegating, which I think is closer to what's actually happening here than vibe coding. I don't care how the work gets done so long as it shows up as a PR I can review, in a trail I can inspect. The compute is at OpenAI, the audit trail is on GitHub, the tunnel to my machine runs through the Codex desktop app, and the risk is distributed across institutions with reputations to protect and support contracts to honour. One app as the single point of contact for all of it, and it happened quietly enough that I nearly missed it.

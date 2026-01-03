---
layout: post
title: "Too Comfortable"
date: 2026-01-03 07:00:00 +0000
tags: [ai, llm, coding, scaling, tools]
excerpt: "Terminal agents have been the stable pattern for a year now. If scaling laws hold, that stability should feel suspicious."
---

[Jeff Tang](https://x.com/jefftangx/status/2007230663553151281) captured something real under the satire:

> "oh you're still on Claude Code? we're orchestrating agents with Beads now. wait, Steve Yegge just shipped Gas Town, it's like Kubernetes for Coding Agents. just kidding, we put Ralph Wiggums in a for loop. we gave him a phone number and bank account and asked him to autonomously make a million dollars, so he setup a daycare center in Minneapolis
>
> we ssh'd into Ralph's sandbox from Termius with Tailscale and Tmux so i could code while pooping, but we hit our limit on our 10th claude code max plan. so we forked Droid's structured compaction, then stole Amp's hand-off, rewrote it in Rust, then rewrote it again in Zig in 150LOC
>
> but we needed a GUI for browser-use so we added opencode with playwrighter clicks, and reverse-engineered Claude Chrome over Christmas so it would work with remote browsers, and now it deterministically solves CAPTCHA from a TUI, so now Ralph is sending Hinge messages for me
>
> if you're not hyperengineering and burning 4 quadrillion tokens a microsecond for 92 peta-hours uninterrupted, you're cooked. 2026 is about to be wild."

The joke works because the churn is real. Every week brings a new framework, a new orchestration pattern, a new way to arrange the same underlying capabilities.

And yet: terminal-based agents have been the stable pattern for about a year now. Aider arrived, then Claude Code, and here we are - still typing into terminals, still watching diffs scroll by. The surface chaos obscures a surprisingly stable core.

That stability should feel suspicious.

## The numbers

[Huang's law](https://en.wikipedia.org/wiki/Huang's_law) observes that Nvidia GPU performance has more than tripled every two years since 2006 - faster than Moore's law. AI-relevant compute is [projected to grow](https://ai-2027.com/research/compute-forecast) at roughly 2.25x per year through 2027.

Call it a rough 4x every 18 months if you want a round number. That would mean 16x in three years.

[Leopold Aschenbrenner](https://www.dwarkesh.com/p/leopold-aschenbrenner) put it concretely: "GPT-2 was kind of like a preschooler. GPT-4 could write code and do hard math, like a smart high schooler." That's two years of scaling. Two more iterations at the same rate gets you somewhere else entirely.

[Ilya Sutskever](https://www.dwarkesh.com/p/ilya-sutskever-2) framed it differently on the same podcast: "2020 to 2025 was the age of scaling... scaling sucked out all the air in the room." The wave isn't done.

## The lurch

If capabilities continue to compound at anything like this rate, a year from now shouldn't look like today. The tools that feel cutting-edge now should feel quaint. The workflows we've settled into should be disrupted.

So why does terminal-agent coding feel like it's settled? Why does my current setup feel... comfortable?

Maybe it's the right abstraction and will persist. Maybe chat-plus-diff is genuinely the stable interface for human-AI collaboration on code.

Or maybe I've stopped lurching. Maybe I've let the daily churn exhaust me into accepting a local maximum.

The Jeff Tang tweet is funny because it's exhausting to contemplate. But the exhaustion might be the point. If you're not periodically questioning whether your entire workflow is already obsolete, you might be coasting on momentum from a year ago.

I don't know what the next shift looks like. But I'm suspicious of my own comfort.

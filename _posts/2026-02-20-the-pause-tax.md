---
layout: post
title: "The Pause Tax"
date: 2026-02-20 12:00:00 +0000
tags: [ai, software, workflow]
excerpt: "You are the bottleneck now."
---

I've used org-mode for years. One file per project, opened with a keybind, simple checkboxes. Plain text, tree structure, nothing fancy. Unreasonably effective.

What I only recently noticed: my to-do items have become prompts. All my work runs through coding agents now. When I add a task, I'm really staging a prompt. And because I use speech-to-text for everything, it's actually easier to braindump the full context at the moment I'm thinking about it than to write something terse. So my to-do items have gotten verbose - they're basically ready to fire.

Here's the embarrassing bit. For months I'd add follow-up tasks while an agent was working, planning to copy them into the chat later. Then I realised: the agent can just read the file. The manual step was completely redundant. It can read the org file, pull work from it, even update it as things complete.

So now that's the workflow. The org file is a living document. I tell the model to check it before completing any task, treat it as the running context for what we're doing. I dump thoughts, DMs, code fragments, political context - whatever's relevant - straight in as to-do items. The model pulls from it; I keep adding to it.

What surprised me is how fast this is.

I think it's because the pauses were costing more than I realised. In the old workflow - pass a task, wait for output, review, pass the next - the model would finish and wait for me. And I'd be "quickly" checking Teams, or reading a Slack thread, or answering an email. These felt momentary. They weren't. The aggregate drag on forward motion was enormous.

It's like an experiment I do with my phone sometimes. On weekends I switch it fully off between uses - not standby, off. Not a rule that I can't use it, just friction before I do. Two things happen: I basically stop using it, and I'm shocked how much time opens up. The minutes that feel marginal pass without you noticing. They add up fast.

Same thing here. In ordinary use the train stops entirely while I'm engaged elsewhere, and it doesn't feel like lost time because I'm busy. But the throughput cost is real.

The new workflow doesn't pause. I'm still watching everything, still reading output, still judging whether it's missing something. But the system doesn't block on my input between tasks. The model pulls the next item and keeps moving. My attention can drift to the broader picture - what we're trying to do, what trade-offs we haven't considered, what's coming next - while work continues underneath.

This only works because the models are good enough now. A year ago you needed tight coupling - sign off on nearly every function, because drift happened fast if you looked away. The sensible ratio was something like one approval per commit. Now I can batch. The models at this generation feel less like toddlers needing guardrails and more like high-agency juniors who are rough around the edges but keen to get things done. You want to give them context about why, not just what - because that feeds into their decisions.

Which means my job is shifting. Less time on commit-level concerns. More time on coordination, team-level failure modes, project-level risk. The models are reaching the point where they have grounds to challenge me on decisions, and the ratio of useful pushback is going up. That's a product of better taste - rising intelligence, RL on code, whatever's driving it - and I expect it to continue.

So the workflow is: living document, model pulls from it, human watches and steers but doesn't block. The pause tax disappears. Throughput goes up by more than you'd expect.

You are the bottleneck now. Might as well notice.

---
layout: post
title: "Image Problem"
date: 2026-03-11 10:00:00 +0000
tags: [tools, ai, workflow]
excerpt: "Terminals have two of them."
---

![Image Problem](/assets/images/2026-03-11-image-problem.png)

Terminals have two image problems.

The first is perception - they're foreboding, hiding possibilities behind memorized incantations rather than revealing them through buttons and dropdowns. If you know man pages exist you can figure things out, but it's not intuitive.

The second is literal: terminals can't display images. And that's starting to matter.

Steve Yegge, in his [talk with Gene Kim](https://www.youtube.com/watch?v=FtJObsATsh0): "If you're using an IDE starting on... I'll give you till January 1st. You're a bad engineer."

The argument makes sense. IDEs accumulated decades of cruft. AI coding agents don't need syntax highlighting, bracket matching, file trees - they need a codebase and a prompt. The terminal strips away everything else. Stage 5 in Yegge's framework: CLI, single agent. That's where serious work happens.

I've been there for a while with Claude Code and Codex CLI. It's good - composable, and I can SSH in from anywhere.

But something shifted. The VS Code extensions for these tools are now just UI shims on top of the same terminal agents, same engine underneath. And standalone apps like Codex Desktop exist too - GUIs that aren't IDEs, built specifically for agent workflows. Why would anyone use those instead of the terminal? Because of images.

When the agent takes a screenshot to verify something, GUI users see it inline. When it generates a diagram, they see it. When it shows you what it's looking at, they see it. In the terminal, I see a file path. Terminals render text - that's what they do, and there's no way around it. A TUI cannot show you a picture. As AI feedback loops tighten, as visual verification becomes part of how you work with agents, that gap matters more.

You could work around this. The harness could auto-open images in your OS when the agent wants to show you something - pop up a preview window. It's not hard to build. But it's still not the same as inline; your eyes leave the terminal, you context-switch, and the flow breaks, even if only briefly.

So maybe the trajectory isn't terminal forever. Strip away the IDE cruft, yes - get down to agent plus codebase plus prompt. But the surface you interact through might swing back toward GUI. Not the old IDE, but something leaner: a shell that can show you what the agent sees.

I'm not sure yet. The terminal workflow is good in other ways. But this limitation isn't going away.

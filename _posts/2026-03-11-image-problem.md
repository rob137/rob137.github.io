---
layout: post
title: "Image Problem"
date: 2026-03-11 10:00:00 +0000
tags: [tools, ai, workflow]
excerpt: "Terminals have two of them."
---

Terminals have two image problems.

The first is perception. They're foreboding. If you know that man pages exist, you can figure things out - but it's not intuitive the way a button or dropdown is. GUIs implicitly reveal possibilities. Terminals hide them behind memorized incantations.

The second is literal. Terminals can't display images. And that's starting to matter.

Steve Yegge, in his [talk with Gene Kim](https://www.youtube.com/watch?v=FtJObsATsh0): "If you're using an IDE starting on... I'll give you till January 1st. You're a bad engineer."

The argument makes sense. IDEs accumulated decades of cruft. AI coding agents don't need syntax highlighting, bracket matching, file trees. They need a codebase and a prompt. The terminal strips away everything else. Stage 5 in Yegge's framework: CLI, single agent. That's where serious work happens.

I've been there for a while. Claude Code, Codex CLI. It's good. Composable. I can SSH in from anywhere.

But something shifted. The VS Code extensions for these tools are now just UI shims on top of the same terminal agents. Same engine underneath, different surface. And standalone apps like Codex Desktop exist too - GUIs that aren't IDEs, built specifically for agent workflows.

Why would anyone use those instead of the terminal?

Images.

When the agent takes a screenshot to verify something, GUI users see it inline. When it generates a diagram, they see it. When it shows you what it's looking at, they see it.

I see a file path.

Terminals render text. That's what they do. There's no way around it. A TUI cannot show you a picture. And as AI feedback loops tighten - as visual verification becomes part of how you work with agents - that gap matters more.

You could fix this. The harness could auto-open images in your OS when the agent wants to show you something. Pop up a preview window. It's not hard to build. But it's still not the same as inline. Your eyes leave the terminal. You context-switch. The flow breaks, even if only briefly.

So maybe the trajectory isn't terminal forever. Strip away the IDE cruft, yes. Get down to agent plus codebase plus prompt. But the surface you interact through might swing back toward GUI - not the old IDE, but something leaner. A shell that can show you what the agent sees.

I'm not sure yet. The terminal workflow is good in other ways. But this is a limitation that isn't going away.

---
layout: post
title: "What I Don't Touch Anymore"
date: 2026-01-19 16:00:00 +0000
tags: [ai, workflow, automation]
excerpt: "The list of things I've stopped doing is more interesting than the tools I'm using."
---

> "A human being should be able to change a diaper, plan an invasion, butcher a hog, conn a ship, design a building, write a sonnet, balance accounts, build a wall, set a bone, comfort the dying, take orders, give orders, cooperate, act alone, solve equations, analyse a new problem, pitch manure, program a computer, cook a tasty meal, fight efficiently, die gallantly. Specialization is for insects."
>
> — Robert Heinlein, [*Time Enough for Love*](https://en.wikipedia.org/wiki/Time_Enough_for_Love)

> "Efficiency is for robots. Efficiency is for AI. Humans are about inefficiencies... Productivity is for robots."
>
> — Kevin Kelly, [*North Star Podcast*](https://perell.com/podcast/kevin-kelly-seeing-the-future/)

---

I still have a normal job with a normal manager who assigns me tickets. But my workflow has become science fiction.

The things I don't touch anymore aren't the things I was bad at. They're the things I was *good* at—upper fifth percentile, the skills I spent years developing, the ones that got me hired.

**Git.** I was fluent. Rebasing, cherry-picking, worktrees, reflog archaeology. Now I don't type git commands. Claude spins up Codex instances in separate worktrees, each making a single-commit PR for a ticket. The commands happen. I don't type them.

**Test harnesses.** I knew how to set these up well. Targeted test runs, sensible suite organisation, fast feedback loops. I've made them legible to LLMs now—makefile targets with comments explaining what each suite does. But I don't run them. Claude runs them, reports back, iterates if something fails.

**Language servers.** LSP was a lifeline—jump to definition, find references, the kind of code navigation that made large codebases tractable. I have company-mode and lsp-mode set up in Emacs. They've been broken for weeks. I genuinely don't know if they work anymore, because I've stopped using them. Grepping through a codebase with an LLM that understands what it's looking at turns out to be just as fast.

**Breaking down tasks.** This was the skill. Taking a vague requirement and decomposing it into the right units of work. Now the orchestrator pulls tickets from Azure DevOps, reads the comments, cross-references merged PRs, checks dates of merges against comments—forensics on the semantic history of the thing. Then it farms the work out to agents, and I review what comes back.

**Even manual testing.** First-line manual testing is done by the bots now. I say "check that the dropdown works" and watch Claude navigate the browser, click through the UI, take screenshots. I still need to get the fuzzy feeling myself by checking—but this is [becoming the bottleneck](/2026/01/06/trial-by-foom/).

What's left? Not just approval. The job is more intellectually demanding now, not less. I'm constantly articulating ambiguity—social uncertainties, gaps in my own understanding, the possible ways things might be, the intentions behind test setups or architectural fudges that wouldn't be obvious to a new joiner. I have to frame all of this in a way that lets smart models move fast.

I sit in front of three terminal panes. One is orchestrating. One is testing. One is waiting for direction. The locomotion is theirs. The context-shaping is mine.

Here's the uncomfortable part: the skills you invested years in, the ones you were proud of—those are exactly the skills worth automating. Your strengths get eaten first, not your weaknesses. That's the economics.

Heinlein celebrated the generalist human against insect-like specialisation. Kelly defended inefficiency as the human domain. Both were drawing lines between us and machines. Those lines are dissolving. The generalist skills and the efficient execution are both being absorbed now.

The tail wags the dog. I got a good microphone because I use speech-to-text constantly. Then I started caring about audio quality. Then I started recording thoughts while agents work. But it's not a weird cubbyhole—there's a flywheel here. Thinking out loud to an intelligent listener develops ideas. Developing ideas makes you faster with the tools. Being faster with the tools lets you get faster at other things quicker. Those feed back into tool usage. Getting stuff done feels good, so you're drawn toward whatever compounds. It's a self-improving loop I'm not fully conscious of. Every experiment lands you somewhere better.

It's getting pretty weird now.

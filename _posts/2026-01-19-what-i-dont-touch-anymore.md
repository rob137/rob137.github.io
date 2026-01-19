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

**Breaking down tasks.** This was the skill. Taking a vague requirement and decomposing it into the right units of work. Now the orchestrator pulls tickets from Azure DevOps, farms them out to agents, and I review what comes back.

**Even manual testing.** I say "check that the dropdown works" and watch Claude navigate the browser, click through the UI, take screenshots. I'm still reviewing, still deciding. But the mechanical testing has shifted.

What's left? Judgment. Review. The decision to ship.

I sit in front of three terminal panes. One is orchestrating. One is testing. One is waiting for my approval. My job has become saying "yes" or "not yet" while agents do the locomotion.

Here's the uncomfortable part: the skills that are easiest to automate are the ones worth automating—the ones that took years to develop, the ones you were proud of. The valuable skills are the ones the models learn first. That's the economics. That's the point.

Heinlein celebrated the generalist human against insect-like specialisation. Kelly defended inefficiency as the human domain. Both were drawing lines between us and machines. Those lines are dissolving. The generalist skills and the efficient execution are both being absorbed now.

The tail wags the dog. I got a good microphone because I use speech-to-text constantly. Then I started caring about audio quality. Then I started recording thoughts while agents work. The tools reshape the user.

It's getting pretty weird now.

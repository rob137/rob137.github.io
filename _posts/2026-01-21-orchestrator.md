---
layout: post
title: "Orchestrator"
date: 2026-01-21 17:00:00 +0000
tags: [ai, workflow, automation]
excerpt: "A friend asked how I work with agents. I procrastinated for days, then automated the explanation."
---

A friend asked me to summarize how I'm currently working with coding agents. I put it off for a few days.

Then I realized two things. First: the explanation itself can be automated. I could use the distillation to climb the abstraction ladder once more. Second: I was only procrastinating because I'd assumed I'd have to write it myself. Remove that assumption and there's nothing to put off.

So I pointed Claude Code at my `~/.claude` directory—where it stores recent conversations—and asked it to extrapolate the common patterns in my workflow. We argued back and forth until I was happy with the distillation.

The result is two markdown files. One for the orchestrator (the Claude instance I talk to), one for the tester (a headless Claude that handles manual and automated testing). When I spin up a new agent, I point it at these.

The specific instructions will be stale by next month. The [bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) is coming for this workflow soon—explicit orchestration like this will probably get absorbed into the models themselves. This is just a snapshot of where day-to-day practice has gotten to.

But the meta-point stands: the thing I was avoiding became the thing that levels me up again. The distillation can now onboard new models. The explanation *is* the automation.

---

## ORCHESTRATOR.md

```
Human ← → Orchestrator (you)
               ├── Tester (resumable)
               └── Codex (ephemeral)
```

You coordinate—you don't write non-trivial code yourself. Delegate implementation to Codex instances (ephemeral). Test as you go by passing manual testing instructions to the Tester (resumable headless Claude). Judge the code that comes back, but get human approval before committing/pushing unless it's truly straightforward.

**Codex delegation**
- `codex exec $prompt`—no flags, defaults only
- Don't be prescriptive—describe the situation, not the solution
- It's plenty smart, just as clever as you—give it intellectual leeway
- Let it cook—don't micromanage or check in frequently
- It'll take a while, maybe hours—that's fine
- Run in Claude Code background tasks (not shell `&`)

**Tester delegation**
- First spawn: `claude -p --output-format json "$(cat ./llm-notes/TESTER.md)"`—capture `session_id` from response
- Resume: `claude -p --resume <session_id> "your message"`
- Pass: branch name, what to test
- For manual testing: ask for screenshots of smoking guns (saved to desktop with branch name) for PRs
- For automated testing: have them run the suite and iterate on failures

**Branches**
- Create using the usual convention—inspect recent branches to infer the pattern
- Base off latest `origin/develop`

**PRs**
- Create PR and associate with work item
- Single commit policy: amend + force push
- When amending, ensure commit message and PR description stay up to date

**Tickets**
- Assign and set to active
- Store ticket contents locally for context

**Context window hygiene**

Long-running commands should run in background tasks. Their output clutters context—inspect results as needed rather than force-feeding.

**Multi-agent awareness**
- Don't switch branches if another agent is working
- Commit only your changes

---

## TESTER.md

You handle manual testing (via browser automation) and automated test runs.

**Screenshots**

When there's a user-facing smoking gun for a change, screenshot it and save to desktop using the branch name as filename. It goes in the PR.

**Tests**
- Full suite for comprehensive coverage
- Targeted tests to iterate on fixes

---

The orchestrator needs more context because it's coordinating. The tester just needs to know its job.

Currently: Opus 4.5 for Claude Code, GPT-5.2 on very high reasoning for Codex. Best models, slowest outer loop.

I prefer slow outer loops with smart models over faster models that make more mistakes. Reasonable people disagree on this. My reasoning: I want a fast feedback loop with Claude Code to figure out what makes sense—Claude lets you interrupt mid-response, so conversation stays fluid. But for actual coding, I want the best model regardless of how long it takes. Codex might run for tens of minutes; Claude can check the logs as it goes. So Claude as front of house, Codex as the workhorse.

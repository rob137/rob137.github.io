---
layout: post
title: "Token Communism"
date: 2026-05-29 10:00:00 +0000
tags: [ai, teams, management]
excerpt: "Amazon's AI leaderboard is Goodhart's Law in corporate form. But the real lesson is about who gets the budget."
---

[Amazon built an internal leaderboard](https://x.com/GergelyOrosz/status/2060276380638576750) tracking employees' AI tool usage. Workers started gaming it immediately, running pointless tasks, padding their scores. The company shut it down this week. Anthropic apparently considered something similar two months ago, debated it internally, and killed the idea before it shipped. One company thought ahead, the other ran the experiment and learned the hard way.

This is Goodhart's Law playing out in real time: when a measure becomes a target, it ceases to be a good measure. Token consumption is trivially easy to inflate. Run a heater 24/7 and you top the electricity leaderboard. It tells you nothing about whether anyone's getting warmer.

The more interesting point is underneath the Goodhart problem.

---

Most software engineers in large companies aren't in value-producing roles. They're maintaining systems, attending meetings, working on internal tools that don't touch revenue. This isn't a criticism - big organisations need infrastructure, need coordination, need people keeping the lights on. But it means most engineers are cost centres, not profit centres.

A cost centre can only squeeze a bit. You can make it cheaper, but there's a floor. A profit centre can scale to infinity.

The military understands this. Compare the spend over ten years on a special forces operator versus a line infantry soldier - even at Tier 2, training costs differ by more than an order of magnitude. You pour resources into the people who deliver disproportionate impact.

Token leaderboards assume the opposite. They assume the right answer is communism - everyone gets the same ration, and we'll measure whether they're using it. But that gets it backwards. The question isn't "how do we make sure everyone's consuming tokens?" It's "who do we want to give the budget to, because they'll actually do something with it?"

---

AI agents make software engineers more productive. They finish tasks faster, they can tackle more ambitious work. But that only matters if the work being finished is valuable. If someone is maintaining a system nobody should be maintaining, or attending meetings that exist because process has calcified around them, then making them faster just makes them more expensive.

A lot of studious, hard-working people are actually cost centres. They're doing the job they were hired to do. It's not their fault the job shouldn't exist. But when you give everyone equal token budgets and rank them on consumption, you're not identifying your best performers. You're identifying who's best at looking busy.

The companies that figure this out will do something different. They'll identify who actually generates value and give them asymmetric resources.

Everyone else gets whatever's left after that, which might be a lot or might be nothing. The egalitarian version feels fairer, but the asymmetric version is how you survive.

---

[Vik Khyat put it bluntly](https://x.com/vikhyatk/status/2059771148540527028): agents make SWEs more productive, but most SWEs in large companies aren't in value-producing roles. If your job is a cost centre and you become twice as fast at it, you've halved the time until someone notices the job shouldn't exist.

Token communism is one way organisations can avoid confronting this. Give everyone the same budget, track it on a leaderboard, pretend the problem is adoption. The Amazon experiment demonstrated why that doesn't work.

I've [written before](/2026/01/28/three-fingers/) about how managers reveal outdated mental models through small gestures, like setting two-day deadlines for two-hour work. The leaderboard is the same tell at organisational scale. Leadership that thinks the right metric is "are people using AI?" has revealed, without knowing it, that they haven't understood what AI changes. The question was never adoption, it was allocation.

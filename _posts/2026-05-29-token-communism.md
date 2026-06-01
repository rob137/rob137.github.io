---
layout: post
title: "Token Communism"
date: 2026-05-29 10:00:00 +0000
tags: [ai, teams, management]
excerpt: "Amazon's AI leaderboard is Goodhart's Law in corporate form. But the deeper problem is political: who gets the budget, who loses it, and whether the org can move fast enough to decide."
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

The trouble is that knowing this and acting on it are different problems entirely.

A lot of cost-centre teams didn't start as cost centres. They were expanded because politics demanded it - somebody needed headcount to justify a budget, a reorg left the group orphaned, they're the residue of a negotiation between VPs three years ago. The individuals are often perfectly diligent. They're doing the job they were hired to do. It's just that the job probably shouldn't exist, and nobody with the authority to say so has the political incentive to.

As [Vik Khyat put it](https://x.com/vikhyatk/status/2059771148540527028): if your job is a cost centre and you become twice as fast at it, you've halved the time until someone notices the job shouldn't exist. Give everyone an equal token budget and you're not just failing to identify value - you're subsidising political inertia, making it more comfortable to leave broken structures in place.

---

I'm now lead developer at a startup, and one of the things I found myself immediately aligned with the founders on was team size. I [wrote about Brooks' Law](/2026/01/03/brooks-law-redux/) in January - communication overhead becomes the dominant bottleneck when everything else speeds up. Amdahl's Law in practice: the non-parallelisable fraction swallows your gains.

But team size isn't just a communication problem. It's a political one. Big teams create constituencies, and constituencies resist change. Dismantling a team means someone loses budget, someone loses status, and nobody wants to be the one who lets go of the diligent people who were doing exactly what they were asked to do.

---

Meanwhile, AI doesn't wait for the org chart to catch up. Yann Dubois at OpenAI [described it well recently](https://zeno.fm/podcast/the-mad-podcast-with-matt-turck/episodes/openais-yann-dubois-why-ai-progress-suddenly-feels-real/): inside labs, improvement is continuous - incremental gains in reliability, post-training, evals. Outside, it feels like a step-change, because usefulness crosses a threshold and suddenly the tool works on real problems, not just demos.

Different domains hit that threshold at different times. Software engineers were shouting about it from November to February. More recently it's mathematicians and theoretical physicists - OpenAI's work on the Erdos unit-distance problem got serious mathematicians' attention in a way that benchmarks never did. Each crossing sends a fresh wave of pressure through the organisations that depend on that domain, and they don't stop coming.

---

This is what makes the allocation question so pointed right now. The organisations that most need to decide who gets the budget and who loses it are exactly the ones least equipped to decide, because those decisions are political, and politics is the ultimate non-parallelisable bottleneck. Token communism is what you get when the political clock runs slower than the technical one, and AI is outpacing organisational OODA loops by a widening margin.

The question was never adoption. It was allocation. But allocation requires political will, and a leaderboard is so much easier to ship.

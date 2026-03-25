---
layout: post
title: "BDD With the Excuses Removed"
date: 2026-03-25 09:00:00 +0000
tags: [ai, software, bdd, specifications, sdlc]
excerpt: "Spec-driven development isn't new. It's what happens when the old discipline finally pays off."
---

![BDD With the Excuses Removed](/assets/images/2026-03-25-bdd-with-the-excuses-removed.png)

In January 2023, Andrej Karpathy posted what became one of the most-shared tweets in tech:

![Karpathy tweet: The hottest new programming language is English](/assets/images/karpathy-english-tweet.png)

It got 10.8 million views, and he followed up with a [thread](https://x.com/karpathy/status/1617979122625712128) cataloguing what he meant: voice assistants programmed in English, LLMs as backends taking state as JSON and modifying it based on natural language, system prompts constructing entire identities. His summary: "GPT is a general-purpose computer, reconfigurable at run-time to run natural language programs." And this new paradigm had the potential to expand the number of programmers to 1.5 billion people.

That was over three years ago. He was right. But what's interesting now is watching the formalisation catch up with the intuition.

---

A recent paper on arxiv, [Spec-Driven Development](https://arxiv.org/html/2602.00180), gives a thorough treatment of what SDD looks like in practice. It's a good paper, and a prescient one. The author got there before a lot of businesses did. His framing:

> The quality of specifications directly determines the quality of everything that follows. Good specs share several characteristics: they are behavior-focused, describing what happens rather than how; they are testable, with each requirement being verifiable; they are unambiguous, meaning different readers reach the same interpretation; and they are complete enough to cover essential cases without over-specifying.

Behavior-focused. Testable. Unambiguous. Complete enough without over-specifying. If you've spent any time with [Behavior-Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development), this is just BDD's definition, restated for an AI audience.

Dan North [introduced BDD](https://dannorth.net/introducing-bdd/) as an evolution of TDD, itself building on Eric Evans' [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design). Martin Fowler wrote about the same ideas via [Given-When-Then](https://martinfowler.com/bliki/GivenWhenThen.html). Dave Farley has spent years [arguing](https://www.youtube.com/watch?v=gXh0iUt4TXA) that BDD is about collaboration and specification, not about Cucumber syntax. None of this is obscure, and none of it is recent.

The SDD paper's author knows it too. He spends serious time elsewhere on Cucumber and other executable spec tools, and he cites Bryan Finster directly: ["SDD is not a revolution… it's just BDD with branding."](https://bdfinst.medium.com/5-minute-devops-spec-driven-development-isnt-new-3a5c552efc95) Finster's piece is worth reading in full. His framing is sharper: "Tests describe behavior. Behavior drives code. Code is the implementation detail." And his closing line: "AI amplifies your discipline or your dysfunction. Your choice." The paper acknowledges all of this and still softens the framing. I think that's a misstep.

---

The boundaries between DDD, BDD, and SDD are less interesting than the direction of travel. All three are the same conviction at different levels of ambition: if you get the language right, the implementation follows.

DDD said: model the domain in the code. The language *is* the design.

BDD said: specify behavior in domain language. The spec *is* the test.

SDD says: hand domain-language specs to an agent. The spec *is* the code.

Each one pushes "think carefully about the domain up front" one step further down the pipeline. SDD is what you get when you combine DDD's ubiquitous language with BDD's executable specs and give them to something that can actually write the implementation. The idea hasn't changed. It's just that "the implementation follows" used to be aspirational and is now literal.

---

I'm ambivalent about this, though.

SDD forces carefulness up front. It gives you a legible banner in corporate environments for practices you probably should have been following anyway, rather than racing toward arbitrary deadlines. When the spec is the thing the machine reads, writing a good spec stops being overhead and starts being the work. Anything that gets teams spending more time thinking about what they actually want and what the words they're using actually mean in a bounded context is good.

But look at who's pushing SDD loudest. It tends to be architects at large organisations where a neat, VP-legible picture matters. The rough-and-ready, bottom-up end of the AI-tools world — Karpathy, Simon Willison, swyx — haven't picked up spec-driven development as a named practice at all. They're just building, with tight feedback loops and direct control over what the model sees. Tools that formalise SDD, like Amazon's Kiro, introduce an intermediary layer between you and the model. When you run a `/specify` command, text gets added to the context window that you don't control and can't see. If you're already comfortable with LLMs, that's noise. If you're not, you're learning two things at once: how the model works and how the tool works, with an opaque layer between them. A tight grip on what's in the context window is the difference between knowing what you're doing and watching something happen on your screen.

Spec rot is the other problem. Markdown specs are loosely coupled to the code, but they're also loosely coupled to the conversations that produced them. In most teams, the canonical document is what people actually said in the meeting. Tickets are a lossy shadow of that. A spec file in a repo or a Confluence page is another degree of indirection further out. Someone has to remember to update it, and it doesn't take much drift before people stop trusting it. I've seen this happen on projects. The specs exist, they're just wrong enough that nobody checks them any more. If people reliably forget to update the spec, that's not a discipline problem, it's a [Don't Make Me Think](https://en.wikipedia.org/wiki/Don%27t_Make_Me_Think) design problem. Executable specs adjust for it. Markdown specs legislate against it. BDD understood this, which is why it pushed for specs that *run*. SDD inherits the same vulnerability when its specs are just markdown files that an agent reads rather than tests that fail.

And whether you think carefully before writing code is one choice, but whether you route that thinking through a particular tool's pipeline is another. You can have BDD's discipline without surrendering visibility into what the agent is actually being told. A one-line config change doesn't need a spec. A greenfield service probably does. If you watch the desire lines, you see people reaching for the simplest approach that can work, and matching ceremony to task size is something they do intuitively when you let them.

---

I keep coming back to the Trojan horse, though.

Most teams don't do BDD. They know they should. [Farley](https://www.youtube.com/@ContinuousDelivery), [Humble](https://continuousdelivery.com/), [Evans](https://www.domainlanguage.com/), [Spolsky](https://www.joelonsoftware.com/) — decades of smart people arguing that careful upfront thinking pays off. The industry nodded politely and kept sprinting toward the next arbitrary deadline. The friction was always the excuse. Writing specs took time. Maintaining them took more. The ROI was real but distant, and distant ROI loses to deadline pressure every single time.

SDD collapses the distance. The spec is no longer documentation you maintain alongside the code. It's the input that produces the code. The ROI is immediate. And if a tool like Kiro gets people writing behavioral specifications who otherwise wouldn't have written them at all, that's a net win even if the tool itself is eventually superseded.

My suspicion is that the bitter lesson is coming for the contrivance. Heavy intermediary tooling will get steamrolled as models get smarter and context windows get longer. But the bitter lesson is *not* coming for clarity of intent. Thinking carefully about what you want, in precise language, before asking a machine to build it. That part sticks.

SDD might be transitional technology pointing at a permanent practice. If the scaffolding falls away and the discipline remains, it will have done its job.

BDD with the excuses removed. Even if it takes a detour to get there.

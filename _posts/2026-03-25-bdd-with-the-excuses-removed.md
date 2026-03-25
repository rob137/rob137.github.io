---
layout: post
title: "BDD With the Excuses Removed"
date: 2026-03-25 09:00:00 +0000
tags: [ai, software, bdd, specifications]
excerpt: "Spec-driven development isn't new. It's what happens when the old discipline finally pays off."
---

![BDD With the Excuses Removed](/assets/images/2026-03-25-bdd-with-the-excuses-removed.png)

In January 2023, Andrej Karpathy posted what became one of the most-shared tweets in tech:

![Karpathy tweet: The hottest new programming language is English](/assets/images/karpathy-english-tweet.png)

10.8 million views. He followed up with a [thread](https://x.com/karpathy/status/1617979122625712128) cataloguing what he meant: voice assistants programmed in English, LLMs as backends taking state as JSON and modifying it based on natural language, system prompts constructing entire identities. His summary: "GPT is a general-purpose computer, reconfigurable at run-time to run natural language programs." And this new paradigm had the potential to expand the number of programmers to 1.5 billion people.

That was over three years ago. He was right. But what's interesting now is watching the formalisation catch up with the intuition.

---

A recent paper on arxiv, [Spec-Driven Development](https://arxiv.org/html/2602.00180), gives a thorough treatment of what SDD looks like in practice. It's a good paper and a prescient one. The author got there before a lot of businesses did. His framing:

> The quality of specifications directly determines the quality of everything that follows. Good specs share several characteristics: they are behavior-focused, describing what happens rather than how; they are testable, with each requirement being verifiable; they are unambiguous, meaning different readers reach the same interpretation; and they are complete enough to cover essential cases without over-specifying.

Read that again. Behavior-focused. Testable. Unambiguous. Complete enough without over-specifying. If you've spent any time with [Behavior-Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development), this is not new. This is BDD's definition, restated for an AI audience.

The paper goes further:

> In greenfield projects, developers become architects who design systems through specifications rather than code. They focus on requirements elicitation, constraint definition, and acceptance criteria — the "what" rather than the "how."

Again: this is BDD. And BDD was itself building on [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) before it. The lineage is clear. The author knows it too — elsewhere in the paper he spends serious time on Cucumber and other executable specification tools. He's not ignorant of the history. He just softens the framing.

I think the softening is a misstep, even if a diplomatic one.

---

The boundaries between DDD, BDD, and SDD are less interesting than the direction of travel. All three are the same conviction at different levels of ambition: if you get the language right, the implementation follows.

DDD said: model the domain in the code. The language *is* the design.

BDD said: specify behavior in domain language. The spec *is* the test.

SDD says: hand domain-language specs to an agent. The spec *is* the code.

Each one pushes "think carefully about the domain up front" one step further down the pipeline. SDD is what you get when you combine DDD's ubiquitous language with BDD's executable specs and give them to something that can actually write the implementation.

What changed isn't the idea. What changed is that "the implementation follows" used to be aspirational and is now literal. An agent can take a well-written spec and produce working code. The decades-old argument that careful domain modelling pays off — always true, but hard to prove when humans still had to manually bridge spec to code — is now trivially demonstrable.

---

This matters practically, not just intellectually. SDD forces carefulness up front. It gives you a legible banner in corporate environments for the practices you probably should have been following anyway, rather than just racing toward arbitrary deadlines. When the spec is the thing the machine reads, writing a good spec stops being overhead and starts being the work.

And in brownfield projects, the paper's point about encoding existing behavior as specifications before making changes is genuinely useful. The spec becomes the bridge between old and new implementations. That's not a new idea either — characterisation tests have been around for years — but AI makes the payoff immediate enough that people will actually do it.

The friction was always the excuse. Writing specs took time. Maintaining them took more. The ROI was real but distant, and distant ROI loses to deadline pressure every single time. AI collapses the distance. The spec is no longer documentation you maintain alongside the code. It's the input that produces the code. The ROI is immediate.

BDD with the excuses removed.

---

Karpathy saw this coming when he said English was the hottest new programming language. He was pointing at the same convergence from the other direction: natural language as a programming interface, specifications as programs. The SDD paper fills in the engineering detail. Between them, the picture is clear.

These aren't three competing methodologies. They're one idea that kept getting dismissed as too expensive, until AI made the cost argument disappear.

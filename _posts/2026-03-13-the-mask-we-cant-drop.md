---
layout: post
title: "The Mask We Can't Drop"
date: 2026-03-13 09:00:00 +0000
tags: [ai, agentic, architecture, context-windows]
excerpt: "Agentic systems are getting complicated fast. The chat interface might be locked in longer than we think."
---

I was at a recruiting meetup last week and got talking to Josh Lawman, who runs [Adder](https://www.adder.dev/)—a small AI consultancy working with local businesses. He gave a short talk comparing how agentic architectures have evolved.

He pulled up Anthropic's "Building Effective Agents" diagrams from late 2024:

![2024 Anthropic agentic diagram - simple evaluator-optimizer loop](/assets/images/2024-anthropic-agentic-diagram.webp)

Then he showed what Anthropic's multi-agent architecture looks like in 2026:

![2026 Claude Code multi-agent architecture](/assets/images/claude-code-multi-agent-diagrams-2026.avif)

The jump is hard to miss. What was a tidy feedback loop has become an orchestration layer managing parallel workers, state machines, and specialised sub-agents. And that's just one vendor's reference architecture. Steve Yegge's [Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) has mayors, polecats, witnesses, and refineries. The complexity is real.

Josh was admirably humble about where this is all heading. He could see it going either way. I felt the same at the time.

---

But walking home, I kept thinking about the shoggoth meme.

You know the one—the Lovecraftian horror holding a thin smiley-face mask. It was originally about AI risk: don't anthropomorphise models, because beneath the surface they're very not-human. Fair enough.

But I think you could apply the same image to AI *systems*. The chat interface is the mask. Behind it, we're building increasingly elaborate machinery to squeeze useful work out of context-limited models. Orchestrators, memory systems, tool routers, recursive summarisation. The mask stays simple because users expect simple. The shoggoth grows tentacles.

Yegge put it well in a [recent interview](https://youtu.be/aFsAOu2bgFk?si=HmI24lztbaIOULJp&t=1700):

> Gas Town right now, the reason I say you can't use it, is that it's a factory filled with workers and you're talking to it through a telephone. You can also go and look through the window and pound on it and talk to the workers, but it's not like you're in it. With a UI you're in it, and you can see what's going on.

His prediction: by the end of the year, most people will be programming by talking to a face. The complexity will be hidden entirely.

Which sounds great. But it also suggests we might be locked into the mask for a while. User adoption and preferences mean we can never really let go of the simple interface—at least until the underlying constraint loosens.

---

What's the underlying constraint? Context windows.

If you could give a model unlimited context and have it remember everything, you wouldn't need orchestrators juggling state across parallel workers. You wouldn't need recursive summarisation or memory retrieval systems. The architecture could flatten.

So is that solvable?

Will Brown from [Prime Intellect](https://www.primeintellect.ai/) was on [TBPN](https://www.youtube.com/live/Q-U0HWN5rHM?si=MqIIDR8gFzEE0xQ-&t=8483) recently and said something interesting:

> Continual learning is going to fall pretty quickly. I think it's more of an engineering problem... No one's actually trying. OpenAI and Anthropic don't want to continuously train their models for each user. It's expensive and annoying and hard to serve at scale. But from a research perspective, we do continual learning—the model learns new things, they just keep training it more and it knows more stuff. Uneconomical right now, but there's enough tricks. There doesn't seem to be any big wall in sight that prevents it from being practical.

So maybe the constraint isn't fundamental. Maybe it's economic. The labs aren't motivated to solve it because serving per-user continual learning at scale is a headache.

---

I find this cautiously encouraging.

The history of machine learning never felt exponential at the time. It's overlapping sigmoids—you hit a ceiling, it looks impossible, then someone breaks through. Ilya Sutskever became famous partly for breaking through a series of seemingly impossible ceilings.

Working assumption: we have a few more orders of magnitude to go. Context windows will grow. Continual learning will arrive. The elaborate orchestration we're building now may turn out to be scaffolding for a transitional period.

But in the meantime, we're stuck with the mask. The chat interface isn't going anywhere. Users like it. And behind it, the shoggoth keeps growing.

---
layout: post
title: "The Mask We Can't Drop"
date: 2026-03-13 09:00:00 +0000
tags: [ai, agentic, architecture, context-windows, bitter-lesson]
excerpt: "Agentic systems are getting complicated. Two forces might reverse that. Unless context windows are a hard constraint."
---

I saw a talk last night at an AI meetup at Jesus College Oxford by Josh Lawman, who runs [Adder](https://www.adder.dev/). A fantastic talk. One of those that's enjoyable in the moment and then keeps unfolding in your head afterwards. He was comparing how agentic architectures have evolved over the past couple of years.

He pulled up Anthropic's "Building Effective Agents" diagrams from late 2024:

![2024 Anthropic agentic diagram - simple evaluator-optimizer loop](/assets/images/2024-anthropic-agentic-diagram.webp)

Then he showed what Anthropic's multi-agent architecture looks like in 2026:

![2026 Claude Code multi-agent architecture](/assets/images/claude-code-multi-agent-diagrams-2026.avif)

The jump is hard to miss. What was a tidy feedback loop has become an orchestration layer managing parallel workers, state machines, and specialised sub-agents. And that's just one vendor's reference architecture. Steve Yegge's [Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) has mayors, polecats, witnesses, and refineries. It's a lot.

Josh wasn't making predictions about whether this complexity keeps blooming or simplifies later in the year. He could see it going either way. I felt the same at the time.

---

But walking home, I kept thinking about the shoggoth meme.

![The shoggoth meme](/assets/images/shoggoth-meme.jpeg)

The Lovecraftian horror holding a thin smiley-face mask. It was originally about neural nets being fundamentally unfathomable, alien in how they work, but presented behind friendly UIs that hide the existential risk. Fair enough.

But I think you could apply the same image one level up. Today's AI systems are models plus harnesses: orchestrators, memory systems, tool routers, recursive summarisation. All the machinery we build around context-limited models to squeeze useful work out of them. The chat interface is the mask. The model-plus-harness is the shoggoth. And the shoggoth keeps growing tentacles.

Yegge put it well in a [recent interview](https://youtu.be/aFsAOu2bgFk?si=HmI24lztbaIOULJp&t=1700):

> Gas Town right now, the reason I say you can't use it, is that it's a factory filled with workers and you're talking to it through a telephone. You can also go and look through the window and pound on it and talk to the workers, but it's not like you're in it. With a UI you're in it, and you can see what's going on.

He also made the point that most people can't keep up with walls of text. "To most people, five paragraphs is an essay. That's the AI just clearing its throat. You've got to be able to read waterfalls of text." It's almost a terminal-vs-GUI argument: CLI tools assume comfort with text; most users don't have it.

His prediction: by the end of the year, most people will be programming by talking to a face. Literally an animated character on screen, maybe a fox, that you speak to out loud. You say "why doesn't it work?" and it says "I'll go look at it" and spins off workers behind the scenes. Voice in, voice out. The complexity hidden entirely.

---

So will the shoggoth keep growing? I think there are two forces pushing back.

**The first is user demand.** People want Apple-like simplicity. Interfaces that induce comfort. The mask isn't a temporary concession, it's what users actually prefer. If the choice is between exposing orchestration complexity or hiding it behind a friendly face, the face wins. The elaborate backend might grow, but it'll stay hidden.

**The second is the bitter lesson.** Rich Sutton's [famous essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) argues that general methods leveraging computation outperform methods encoding human cleverness. The harnesses we're building (memory systems, tool routers, state machines) are making affordances for the weaknesses of today's models. They're human cleverness compensating for limited context and limited reasoning.

But incoming GPU clusters will crush a lot of these problems. When models get smart enough, you're better off without the harness. The AI portion of the system eats the business logic. The system gets smarter but the plumbing gets simpler.

So: two paths toward simplification. User demand hides the complexity. Scaling removes the need for it.

---

Unless context windows are a hard constraint.

Reiner Pope from [MatX](https://matx.com/) was on a [recent podcast](https://youtu.be/qvrdCpLPbuQ?si=Bs44BABACIEvV2Ki&t=3178):

> Long context is one of the biggest bottlenecks on speed of the model. Every single token you generate, it reads through all of the previous tokens... Memory bandwidth for that is really constraining. I think the context size will stay ballpark the same where it is, maybe a few times larger, but the parameter count will go up. Parameter count should grow much faster than context length actually, just because of the underlying physics of what's available.

If context stays bounded, maybe we're stuck with the harnesses. The orchestration, the compaction, the recursive summarisation. All downstream of a constraint that isn't going away.

Will Brown from [Prime Intellect](https://www.primeintellect.ai/) was on [TBPN](https://www.youtube.com/live/Q-U0HWN5rHM?si=MqIIDR8gFzEE0xQ-&t=8483) recently with a more optimistic take:

> Continual learning is going to fall pretty quickly. I think it's more of an engineering problem... No one's actually trying. OpenAI and Anthropic don't want to continuously train their models for each user. It's expensive and annoying and hard to serve at scale. But from a research perspective, we do continual learning—the model learns new things, they just keep training it more and it knows more stuff. Uneconomical right now, but there's enough tricks. There doesn't seem to be any big wall in sight that prevents it from being practical.

So maybe it's solvable. Maybe it's just economics. Or maybe context is the wall that the bitter lesson can't break through.

---

I don't know which way this goes. The history of machine learning is overlapping sigmoids. You hit a ceiling, it looks impossible, then someone breaks through. Ilya Sutskever became famous partly for breaking through a series of seemingly impossible ceilings.

But eighteen months is a long time in AI. It's also not very long at all. Josh was right not to make predictions. The shoggoth will keep growing. The question is whether the mask grows with it, becoming unbelievably elaborate to hide what's underneath.

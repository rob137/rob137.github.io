---
layout: post
title: "The Bottleneck Moved"
date: 2026-01-27 14:30:00 +0000
tags: [ai, workflows, llm]
excerpt: "Execution got cheap. The scarce resource is now exploration and taste."
---

I've been running Claude Code overnight. Not babysitting it—actually leaving. Tasking it with moderately complicated work in a codebase: coding, iterating on tests, doing things with the build. A sequence of steps. Then disappearing until morning.

It works. Not perfectly, but well enough that the failure modes are predictable and nudgeable. The model crashes in ways I can anticipate given the nature of the codebase. I check in, course-correct, leave again.

The writing workflow has shades of this. I record thoughts into audio files on dog walks, share them over Tailscale, and Claude Code transcribes and drafts. If I'm caught by a flash of inspiration at the gym, I don't need to find time later. I just talk. The recording replaces the podcast I would have listened to anyway.

These workflows resemble each other but they're actually quite different. The coding one maps to something familiar: tech lead with a remote team. The writing one doesn't map to anything I can name. It's not dictation. It's not editing. It's closer to thinking out loud with a transcriptionist who also happens to be a competent ghostwriter—but that's a stretch too.

This is the thing I keep noticing: *nameless workflows*. The space of possible workflows just got much wider than the space of things we can point at and say "that's a known job."

---

Here's what I think is happening. The bottleneck moved.

It used to be execution. "Can I build this?" was the hard question. You had an idea, and the constraint was whether you could actually make it real—or find someone who could, and afford them, and communicate well enough that they'd build what you meant.

Now the hard question is "What should I even build?" Execution is covered, at least the first 30%. You still have to attend to things. But you're not writing 80% of the code anymore. Your 20% input is making sure things align with your intent as they go along.

The bottleneck is now exploration. Hunches. Taste. The feeling of being onto something.

---

And here's the strange part: those hunches are becoming self-fulfilling.

Not in the hyperstition sense, where you believe something and unwittingly make it happen through that belief. More like a self-fulfilling *lead*. You're onto something, it's investigative, you're chasing it down. That very feeling is now a trigger to approach a frontier model.

You describe the workflow you wish existed. The model takes on an almost concierge quality—it knows the established options, the common patterns, at least as of its training data. Hardware doesn't move that fast, so usually that's fine. It gives you the workflow. You ask for something you can hand to another agent. It does that too. You're left with a human-specific list of instructions to set things up on your phone.

You can complete it over a coffee.

I wanted a button to start recording, a button to stop, and a pipeline that shares the file and triggers transcription. Two button presses, everything else behind the scenes. Twenty minutes later I had it working via Tasker on Android.

The hunch became real because I could describe it and the model could implement it. No forums, no research, no weekends lost to yak-shaving. Just a need, a conversation, and then the solution—before I even had a name for what I was building.

---

People talk about model overhang. The idea that capabilities are ahead of deployment, that we haven't yet figured out how to use what we already have.

I think there's a *human overhang* too. Most people haven't updated their priors on what's possible. They're running 2024 mental models on 2026 capabilities. There are workflows that simply didn't make sense six months ago which you can set up trivially now—since the last big round of releases.

The space of these workflows is enormous. And almost completely unexplored.

We're in an odd period where your bespoke workflow works before it gets absorbed into a proprietary harness. The bitter lesson is coming for all this stitching and glue. The things we're composing to let models work will become either capabilities of the models themselves or features of official tooling.

But right now? Your hunches are pretty much ready to go if you can describe them to a frontier model. No harness required.

The question used to be "Can I build this?" Now it's "Do I have the taste to know what's worth building?"

The bottleneck moved. Most people haven't noticed yet.

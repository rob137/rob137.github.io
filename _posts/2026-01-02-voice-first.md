---
layout: post
title: "Voice First"
date: 2026-01-02 08:00:00 +0000
tags: [ai, voice, llm, productivity, sdlc]
---

Last night I became an audio engineer.

I don't have any training in audio engineering. I've never taken a course, read a book, or spent time learning the fundamentals. And yet by the end of the evening I was discussing preamps, gain staging, and noise floors. More importantly, I was *doing* something about them.

Here's the thing: I'm not even the kind of person you'd expect to become an audio engineer. I've watched product reviews on YouTube when choosing headphones, and I always felt slightly out of place - like the professional audio engineers speaking weren't quite my tribe, intellectually. I find what they have to say genuinely interesting, but I don't see myself in them right away. It wasn't a world I would have given myself permission to enter. There's always opportunity cost. I'm always too busy for important things, let alone something tangential.

And yet here I was, diving into their domain quite happily. Because I wasn't trying to learn audio engineering. I was trying to record bedtime stories for my daughter.

## The Setup

I've assembled a simple voice-first toolkit:

- **[Zoom H2 Essential](https://zoomcorp.com/en/us/handheld-recorders/handheld-recorders/h2essential/)** - A portable recorder that doubles as a dictaphone for meetings. The beauty is it's unobtrusive. People don't tense up when you're not pointing a phone at them or asking them to install an app.
- **[Samson Q2U](https://samsontech.com/samson/products/microphones/usb-microphones/q2u/)** on a boom arm - Plugged straight into my laptop via USB for desk work. Solid audio quality without fuss.
- **[SuperWhisper](https://superwhisper.com/)** with Parakeet - For real-time speech-to-text on my Mac.

I've been using the H2 for everything. Recording piano practice. Reading stories to my kids. Testing how well speech-to-text handles a chaotic living room with three small children talking over each other.

## Just-in-Time Software Engineering

Here's the thing that feels genuinely revolutionary to me: I have no background as an audio engineer, but last night I found myself doing audio engineering.

I wanted to record bedtime stories for my daughter Joan to put on [Yoto](https://yotoplay.com/) cards. I fired up [Audacity](https://www.audacityteam.org/), recorded a few stories, and then realized the audio quality wasn't quite right. Too much background noise. Levels were inconsistent. I didn't know the first thing about fixing this.

So I asked Claude.

Not in a "give me a tutorial" way. In an open, exploratory, almost conversational way. I described what I was trying to achieve. I asked what was possible. The model guided me through noise reduction techniques, explained what decibels actually mean in this context, suggested specific Audacity effects, and helped me understand the tradeoffs between different compression settings.

I was channeling the AI toward the art of the possible - but I didn't know what that was until I started talking.

This is what I mean by **just-in-time software engineering**. Instead of spending hours learning audio engineering fundamentals before doing anything, I learned exactly what I needed, exactly when I needed it, in the context of a real task I cared about.

## Just-in-Time Code

But it goes further than learning. [Claude Code](https://docs.anthropic.com/en/docs/claude-code) wasn't just teaching me - it was writing disposable code on the fly to solve my problems.

When I asked about the audio files, it generated [ffmpeg](https://ffmpeg.org/) commands to convert formats, normalize levels, strip silence. When I wanted to transcribe recordings, it wrote shell scripts to batch-process files through [Whisper](https://github.com/openai/whisper). None of this code was meant to last. It was JIT code: just-in-time, use-once, throw-away.

This changes the economics of tooling in a profound way.

I have Audacity installed. I could learn to use it. But why would I? The payoff for learning a GUI application is that you can then do things with it. But if an LLM can generate the equivalent CLI commands instantly, the activation energy for the "professional" tool becomes a liability rather than an asset.

The capabilities were always there. ffmpeg has been able to do audio processing for decades. The bottleneck was never the tools; it was the friction of learning arcane command-line syntax, remembering flags, debugging errors. That friction made GUI applications worthwhile despite their limitations.

An LLM middle layer collapses that friction. Suddenly the full power of CLI tools is accessible to anyone who can describe what they want. The GUI becomes a detour rather than a shortcut.

I think a lot of software is about to become obsolete. Not because it stops working, but because the activation energy it was designed to lower is no longer the bottleneck.

## A Transcript from Last Night

To make this concrete, here's what actually happened. I plugged in my H2, which had recordings from the afternoon, me reading stories to my kids while testing the recorder's speech-to-text potential.

I asked Claude Code to transcribe the recordings. It discovered I didn't have Whisper installed, so it installed `whisper-cpp` via Homebrew, downloaded the medium model, and started transcribing. Here's a snippet of what came back:

```
[00:00:00.000 --> 00:00:07.000]   I'll just hit record on the device because
   I want to see how well the microphone works in a busy room.

[00:01:00.000 --> 00:01:07.000]   The key thing is I'm not recording a podcast -
   I just want it to be natural enough that I can do speech to text.
```

And then later, reading to the kids:

```
[00:02:51.000 --> 00:02:54.000]   So this book is called The Three Wishes.

[00:03:03.000 --> 00:03:06.000]   Lambert, Hilda and Ross were sat in front of the television.

[00:05:55.000 --> 00:05:57.000]   I'd like a great big banana to munch on while we decide,
   said Lambert.

[00:06:05.000 --> 00:06:10.000]   Suddenly, the biggest banana you've ever seen
   appeared on the table.
```

The transcription picked up everything - the story, the kids interrupting, my wife asking about whether Edie was drawing on the doors, the whole domestic chaos. In a 15-minute recording. In under a minute of processing time on an M4 Max.

## The Meta-Layer

Here's what strikes me: I'm writing this blog post by talking to Claude Code via SSH from my phone, over [Tailscale](https://tailscale.com/), while not sitting at my laptop. I'm dictating. The model is turning my rambling speech into structured prose, finding the relevant conversation history from last night, and assembling it into something coherent.

The workflow is:

1. **Talk** - Stream of consciousness, exploratory, hemispheric
2. **Let the model structure** - It finds the thread, organizes the thoughts
3. **Iterate** - Refine through more conversation

This is different from typing. When I type, I self-edit as I go. I constrain my thinking to fit the pace of my fingers. When I talk, I think out loud. The AI handles the mess.

## What This Means for Software Development

I think we're at the beginning of something significant. In my day job at [Volaris Group](https://volarisgroup.com/), I'm on a skunkworks team exploring how LLMs might reshape the software development lifecycle, and this is the kind of thing we talk about. (We're hiring, by the way. If this resonates, reach out.) The traditional SDLC assumes developers work primarily through keyboards and IDEs. But voice-first interaction with AI changes the economics of communication:

- **Meetings become data** - A recorded meeting isn't just minutes anymore. It's raw material for an AI to extract action items, summarize decisions, identify risks.
- **Documentation happens automatically** - Explain what you're building out loud, and you've written the design doc.
- **Pair programming becomes conversation** - "Let's think through this auth flow" turns into actual code, tests, and documentation.
- **Domain expertise becomes accessible** - I'm not an audio engineer, but I can do audio engineering when I need to.

## The Trick Is Being Open

The thing that makes this work is approaching the AI with genuine curiosity rather than narrow queries. I didn't ask "how do I reduce noise in Audacity." I said "I'm trying to record bedtime stories for my daughter to put on Yoto cards, and the quality isn't quite right. What can I do?"

That openness - that willingness to let the model help you discover what's even possible - is what unlocks the real value. You don't need to know the right question. You just need to know what you're trying to achieve.

And then you talk.

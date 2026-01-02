---
layout: post
title: "Voice-First: The Future of Talking to Machines"
date: 2026-01-02
tags: [ai, voice, llm, productivity, sdlc]
---

I'm a software engineer at Volaris Group, working on a skunkworks team exploring how AI and large language models might reshape the software development lifecycle, product features, and working practices. But this post isn't about enterprise strategy. It's about something I've become deeply convinced of through personal experimentation: **speech as input is the future**, and you can already get enormous productivity benefits by doubling down on it.

## The Setup

I've assembled a simple voice-first toolkit:

- **Zoom H2 Essential** - A portable recorder I expensed as a dictaphone for meetings. The beauty is it's unobtrusive. People don't tense up when you're not pointing a phone at them or asking them to install an app.
- **Samson Q2U** on a boom arm - Plugged straight into my laptop via USB for desk work. Solid audio quality without fuss.
- **SuperWhisper** with Parakeet - For real-time speech-to-text on my Mac.

The H2 was ostensibly for work meetings, but I've been using it for everything. Recording piano practice. Reading stories to my kids. Testing how well speech-to-text handles a chaotic living room with three small children talking over each other.

## Just-in-Time Software Engineering

Here's the thing that feels genuinely revolutionary to me: I have no background as an audio engineer, but last night I found myself doing audio engineering.

I wanted to record bedtime stories for my daughter Joan to put on Yoto cards. I fired up Audacity, recorded a few stories, and then realized the audio quality wasn't quite right. Too much background noise. Levels were inconsistent. I didn't know the first thing about fixing this.

So I asked Claude.

Not in a "give me a tutorial" way. In an open, exploratory, almost conversational way. I described what I was trying to achieve. I asked what was possible. The model guided me through noise reduction techniques, explained what decibels actually mean in this context, suggested specific Audacity effects, and helped me understand the tradeoffs between different compression settings.

I was channeling the AI toward the art of the possible - but I didn't know what that was until I started talking.

This is what I mean by **just-in-time software engineering**. Instead of spending hours learning audio engineering fundamentals before doing anything, I learned exactly what I needed, exactly when I needed it, in the context of a real task I cared about.

## A Transcript from Last Night

To make this concrete, here's what actually happened. I plugged in my H2, which had recordings from the afternoon - me reading stories to my kids while testing the recorder's speech-to-text potential.

I asked Claude Code to transcribe the recordings. It discovered I didn't have Whisper installed, so it installed `whisper-cpp` via Homebrew, downloaded the medium model, and started transcribing. Here's a snippet of what came back:

```
[00:00:00.000 --> 00:00:07.000]   I'll just hit record on the device because
   I want to see how well the microphone works in a busy room.

[00:00:25.000 --> 00:00:33.000]   Basically I've realised that with my camera lessons
   I can probably expense a recorder with a line in on it.

[00:01:00.000 --> 00:01:07.000]   And the key thing is because I'm not like recording a podcast,
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

Here's what strikes me: I'm writing this blog post by talking to Claude Code via SSH from my phone, over Tailscale, while not sitting at my laptop. I'm dictating. The model is turning my rambling speech into structured prose, finding the relevant conversation history from last night, and assembling it into something coherent.

The workflow is:

1. **Talk** - Stream of consciousness, exploratory, hemispheric
2. **Let the model structure** - It finds the thread, organizes the thoughts
3. **Iterate** - Refine through more conversation

This is different from typing. When I type, I self-edit as I go. I constrain my thinking to fit the pace of my fingers. When I talk, I think out loud. The AI handles the mess.

## What This Means for Software Development

I think we're at the beginning of something significant. The traditional SDLC assumes developers work primarily through keyboards and IDEs. But voice-first interaction with AI changes the economics of communication:

- **Meetings become data** - A recorded meeting isn't just minutes anymore. It's raw material for an AI to extract action items, summarize decisions, identify risks.
- **Documentation happens automatically** - Explain what you're building out loud, and you've written the design doc.
- **Pair programming becomes conversation** - "Let's think through this auth flow" turns into actual code, tests, and documentation.
- **Domain expertise becomes accessible** - I'm not an audio engineer, but I can do audio engineering when I need to.

## The Trick Is Being Open

The thing that makes this work is approaching the AI with genuine curiosity rather than narrow queries. I didn't ask "how do I reduce noise in Audacity." I said "I'm trying to record bedtime stories for my daughter to put on Yoto cards, and the quality isn't quite right. What can I do?"

That openness - that willingness to let the model help you discover what's even possible - is what unlocks the real value. You don't need to know the right question. You just need to know what you're trying to achieve.

And then you talk.

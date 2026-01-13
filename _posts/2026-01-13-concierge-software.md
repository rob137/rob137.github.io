---
layout: post
title: "Concierge Software"
date: 2026-01-13 09:30:00 +0000
tags: [ai, llm, vibe-coding]
excerpt: "It was easier to conjure bespoke software than to find something that fit."
---

I'm dictating this into a microphone. Speech to text. That's how I'm writing the article.

I've been recording things using a Zoom H2 Essential - a field recorder that makes it easy to get good audio quality for dictation. It lets me detether from my laptop when thinking - moving around is often conducive to getting good thoughts out. Good for group settings too, when recording multiple people. My default workflow has been: plug it into my laptop, fire up a coding harness, tell it the device is attached and I want the files moved and transcribed. It pulls up whisper-cpp or whatever. I get the text. Done.

But I realised I'd never actually listened to any of these recordings. Partly a UX thing - not easy to just pull them open and browse.

Linus Torvalds has been [experimenting with vibe coding](https://github.com/torvalds/AudioNoise). I'd already been doing it myself, but seeing it prompted a realisation: there are pain points I take for granted sitting right in front of me. The real question I need to keep asking myself is whether AI could just solve them.

## Five Minutes

I vibe coded a dashboard. Device detection, import, transcription, playback, metadata. The features I actually wanted.

It took less than five minutes of effort. Not elapsed time - I'd check in while doing other things, try the UI, tell it what I wanted different, and go back to what I was doing. Concierge software. Background task.

The key thing isn't that it was doable, or easy, or cheap, or possible. (Though it was all these things.)

It was *easier than finding existing software*.

## The Alternative

Think about what finding software normally involves. Google. Compare competing options. Click download. Move the DMG. Open it. Sign up to something. Disable the settings you don't want. Realise you're an edge case of a much broader feature suite. Figure out which corner of the UI to constrain yourself to.

All those questions were gone. The only features that existed were the ones I wanted.

That's the shift. Not "I can build it" but "building it is the path of least resistance."

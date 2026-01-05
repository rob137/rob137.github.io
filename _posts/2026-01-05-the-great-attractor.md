---
layout: post
title: "The Great Attractor"
date: 2026-01-05 14:00:00 +0000
tags: [ai, tools, convergence]
excerpt: "Certain general-purpose devices attract all functionality. The phone ate my flashlight. Now the terminal is eating everything else."
---

A friend put me onto flashlight enthusiasts. There's a [whole subreddit](https://www.reddit.com/r/flashlight/) of people slightly obsessed with finding the right torch - and it turns out the fringes of this hobby contain some beautifully designed products.

I've written before about over-obsessing on purchasing decisions. This was one of them. Before I knew it, I'd spent a few days sucked into the topic and ended up buying a [Noctigon KR1](https://intl-outdoor.com/noctigon-kr1.html) - a pocket thrower made by Hank Wang, who runs his shop as something between a side hustle and a calling. The design is lovely. It runs [Anduril](https://github.com/ToyKeeper/anduril), an open source firmware that lets you configure every aspect of how the light behaves. Someone saw a gap and filled it, beautifully.

That winter I used it on every dog walk. It felt just right for the purpose - a tool that did one thing well.

## Two winters later

It's dark in winter in the UK. That's when you reach for your torch. But somewhere along the way, I lost the habit. Now I just use my phone.

The same thing happened with my laptop. It sits ready to go, and I almost never open it outside of work. Online shopping, browsing, reading - all on the phone now. This blog is an example: I'm dictating posts on my phone using speech-to-text, SSHing into my laptop to commit them.

Certain general-purpose devices attract all functionality. The phone is a great attractor - good enough at everything, always in your pocket. The specialist tool, however beautiful, gets left in the drawer.

## AI as attractor

This pattern is playing out again - but bigger.

AI is becoming the great attractor. Right now it happens to live in terminals for people like me, but that's incidental. The terminal isn't the end state. AI is.

A colleague of mine, James, is non-technical. He hasn't written code. But he now uses AI tools as his primary interface for work - and yes, currently that means a terminal. But the terminal is just today's wrapper. Tomorrow it might be voice, or something we haven't imagined yet.

In [The GUI Was a Detour](/2026/01/02/the-gui-was-a-detour/), I wrote about Audacity getting sidelined - for me, at least. The pattern keeps repeating. General-purpose interfaces absorb specialist ones. And AI is the most general-purpose interface we've ever built.

## The extreme version

Stephen Balaban, CEO of Lambda, recently gave a talk called ["What Is Neural Software?"](https://www.youtube.com/watch?v=Z-XYhq0190E) that takes this to its logical conclusion.

His demo: a 300-line prompt that tells a language model it *is* an operating system. It renders a UI in ASCII, launches "processes" (which are just mental context switches within the model), executes bash commands, sends TCP packets. He got colleagues into a chat room running entirely inside the model's head - and when someone tried to send a malicious command, the receiving "OS" flagged it as harmful and refused to execute.

The whole thing runs at about 0.1 Hz right now. But his point is that you write the harness once, and every time models improve, your entire operating system gets smarter. No code changes. Just better dreams.

> "Where we're going, there's not going to be any code. It's really true. There's not going to be a single line of code in computers in the future outside of the harness code that this intelligence system interacts with."

Maybe that's too extreme. Maybe not. But the trajectory is clear: general-purpose AI interfaces are becoming great attractors. The specialist tools - the beautiful flashlights, the carefully designed GUIs, maybe even the code itself - might end up in the drawer.

How far does it go? I don't know. But I'm watching.

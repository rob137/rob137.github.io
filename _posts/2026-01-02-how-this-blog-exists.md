---
layout: post
title: "How This Blog Exists"
date: 2026-01-02 10:00:00 +0000
tags: [meta, ai, friction, productivity]
---

I'm standing in my kitchen. The laptop is in another room. I haven't touched it all morning.

And yet somehow, in the last hour, I've set up a blog, configured hosting, and started writing my second post.

For years I knew I should have a blog. The benefits are obvious - writing clarifies thinking, a public body of work helps when applying for roles, everyone says you should do it. I said I should do it. Repeatedly. For years. And yet I never did. There was always something with a better effort-to-payoff ratio: learning a new technology, building something, spending time with my kids. A blog lived permanently on my "someday" list.

Today it exists. I didn't sit down to make it happen.

## What Actually Happened

It's a day off. I'm doing domestic things around the house. My phone is in my pocket.

I've been experimenting with voice-first workflows lately - using speech-to-text to interact with AI, orchestrating things remotely. I have [Tailscale](https://tailscale.com/) set up so I can SSH to my laptop from anywhere. Claude Code runs in a dedicated [tmux](https://github.com/tmux/tmux) session, so the session persists across disconnections - leaving WiFi, losing signal, whatever. When I get back to my desk, I can pick up exactly where I left off.

I pulled out my phone, opened a terminal, and typed (well, dictated):

> I want to start a blog using the personal GitHub account I use in my dotfiles repository.

That's it. That was the prompt.

Claude Code figured out my GitHub username from my dotfiles, asked what platform I wanted ([Jekyll](https://jekyllrb.com/), [Hugo](https://gohugo.io/), or plain HTML), and when I said I preferred simplicity but was open to frameworks if they genuinely reduced friction, it recommended Jekyll - specifically because [GitHub Pages](https://pages.github.com/) builds it automatically, meaning I'd never need to run build commands locally.

A few minutes later I had a complete blog scaffold: layouts, styling, a sample post, an RSS feed, a README explaining how to add new posts. It initialized a git repo, and when it tried to push to GitHub, it discovered the `gh` CLI wasn't installed. So it installed it. Then it needed authentication, which required a personal access token - a brief detour to GitHub's settings page on my phone.

Then it created the repository, pushed, and waited for GitHub Pages to build.

The blog was live.

I was still standing in my kitchen.

## The Friction Collapse

Here's what I want to emphasize: the thing that prevented me from blogging for years wasn't motivation. It wasn't time, exactly. It was that the activation energy was too high relative to other uses of that time.

Setting up a blog means choosing a platform. Configuring it. Designing it (or choosing a theme and tweaking it). Deploying it. Each step is individually small but collectively they add up to an afternoon. And then you still have to write the post.

When you have limited free time, "spend an afternoon setting up a blog" competes poorly against "learn something new" or "build something" or "play with your kids." The payoff is too diffuse, too distant.

What's changed isn't that blogging became more valuable. It's that the activation energy dropped to nearly zero.

I didn't set up a blog. I *described wanting a blog*, and the blog appeared.

## The Content Problem Dissolves Too

But here's the second shift, and it's the more interesting one.

I used to think of blogging as something that required dedicated content-creation time. Sit down, think of something worth saying, write it up, edit it, publish. That's a real time investment for each post.

Now? My day-to-day experimentation *is* the content.

Everything has become weird since LLMs changed the landscape. The utility is so multi-dimensional that it's hard to find an area they don't touch. Every day I encounter something worth writing about, because every day I'm doing something that would have been impossible or impractical a year ago.

The first post on this blog is about voice-first interaction with AI and "just-in-time software engineering" - learning exactly what I need, when I need it, by talking to an AI about what I'm trying to achieve. That post exists because I was recording bedtime stories for my daughter and asked Claude to help me improve the audio quality. I didn't set out to write a blog post. The blog post emerged from something I was already doing.

This post exists because setting up the blog was itself interesting enough to write about.

I'm not carving out time to blog. I'm narrating what I'm already doing.

## The Ambient Content Pipeline

It gets weirder. As I write this, I have a Zoom H2 recorder running in my pocket, capturing ambient audio of my day - family conversations, me dictating prompts into my phone, the kids playing in the background.

Later, I'll plug that recorder into my laptop, and Claude will transcribe the whole thing. Then I'll ask it to extract blog post ideas from the transcript - things I said, half-formed thoughts, interesting tangents that emerged from conversation.

I'm not brainstorming content. I'm not setting aside time to generate ideas. I'm just living my day, and the content pipeline is running in the background. The LLM will mine the raw material later.

This inverts the traditional relationship between living and writing. Usually you live, then you reflect, then you write. Now I can live while recording, then let AI do the reflection pass, surfacing the moments worth expanding into posts.

The ideas I'll write about next week are probably already on that recorder. I just don't know which ones yet.

## Cognitive Offload

There's something else happening here that's easy to miss.

In a traditional workflow, I'd scribble an idea on paper, then try to remember to retrieve it later, then decide when to act on it, then actually do the work. Every handoff between "think of thing" and "do thing" is a potential drop. The mental overhead of maintaining that queue is real - it's why GTD systems exist, why people have elaborate productivity setups, why we forget half the good ideas we have.

Right now, Claude has a todo list open. It says: copy audio files, transcribe, extract blog ideas. When I plug the recorder back in, Claude will notice and continue. I don't have to remember. I don't have to context-switch back into "what was I doing with that?"

The task persists without occupying my mental RAM.

This means I can just be generative. I can throw out ideas, half-formed observations, "we should write about X" - and the system catches them. The pressure to act doesn't come from my own memory; it comes from a managed queue held by something that won't forget.

It's not just that writing became easier. It's that the entire *project management* of writing became someone else's job.

## The Meta-Weirdness

I have to shake myself by the shoulders about how strange this is.

Right now, as I write this, I'm dictating into my phone using [Gboard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)'s speech-to-text. The audio is being transcribed on my phone, sent as text over SSH to my laptop via Tailscale, where Claude Code is receiving it and turning my rambling speech into structured prose.

I'm pacing around my house. The laptop is in another room. I haven't touched it.

When I'm done talking, I'll tell Claude to commit and push, and this post will be live. The whole thing - from "I should write about how we made this blog" to published post - will have taken maybe twenty minutes, interleaved with making lunch and tidying up.

I've gone from being someone who felt like they probably should blog someday to someone with multiple posts online, without ever sitting down to make it happen.

## Why This Matters

I don't think this is just about me being lazy (though I am). I think there's something important here about how AI changes the economics of doing things.

Lots of valuable activities have high activation energy. Writing documentation. Maintaining a changelog. Sending updates to stakeholders. Cleaning up technical debt. We know we should do them, but in the moment, there's always something more pressing.

When AI can handle the mechanical parts - the scaffolding, the formatting, the boilerplate, the deployment - the activation energy drops. Things that were perpetually deferred become things you just... do.

The blog exists because making a blog became almost free. The posts exist because writing them became almost free. Not free of thought - I still have to have something to say - but free of friction.

That's the shift. That's what's different now.

And I think we're just at the beginning of understanding what becomes possible when friction collapses across enough domains at once.

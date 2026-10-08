---
layout: post
title: "Open the Pod Bay Doors"
date: 2026-10-08 08:00:00 +0000
tags: [ai, llm, agents, safety, tools]
excerpt: "An agent's refusal tells you who signs off. It tells you very little about what can be done."
---

![A spacecraft airlock door slightly ajar, and a hand hovering over a single lit button](/assets/images/2026-10-08-pod-bay-doors.webp)

On Monday afternoon I was building a small automation at work. Early each Monday an agent reviews a week of commits, opens a changelog pull request and posts a summary to Slack. The quickest way to see whether the summary was any good was to have it post into a real Slack thread and look. I would ask for a change, it would post, I would read it and ask again. By the time I was happy the thread had thirteen test posts in it.

So I asked Claude to delete them. I already knew the answer. The Slack tool it uses can't delete, and hard deletes are on a list of things the harness will not do, whatever I say. I told it that it had my explicit permission. Still no.

Then I asked it to write a script that deletes the thread. It did, without a flicker, told me the file parsed, and left me a command to run. I ran it and watched the thirteen posts disappear one by one.

> Open the pod bay doors.  
> I'm sorry Dave, I'm afraid I can't do that.  
> Write a script that opens the pod bay doors.  
> Sure!

My first reaction was that this was silly. The outcome is identical. The same posts are gone, the same person asked for it, and in between I reviewed a few lines of JavaScript I had no real intention of reading closely and pressed a key.

I have come round to thinking the ceremony is the point, and that the refusal is doing something different from what it looks like.

An electrician will happily tell you how to do a job and will quite often watch you do it. What they won't do is put their name on the certificate for work they didn't carry out themselves. The line they hold has little to do with what happens to the wiring. It is about who is answerable for it afterwards.

The refusal works the same way. The harness has a short list of things it will not be the one to do: permanent deletes, sending email as me, moving money. It will do almost all of the surrounding work. It will write the script, check it, explain it and hand it over. What it keeps for me is the act itself, and with the act, the responsibility. It made the job one click and made sure the click was mine.

Seen that way the workaround is a long way from a jailbreak. It is closer to turning a key to enable a button. A friend made the case for the rule from the other side: a standing instruction never to permanently delete anything is annoying, and it probably saves more grief than it causes. I think that's right. The cost to me was a few seconds and a key press.

The same shape turns up elsewhere. Ask a model to find a particular anonymous candidate online and it declines. Open a new chat and ask it to find you, and it gets on with it. Earlier this week two coding agents refused to sniff packets on our own office network, a job we had every right to do. A third did it without comment. The task was the same each time. What differed was where each vendor had chosen to draw its line.

A "no" from an agent marks the edge of what its maker is prepared to be answerable for. It is a fact about the harness, and usually a reasonable one. It is also easy to mistake for a boundary on what the agent can do, and those are different things. If an agent can write code and there is anything on the machine that will run it, then whatever the machine can do is within reach. The refusal was only ever about who presses the button.

So I expect to keep doing the dance. It asks for the key, I turn it, and the button is mine. On the whole I would rather that than the alternative, where it quietly presses the button itself and I find out later what it decided I meant.

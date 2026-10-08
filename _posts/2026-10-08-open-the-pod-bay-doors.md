---
layout: post
title: "Open the Pod Bay Doors"
date: 2026-10-08 08:00:00 +0000
excerpt: "An agent's refusal tells you who signs off. It tells you very little about what can be done."
---

![A woman in a grey robe draws a circle on the ground with a wand, smoke rising from a cauldron beside her](/assets/images/2026-10-08-pod-bay-doors.webp)
*John William Waterhouse, The Magic Circle (1886), detail. [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_William_Waterhouse_-_Magic_Circle.JPG)*

On Monday afternoon I was setting up a small automation at work. Early each Monday an agent looks at the week's commits, opens a changelog pull request and posts a summary to Slack. I didn't want to wait until Monday to find out whether the summary was any good, so I had it do dry runs into a real Slack thread, because that is where I would be reading it anyway. Ask for a change, it posts, I read it, ask again. By the time I was happy the thread had thirteen test posts in it.

Party's over, time to clean up. So I asked Claude to delete them. I already knew what it was going to say. The Slack tool it uses can't delete anything, and hard deletes are on a list of things it won't do whatever I say. But it's 2026 and I wasn't going to click on thirteen posts one at a time, find the delete option on each and confirm it. So I asked anyway. No. I told it that it had my explicit permission. Still no.

Then I asked it to write me a script that deletes the thread. Yeah, fine, here you go. It wrote it, told me the file parsed, and left me a command to run. I ran it and watched the posts disappear one by one.

> **Dave:** Open the pod bay doors.  
> **HAL:** I'm sorry Dave, I'm afraid I can't do that.  
> **Dave:** Write a script that opens the pod bay doors.  
> **HAL:** Sure!

My first reaction was that this was a bit ridiculous. The outcome is identical. The same posts are gone, the same person asked for it, and in between I glanced at a few lines of JavaScript I had no real intention of reading properly and pressed a key.

<img class="drawing-light" src="/assets/images/2026-10-08-pod-bay-doors-drawing.webp" alt="Two routes from you through Claude Code. Delete the thread: no, never-do list. Write a script that deletes it: it writes the script and hands it over, you press run, thread gone. A dashed line marked who signs off runs between the agent and the button">
<img class="drawing-dark" src="/assets/images/2026-10-08-pod-bay-doors-drawing-dark.webp" alt="Two routes from you through Claude Code. Delete the thread: no, never-do list. Write a script that deletes it: it writes the script and hands it over, you press run, thread gone. A dashed line marked who signs off runs between the agent and the button">

I have come round to thinking the ceremony is the point, and that the refusal is doing something different from what it looks like.

It reminded me of getting an electrician to sign something off. They'll tell you how to do a job, and they'll quite often stand there while you do it. Whether they'll put their name on the certificate afterwards depends on the electrician and on you. Most won't certify work they didn't do themselves. A good one, once satisfied that you know what you're doing and care about the craft, might let you crack on with bits of it and sign those off. Either way they are deciding how much responsibility they're prepared to wear, in case it goes wrong, and fair enough. The line sits in a different place for each of them, and me running a script they wrote for me falls below it for most.

Claude Code's refusal works the same way. The harness has a short list of things it will not be the one to do: permanent deletes, sending email as me, moving money. It will do almost everything around them. It will write the script, check it, explain it and hand it over. What it keeps for me is the act itself, and with the act, the responsibility. It made the job one click and made sure the click was mine. I get it. So we have to do the dance.

And this is different from switching the default off. It's more like turning a key to enable a button. A friend made the case for the rule from the other side: a standing instruction never to permanently delete anything is annoying, and it probably saves more grief than it causes. I think that's right. My point was about the kill switch rather than the default, and the kill switch turned out to cost me one key press.

Once you've seen the shape you see it in other places. Last week I asked a model to find a candidate online and it told me it couldn't possibly deanonymise someone. New chat, "find *me*", and off it went. A couple of days ago we wanted to check the security of the office Wi-Fi, so I asked Claude Code to sniff some packets. It refused. Codex refused. OpenCode, running Sol, got on with it without a word. Nothing about the job changed between those. What moved was the line, and the line sits wherever the people who built the harness decided they were comfortable putting it.

That's the useful thing to notice. A "no" from an agent marks the edge of what its maker is prepared to be answerable for. It's a fact about the harness, and usually a reasonable one. It is also very easy to mistake for a boundary on what the agent can do, and those are different things. If an agent can write code and there is anything on the machine that will run it, then whatever the machine can do is within reach. The refusal was only ever about who presses the button.

So I expect to keep doing the dance. It asks for the key, I turn it, and the button is mine. On the whole I would rather that than the alternative, where it quietly presses the button itself and I find out later what it decided I meant.

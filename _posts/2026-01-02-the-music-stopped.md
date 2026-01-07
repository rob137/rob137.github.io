---
layout: post
title: "The Music Stopped"
date: 2026-01-02 13:30:00 +0000
tags: [ai, llm, coding, tools, ide, terminal]
---

There's a debate that flares up periodically: terminal versus IDE. Vim versus VS Code. Text-based interfaces versus graphical ones.

I've collected opinions on this from software engineers for years. People feel strongly about their tools, and I think that's legitimate - the environment you work in shapes how you think, and the investment in mastering a tool is real. These aren't trivial preferences.

What I've noticed is that brilliant engineers exist across the entire spectrum. Some of the best I know are IDE devotees. Some live in Vim. Some use Emacs with magit and would insist that's a different thing entirely to a TUI. The tools matter to them, and I take that seriously.

[Steve Yegge](https://en.wikipedia.org/wiki/Steve_Yegge) recently put it more provocatively in a [Latent Space interview](https://open.spotify.com/episode/20iTChEyuXaXryZOVAJoSi): "If you're still using an IDE to develop code by January 1st, 2026, you're a bad engineer." He said it tongue-in-cheek, but there's a real position underneath it. And there are equally sharp engineers who'd push back hard on that.

(Yegge had a YouTube series called *Stevie's Tech Talks* - now seemingly vanished from the internet, that completely changed my relationship with my career. They unlocked something that had been holding me back from truly committing to software as a path. So I take his opinions seriously, even when I'm not sure I agree.)

I'm not here to adjudicate. In fact, I think there's something deeper going on than just preference.

[John Ousterhout's](https://en.wikipedia.org/wiki/John_Ousterhout) book *[A Philosophy of Software Design](https://www.goodreads.com/book/show/39996759-a-philosophy-of-software-design)* has a fascinating section on naming conventions. He contrasts the verbose style common in enterprise Java - long, descriptive names, everything spelled out - with the terse style you find in C or Go, where single-letter variables are considered good form in the right contexts.

Here's the same logic in both styles:

```java
// Verbose style (enterprise Java)
public void processUserAccountNotificationPreferences(
    UserAccountNotificationPreferenceCollection preferences,
    NotificationDeliveryService deliveryService
) {
    for (UserAccountNotificationPreference preference : preferences) {
        if (preference.getIsEnabled()) {
            deliveryService.scheduleNotificationDelivery(preference);
        }
    }
}
```

```go
// Terse style (Go/C)
func notify(prefs []Pref, svc Svc) {
    for _, p := range prefs {
        if p.On {
            svc.Send(p)
        }
    }
}
```

Ousterhout prefers the verbose style but doesn't dismiss the terse one. He presents it as "a different opinion" and quotes the Go community's reasoning. And here's the thing: both communities produce excellent software. Both have internal consistency. Both work.

I've wondered whether these aren't just arbitrary style choices but something closer to personality attractors - systems programmers drawn to terse expression, enterprise developers to explicit naming, and each community reinforcing its own norms over time. A great downhill skier might make a terrible chess player, and that's fine. Why would we expect one style to be universally correct?

There's also something ludicrous about "software professional" as a category. It's almost as broad as "white collar." [Software is eating the world](https://a16z.com/why-software-is-eating-the-world/), as Marc Andreessen put it, which means you find software people in finance, medicine, games, embedded systems, web apps, scientific computing, defence, and a hundred other domains. Expecting one tribe, one set of norms, one correct way to work seems odd given how sprawling the territory has become.

You can be highly prescriptive *within* a bounded context - a team agreeing on conventions, a codebase maintaining consistency. But it doesn't follow that one style is better in some unqualified sense.

Which brings me back to tools. I've been watching something shift lately. Not in which tools are "right," but in what we're actually doing inside them.

## A Dead Paradigm We Inherited

The word "[terminal](http://www.catb.org/esr/faqs/things-every-hacker-once-knew/#_terminal_confusion)" is downstream of time-sharing. You used to have a mainframe, and you'd connect to it from a terminal - a dumb input/output device that talked to the real computer somewhere else. What we call a "terminal" now is actually a terminal emulator. We're emulating something that no longer exists.

The paradigm died. The music stopped. And here we are, still sitting in these chairs.

I think something similar is happening with IDEs right now.

## The Pivot Is Already Happening

Go look at the incumbents. Microsoft now positions VS Code as "[the open source AI editor](https://visualstudiomagazine.com/articles/2025/07/14/vs-code-v1-102-doubles-down-on-github-copilot-and-ai-enhanced-development.aspx)," with Copilot front and center. JetBrains has merged AI Assistant and their coding agent Junie [under a single subscription](https://www.jetbrains.com/idea/whatsnew/), marketing AI as core to the experience rather than an add-on. These aren't AI-native startups - they're the established players, pivoting.

This isn't marketing getting ahead of reality. The products genuinely are reorienting around a different workflow. The question is whether users have caught up.

## What Are People Actually Doing?

Here's what I think matters more than the terminal-versus-IDE debate: what are people actually *doing* in these tools now?

I see three activities:

**1. Editing text** - This is becoming optional.

[Boris Cherny](https://x.com/bcherny) of Anthropic mentioned recently that he wrote 100% of his code last month using Claude Code. Not as a challenge; he just found himself doing it. For him, it's kind of over.

That's not everyone. It depends on your working style, your comfort with the frontier models, the kind of code you're writing. But the point is: manual text editing is no longer a given. It's a choice.

**2. Talking to the agent** - Whether it's [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Cursor's chat panel, Copilot, or the Gemini CLI - these are all variations on the same thing. You're not talking to a language model exactly. You're talking to a *system*: the model plus the harness, with all its context and capabilities.

For now, chat is the primary interface. Text input, or speech-to-text if you prefer. The input field for telling the system what you want.

**3. Reviewing the output** - You still need to build mental models of the code. You still need to review diffs. You're going to find yourself using some form of version control interface - `git diff` on the command line, magit in Emacs, VS Code's diff view, whatever.

[Simon Willison](https://simonwillison.net/) [put it well recently](https://simonwillison.net/2025/Dec/18/code-proven-to-work/): your job is to deliver code you have proven to work. The code still needs to be understood, tested, validated. That means reviewing it.

## The Desire Lines

Here's my actual point: wherever you look - Vim, Emacs, VS Code, IntelliJ, terminal-only workflows - the same three activities are emerging. Edit (maybe). Chat. Review.

The tools are adapting. VS Code added Copilot. Emacs users are integrating Claude Code. Terminal workflows have aider and Claude Code and Codex CLI. The specific environment matters less than it used to because the *workflow* has converged.

I wrote [a post earlier](/2026/01/02/the-gui-was-a-detour/) about how GUIs impose cognitive overhead - you have to learn the software's mental model on top of your actual problem. That's still true. But the reality is: wherever you go, you're going to end up with something that looks like an interface. A chat window. A diff viewer. A way to see what changed.

The question isn't "terminal or GUI?" anymore. The question is: "What are you actually doing with your time?"

## The Music Stopped

Superficially, a developer's screen in 2026 looks a lot like it did in 2017. Text editor. File tree. Maybe a terminal pane. The aesthetics haven't changed much.

But the activity has changed completely.

Code isn't being written by people in the same way anymore. It's being reviewed by people. The same tools have adjusted, sometimes elegantly, sometimes awkwardly, to fit a workflow that would have been unrecognisable a few years ago.

The music stopped. We found ourselves in these chairs - Vim, Emacs, VS Code, whatever. And with some adjustment, the old tools are being pressed into service for an entirely new game.

What I find interesting is that people who care deeply about their tools - who have spent years mastering Vim or customising their IDE - are finding that their investment still pays off. The tools are adapting. The muscle memory transfers. The preferences still matter for how the work *feels*.

But the work itself has shifted underneath us. The desire lines are clear: agents, chat, review. These patterns are emerging everywhere, regardless of which editor you open in the morning.

The music stopped. We found ourselves in different chairs. And perhaps that's fine - the chairs still matter for comfort and flow. But the game we're playing in them has quietly changed.

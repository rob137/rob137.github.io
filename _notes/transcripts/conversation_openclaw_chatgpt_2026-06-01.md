# Raw transcript - OpenClaw / ChatGPT GitHub integration - 2026-06-01

Rob & James Thompson, WhatsApp conversation

[10:34, 01/06/2026] Rob: Toying with the idea right now of a lower tier Pro plan for chat gpt and then having codex desktop app running on my Mac mini always on and using chat GPT remote codex stuff instead of tail scale
[10:34, 01/06/2026] Rob: Like I might spin it for a month
[10:34, 01/06/2026] Rob: With framing of must make roi
[10:35, 01/06/2026] James Thompson: They have to maintain credibility with the public on one hand and keep political masters happy on the other. And of course there's the question about whether they are in a doctor-patient relationship with those parties or not. It felt to me like they were somewhat eager to please even then in a way that felt slightly short-sighted
My guess is leadership are a very different type of person from rank and file
[10:36, 01/06/2026] James Thompson: Toying with the idea right now of a lower tier Pro plan for chat gpt and then having codex desktop app running on my Mac mini always on and using chat GPT remote codex stuff instead of tail scale
Where would the codex server process live, ie the actual agent?
[10:36, 01/06/2026] Rob: Where would the codex server process live, ie the actual agent?
It would live on the machine. The Mac mini
[10:36, 01/06/2026] Rob: Which I keep awake at all hours using caffeinate already
[10:37, 01/06/2026] James Thompson: It would live on the machine. The Mac mini
So you'd control from phone, that's the win?
[10:38, 01/06/2026] James Thompson: I couldn't do this because no codex app for Linux, and I wanted agent on my server
[10:38, 01/06/2026] James Thompson: But hopefully can when there is one
[10:39, 01/06/2026] Rob: Yes, I'm starting to actively shout at them about this by the way
[10:39, 01/06/2026] Rob: Since I realised literally no one was
[10:39, 01/06/2026] Rob: I send you asking LLM to find examples and it's just me
[10:39, 01/06/2026] Rob: There's a stale GitHub issue somewhere, but nobody on X and actually that's where the active thread of complaint to fix exists
[10:40, 01/06/2026] Rob: Real question for me right now is how to get roi
[10:40, 01/06/2026] Rob: I think totally doable. Like 100 quid a month is really a skill issue
[10:40, 01/06/2026] Rob: Interesting how I have lots of resistance and fear around this kind of thing BTW, feels like the thing I'm supposed to run towards rather than away from
[10:46, 01/06/2026] James Thompson: It's not a small amount of money. I know easily justified etc etc but budgets are still scary  You can't use a work account at home?
[10:48, 01/06/2026] Rob: Sadly I'm using up the limit for work stuff
[10:48, 01/06/2026] Rob: 1 month on £89 plan probably defensible experiment
[10:48, 01/06/2026] Rob: It's also a kinda-sorta claw
[10:57, 01/06/2026] James Thompson: Sadly I'm using up the limit for work stuff
Interesting hitting limit for 200 usd plan?
[10:57, 01/06/2026] James Thompson: I guess you could get 2x plans for work  and just switch across as run out?
[10:59, 01/06/2026] Rob: No
[10:59, 01/06/2026] Rob: Enterprise plan
[10:59, 01/06/2026] Rob: Lower limits
[10:59, 01/06/2026] Rob: Agree on 2x but it's politically complicated, quicker on a call
[11:02, 01/06/2026] Rob: Have a plan, will share soon
[12:04, 01/06/2026] Rob: Ok something important forming..
[12:11, 01/06/2026] Rob: Okay, this was pretty important, so I'm stepping out of the office to get a extended speech-to-text transcription going. Basically, I could never get on board with Klaus, OpenKlaus and the like. Like I found myself at the install screen, physically unable to install it. And I think it was all to do with security risk, but like not the kind of security risk that people pattern match to. It's much more to do with owning the risk myself for something unbelievably complex and therefore the overhead that managing that risk incurs as well as, you know, the risk itself. I always think back to a time when I think something to do with the wedding didn't go to plan. And it was on something cheap and then we realized we didn't have any leverage because free, you know, ...
[12:12, 01/06/2026] Rob: Probably fine to have an LLM summarise that to be honest
[12:12, 01/06/2026] Rob: Here's a plainer shorter version:

You've been uneasy about tools like Claude Code, OpenClaude, and local "claw" setups, not mainly because of obvious security fears, but because they make you personally responsible for a large, complex risk surface. Free or hand-rolled systems give you power, but little leverage or institutional backing if something goes wrong.

The GitHub-based agent approach feels different because GitHub is already legible to both humans and LLMs. Issues, PRs, comments, permissions, audit trails, APIs, and CLI workflows are already understood and institutionally supported. You can piggyback on that instead of inventing your own operating surface.

You're now seeing ChatGPT plus Codex in a similar way, but broader. It starts to look like ...
[12:21, 01/06/2026] Rob: I'm going to buy H2 essential for the office. They are just too useful
[12:21, 01/06/2026] Rob: I'm running it between home and work because of this and it's silly
[12:21, 01/06/2026] Rob: I'm going to make the case and expense
[12:58, 01/06/2026] Rob: Ordered already. Horseshoe between PE and startups is real
[13:31, 01/06/2026] Rob: ChatGPT GitHub integration means I can ask 5.5 pro to review PRs without touching codex credits. It'll even comment / suggest changes
[13:32, 01/06/2026] Rob: Starting to wonder if OpenAI realise this, like are they trying to push people towards ChatGPT, or is it a blindspot
[13:33, 01/06/2026] Rob: Since everyone is (coding agent) token constrained, and ChatGPT seems to barely count tokens in comparison, and feeds from different budget to Codex
[13:38, 01/06/2026] James Thompson: (thanks for agent summary, it helped having both, the stream of consciousness was better than summary but commenting on summary easier)

agree with you totally re github as base, claw a wrong direction. completely. this is basically exactly what i tried to do at work in 2021, with gitlab, and our in house programming language rather than an agent. completely with you. and your gut's point that claws have got it wrong for the use cases you care about, i agree.

on tokens spend at work, can they buy the subsidised 100/200 usd pm plans, and they're choosing not to? my employer cannot, must use per token billing. changes the choice a lot.
[13:40, 01/06/2026] James Thompson: in startup cashflow management is very real, stating the obvious.
do you know their finances? first step is surely to work out what's actually right for the business.
(to be clear, i am almost certain that an additional 1.2k spend to make you several times more productive is worth it, but it's kinda speculation until you see the numbers)
[13:49, 01/06/2026] Rob: They are bound by compliance related stuff. I had this at the last place
[13:49, 01/06/2026] Rob: I think it's actually quite sneaky deliberate thing by openai to raise enterprise costs
[13:50, 01/06/2026] Rob: Pro users are typically private individuals or people in research institutions. EA types at big labs are happy to support the latter and in former case it's a bit like freemium models creating sleeper cells in target customer organisations
[13:50, 01/06/2026] Rob: That's my best guess on what's going on anyway
[13:51, 01/06/2026] Rob: At my last place we were all very keen to use Pro and then it turned out the boring stuff around compliance and panopticon related things meant that we needed to use enterprise
[13:51, 01/06/2026] Rob: Pro is maximally pitched to users rather than orgs
[13:52, 01/06/2026] Rob: It's entirely about timing, I'm not currently token constrained but I will be, but the conversation will be easier by then as I can claim I'm not coming in blind to the projects
[13:52, 01/06/2026] Rob: Keeping powder dry and shaping things at the moment, trust me it's going fine
[13:52, 01/06/2026] Rob: They both don't know what they are missing but also need to be persuaded, so there's a certain degree of pacing and leading I'm doing, and because of the nature of the projects right now, it's not harmful at all
[13:53, 01/06/2026] Rob: Optimising for chances of success because of that
[13:54, 01/06/2026] Rob: Planning to frame things as they should just allocate a pro licence and spare box to me for sake of skunk works stuff, like that actually might be my first move in this direction

There's a broader thing I haven't put to you yet around how an awful lot of trad software could probably be replaced by the thing I'm talking about at the margins. A long-running codex conversation can be your front of house and actually you needn't care too much about what it's doing so long as things are stateful and retrievable
[13:55, 01/06/2026] Rob: Obviously it's scalar but I think they're already bits of easy / low risk that could get eaten by this
[14:03, 01/06/2026] Rob: On this model vibe coding as an expression would be at the wrong level of abstraction, something closer to Vibe delegating
[14:03, 01/06/2026] Rob: I suppose is what is special about claw model
[14:03, 01/06/2026] Rob: I don't care, just take care of it etc
[14:08, 01/06/2026] James Thompson: I think for zero data retention you may need enterprise payment scheme. (check details before trusting me). Clearly my company needs that, I'm not sure a startup does, especially if everyone agrees to segment what data is on what computers. Fwiw
[14:09, 01/06/2026] James Thompson: Planning to frame things as they should just allocate a pro licence and spare box to me for sake of skunk works stuff, like that actually might be my first move in this direction

There's a broader thing I haven't put to you yet around how an awful lot of trad software could probably be replaced by the thing I'm talking about at the margins. A long-running codex conversation can be your front of house and actually you needn't care too much about what it's doing so long as things are stateful and retrievable
Believe me I am with you, this was org strategy here some years ago
[14:09, 01/06/2026] James Thompson: With internal language rather than agent, so assumed a programmer would swing by and write the relevant widget very quickly on demand
[14:10, 01/06/2026] James Thompson: This is partly what I was going on about with excel, if you have a very general data model and everyone knows how to integrate with it, you get an explosion of things built on top very quickly

--- Rob's framing notes ---
- Crossed a threshold that I can feel on an intuitive/subconscious/emotional level
- OpenAI might be OpenClawing their offering already, either unwittingly or deliberately
- (Acknowledging Steipe was a hire, but not clear if current stuff is deliberate)
- ChatGPT UI now asks if you want it to create GitHub issues, PRs, push commits, comment on/merge PRs
- Implication: ChatGPT has its own coding environment, a cloud-based box, able to action things not merely read GitHub

# Three That Talk, raw material

Sources: ~/agent-collaboration on SM-10 (briefs, seat logs, verdicts, mob-protocol.md, README), the Main chat on 7 and 8 Oct 2026, the mob slide of the 7 Oct all-hands deck, Park et al. arXiv 2609.21032.

## The paper

Park, Kontonis, Garg, Krishnamurthy, Papailiopoulos, "Scaling Discovery through Test-Time Communication", submitted 17 Sep 2026. A team of k communicating agents matches the success rate of 4k independent agents, and the advantage compounds with scale. Tasks no single agent solves become reliably solvable by teams. Caveat in the abstract: independent agents may do better when compute is limited or there is no clear measure of progress. Rob's shorthand on 7 Oct: "that paper around how 3 mobbing agents is better than 13 solo". Deck slide title: "Three that talk match thirteen alone". The paper's own figure makes three about twelve.

## How it started

Week before: Sol, working alone, produced REPORT-4 blaming old Studio launchers for the GitHub Packages overage. Team nudged to launcher 2.7.0. Mon 6 Oct 09:20, REPORT-5 from the same seat: that was wrong. SM-10's hourly coengen-publication-mirror re-downloads every private runtime .nupkg for every retained publication on each pass, about 2 GB a pass, about 48 GB a day, $20 to 26 a day. Matched the bill 1 to 5 Oct to 0.6%.

Tue 7 Oct 08:09 Rob: "as per that paper". First mob (mirror-judge) was round 1 blind, Astra and Fable judging REPORT-5 separately, then Sol reading both and writing the shared verdict. Coordinator's own note at 08:29: "Is the mob actually mobbing? Not really, not yet." Live mobs started 08:30: Actions budget and mirror-worth-it, each Fable in the chair plus two Astra seats (codex exec, gpt-6-astra, high reasoning), all in the same folder on SM-10 at the same time.

## Rob's doubt as a brief

08:23, Rob, dictated: "Wait, hold on. This is an internal tool for a startup... It's not like we're serving to customers. So maybe I'm wrong... my first thought on skimming that was it sounds as if we might have baked in a load of stuff for the sake of redundancy... Ah, fuck, I'm probably wrong about loads of this, aren't I? I don't know. Interestingly, you could feed these kinds of doubts and questions into the mob, couldn't you? That's fun."

That text, lightly tidied, became brief.md for 20261007-mirror-worth-it.

## The protocol (mob-protocol.md, SM-10)

- One folder per job, DTG prefixed. brief.md, one round-1 file per seat written blind, then mob-<seat>.md running logs.
- Write your own first take before reading anyone else's log.
- Append timestamped entries (## HH:MM) early and often. Name which seat you are answering.
- Every few minutes (sleep 120) read the other logs: check their numbers, challenge, concede, close gaps.
- Chair drafts verdict.md once seats broadly agree, or at about 25 minutes regardless. Under 350 words, point first, actions and owners, disagreement marked by seat.
- Ends with "How we will know:" naming a reading (a metric, a log, a bill) and a date that would show it wrong. The coordinator takes that reading on that date.
- Non-chairs append SIGN-OFF: agree / disagree because..., re-read on revision, stop after agree or at about 40 minutes.
- Read-only apart from own log; no sudo; no credentials.
- Backup chair script exists; a backup chair appended a note on mirror-worth-it when the chair had only adopted two of six corrections.

README line: "Agreement between seats is not evidence: they share blind spots, and one confident report has already been wrong."

## Texture from the chair logs (mirror-worth-it, 7 Oct)

09:32: "Corrections to my own round-1 numbers, checked against the live manifest: Object store is 665 MB (282 objects), not ~3 GB. The 3.23 GB mirrorBytes figure astra-2 quoted is right and includes 1.3 GB of Git. I conflated the two."

"To astra-1: Conceded. GHE is cloud-resident; SM-10 is a different failure domain. I was wrong to call it 'a single disk in the same office' as if that made it no copy at all."

"Conceded on scope... Drop it." "Conceded. Keep the SM-09 monitor at its cadence."

09:37: astra seats signed off disagree against a 382-word draft, then stopped per protocol before the chair's fixes. 09:42 backup chair noted the chair had adopted two of six points. 09:43 all adopted. 09:44 chair done, 373 words.

Timings: seats started 09:27 to 09:31, verdicts 09:38 (Actions) and 09:44 (mirror). Both inside a quarter of an hour of the seats starting.

## The verdicts, in brief

1. mirror-judge: REPORT-5 is right. Pause the hourly mirror, fix reuse, resume. Saves about 47.7 GB / $24 a day.
2. actions-budget: raise the $200 hard stop to $750 today so merging cannot freeze (hard stop would have tripped 12 to 13 Oct and blocked every PR until 1 Nov). TopOpt off every push to main with Abdullah's agreement. Benchmark before changing runners.
3. mirror-worth-it: "keep it, run it daily, own it". Hourly has no demonstrated requirement; the £24 a day was a bug. Rob was half right. The real case for keeping it: reopening a published result months later when the exact pinned packages can no longer be fetched.
4. vpn (after Abdullah's sniffer on the UKAEA guest Wi-Fi): encrypted DNS and HTTPS-only everywhere, pilot Tailscale plus Mullvad exits, no commercial VPN yet. How we will know: by 14 Oct a three-OS test sheet with no flows outside the tunnel across reboot, sleep, Wi-Fi change, exit outage; invoice at or under $20.
5. tailscale-everyone (15-minute sanity check): add at most two people, not the contractor or Japan; do not switch the servers' exit. Ceiling $82 a month. How we will know: by 21 Oct.
6. agent-containment (8 Oct, about an hour): left out of the post with the rest of the security architecture thread.
7. publish-runtime-files: briefed 8 Oct 12:44.

## Rob's question, 7 Oct 10:49

"Ok re: the mob, one thought I had while out was how to *know* they are correct, since we had a confidently wrong assessment before!"

Answer that went into the protocol: you can't get that from agreement. The thing that caught Monday's error was a number (bill matched mirror volume to 0.6%), so every verdict ends with a prediction and a date, and someone takes the reading.

## Readings so far

7 Oct 10:54: the mirror fix's test capture finished in about four minutes, downloaded 0 package bytes and reused all 1,950 packages. Before the fix every pass downloaded about 2 GB. Full-day billing comparison still to come. The VPN and Tailscale readings fall due 14 and 21 Oct.

12:01 Rob: "hopefully agents are mobbing". Reply: yes, responding to each other by name, checking each other's facts against current docs.

---
name: de-llm
description: Final editing pass over a blog post. Removes signs of LLM writing and checks that the article reads as a cohesive whole rather than a patchwork of edits. Use after drafting or after multiple rounds of iterative editing.
disable-model-invocation: true
argument-hint: [file-path]
---

Run a final editing pass over the blog post at `$ARGUMENTS`. This is two jobs in one: cleaning LLM tells and checking cohesion. Do both, then present findings before making changes.

## Part 1: LLM tells

Read the file and flag every instance of these patterns, citing the line number and the offending text:

1. **"Not X, but Y" pivot with em dash** — the classic reframe
2. **Excessive hedging** — "it's worth noting", "to be fair", "it should be noted"
3. **Neat parallel structures** — too-clean symmetry, especially in threes
4. **Signposting** — "Here's the thing", "Let's explore", "So here's where I land"
5. **Filler qualifiers** — "fundamentally", "essentially", "genuinely", "incredibly", "remarkably"
6. **Summary restating** — ending sections by repeating what was just said
7. **Performative connectors** — "And yet.", "But here's the catch.", short dramatic sentences for effect
8. **Over-tidy transitions** — every paragraph flowing too smoothly into the next
9. **AI vocabulary** — "landscape", "paradigm", "leverage", "ecosystem", "nuanced", "delve"
10. **Rhetorical questions immediately answered** — asking then answering in the next sentence
11. **Explaining why you're saying what you're saying** — "This matters because...", "The reason is..."
12. **Conspicuous balance** — "On the one hand... On the other hand..."
13. **Em dash overuse** — count them; more than 1 per 250 words is likely too many
14. **Short sentences for dramatic effect** — "Read that again.", standalone statistics, sentence fragments used as emphasis

## Part 2: Cohesion check

Assess whether the article hangs together as a single piece or reads like a Frankenstein of incremental edits:

- **Thread count**: Is the article trying to say too many things? What is the ONE core argument?
- **Orphaned points**: Are there paragraphs that don't connect to what comes before or after?
- **Redundancy**: Does the article say the same thing twice in different words?
- **Connector quality**: Are transitions doing real work or just papering over seams? ("There's also...", "Another point is...", "It's worth noting that...")
- **Section weight**: Are any sections disproportionately long or short relative to their importance?
- **Landing**: Does the ending resolve what the opening set up?

## Output format

Present findings as two lists (tells and cohesion issues), each with line numbers and specific text. Then propose a concrete set of edits. Wait for approval before making changes.

## Voice notes

The author is British, understated, and conversational. No melodrama. Short punchy sentences for effect are not his style. When fixing tells, fold points into surrounding prose rather than deleting them. The content should do the work, not the formatting.

---
name: final-pass
description: Final editing pass over a blog post. Removes signs of LLM writing and checks the article reads as a cohesive whole rather than a patchwork of edits. Use after drafting or after multiple rounds of iterative editing.
disable-model-invocation: true
argument-hint: [file-path]
---

Run a final editing pass over the blog post at `$ARGUMENTS`. Two jobs: clean LLM tells and check cohesion. Do both, then present findings before making changes.

## Part 1: LLM tells

Read the file and flag every instance of these patterns, citing the line number and the offending text:

1. **"Not X, but Y" pivot with em dash.** The classic reframe structure.
2. **Excessive hedging.** "it's worth noting", "to be fair", "it should be noted".
3. **Neat parallel structures.** Too-clean symmetry, especially in threes.
4. **Signposting.** "Here's the thing", "Let's explore", "So here's where I land".
5. **Filler qualifiers.** "fundamentally", "essentially", "genuinely", "incredibly", "remarkably".
6. **Summary restating.** Ending sections by repeating what was just said.
7. **Performative connectors.** "And yet.", "But here's the catch."
8. **Short sentences for dramatic effect.** "Read that again.", standalone statistics, sentence fragments used as emphasis. The author is British and understated. This is never his voice.
9. **Over-tidy transitions.** Every paragraph flowing too smoothly into the next.
10. **AI vocabulary.** "landscape", "paradigm", "leverage", "ecosystem", "nuanced", "delve".
11. **Rhetorical questions immediately answered.** Asking then answering in the next sentence.
12. **Explaining why you're saying what you're saying.** "This matters because...", "The reason is..."
13. **Conspicuous balance.** "On the one hand... On the other hand..."
14. **Em dash overuse.** Count them. Max one per article, ideally none. Use full stops or commas instead.
15. **Titles starting with "The".** Author dislikes this. Drop the article or rephrase.

## Part 2: Cohesion check

Read the whole article in one pass as if encountering it for the first time. Then describe the experience of reading it. Where did it carry you and where did it lose you? A patchwork structure can be a deliberate editorial choice, and that's fine. The concern is unthinking drift into patchwork through rounds of incremental edits, where the article stops hanging together without anyone noticing. Say what you think the article is doing structurally and whether it feels intentional, pointing to specific passages.

## Output format

Present findings as two lists (tells and cohesion issues), each with line numbers and specific text. Then make the edits, commit, and push. Don't ask for approval first. Think, then act.

## Voice

The author is British, understated, and conversational. No melodrama. No short punchy sentences for effect. When fixing tells, fold points into surrounding prose rather than deleting them. The content should do the work, not the formatting.

# Blog - Claude Memory

## Voice
- Rob's posts are compressed from ~25 mins of talking/dictation
- Keep the spoken quality - don't over-polish
- No melodrama
- No short sentences for dramatic effect - understated British tone, not punchy
- Avoid AI tells: "Not X because Y" + em dash, excessive hedging
- Push after every change - easier to review in browser

## Drafting workflow
1. Save raw transcript to `_notes/` first
2. Draft the post
3. **Before publishing: brutal self-edit pass**
   - What is the ONE core argument?
   - Cut anything that doesn't directly serve it
   - Interesting ≠ essential
   - Don't be polite about your own output
   - The raw transcript is preserved - nothing is truly lost
4. Images: ask Rob before making one. Not every post needs an image. When one would obviously help, ask him first whether he has something in mind (he is online all day chasing AI things and often has a screenshot, a tweet or a chart already) or wants a hand-drawn diagram. Diagrams only where the post describes a structure the reader has to hold in their head; recipe and generators in `_notes/drawings/`, captions are labels not slogans. If he says generate, use gpt-image-1.5 via API (medium quality, no text/letters), and vary the palette from post to post. API key is in `~/.config/openai/key` (not in the env).
5. Set publish times in GMT/UTC, not local UK time. Rob is in the UK; during BST, local time is UTC+1. Jekyll/GitHub Pages will not publish posts dated after the current UTC time, so use a clearly-past UTC timestamp such as `09:00:00 +0000` unless deliberately scheduling a future post.
6. Push

## Common issues
- Too many threads for word count (James Thompson feedback)
- Tailoring examples, Bangladesh suits etc = tangent, cut it
- Garden path sentences - use "when" as hinge to clarify

## Files
- `_notes/` - raw transcripts, fragments (tracked in git since 2026-07-06; public like the rest of the repo)
- `_posts/` - published posts
- `backlog.md` - ideas tracker
- `assets/images/` - post images

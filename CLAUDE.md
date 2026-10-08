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
4. Images: every post opens with something beautiful, a real painting rather than a generated image (Rob, 8 Oct 2026: generated images "were always the wrong tack"; relevance to the post is optional). Source: public-domain works on Wikimedia Commons (artist dead more than 70 years, licence shows Public domain). The paintings already used, listed in `_notes/paintings.md`, define the taste: pick in the same spirit, vary artist and palette, and never reuse a painting. Add every new one to that register. Download via the Commons API at about 1600px, crop portrait works to a 3:2 detail, save as webp under `assets/images/`, and put an italic caption line under the image: *Artist, Title (year), detail. [Wikimedia Commons](file page)*. If Rob has an image in mind he will say; ask when unsure. Diagrams only where the post describes a structure the reader has to hold in their head; recipe and generators in `_notes/drawings/`, captions are labels not slogans.
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

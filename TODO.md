# Audit TODO — 2026-07-06

Findings from a holistic pass. Discuss before executing.

## Bugs

- [x] **Pre-push future-date check is dead on Linux.** `.githooks/lib/post-checks.sh` uses BSD `date -j -f`, which fails on Ubuntu, so `check_not_future` silently skips every post. The repo's own test suite confirms it: 4 of 16 tests fail, all future-date cases. Fix the parse portably (GNU `date -u -d` with BSD fallback) and get `.githooks/test/test-post-checks.sh` green.
- [x] **Duplicate `<title>` in every page head.** `_layouts/default.html:6` emits a manual title and `{% seo %}` on the next line emits a second one. Pick one (drop the manual line, or pass `{% seo title=false %}`).

## Data loss (needs a decision, not just a fix)

- [x] **The `_notes/` corpus is gone.** `backlog.md` links 7 notes files (`intelligence-inside-apps.md`, `2026-02-18-dogwalk-transcript-synthesis.md`, etc.); none exist locally, in git (gitignored, so no history), or in context-store. Only 2 transcripts survive. CLAUDE.md's drafting workflow rests on "the raw transcript is preserved — nothing is truly lost", which is currently false. Decide where notes should durably live (context-store seems the natural home, with `_notes/` a symlink or working copy), and mark the dead backlog links so future sessions don't chase them.

## Hygiene

- [x] **`backlog.md` and `CLAUDE.md` are served on the live site** (both return 200 on rob137.github.io). They're public on GitHub anyway, so no secret is leaking, but the site shouldn't serve working files. Add both to the `exclude:` list in `_config.yml`.
- [x] **README is day-one boilerplate.** References `~/sandpit/blog`, includes a markdown tutorial and GitHub Pages setup instructions for a site that has 89 published posts. It's the public face of the repo — rewrite terse (purpose + non-obvious conventions).
- [x] **Skill file duplicated.** `.agents/skills/final-pass/SKILL.md` and `.claude/skills/final-pass/SKILL.md` are identical regular files; they will drift. Symlink one to the other. *(Resolved per Rob: one file, no symlink — `.agents` copy deleted, `.claude` canonical.)*
- [x] **7 unreferenced images in `assets/images/` (~1.2M).** Mix of old chart outputs from `_scripts/progress_charts.py` and orphaned post art (`temple-machine.webp`, `average-is-over-cover.jpg`, ...). Delete; git history keeps them.
- [x] **Two feeds, one job.** Hand-rolled `feed.xml` plus the `jekyll-feed` plugin in `_config.yml`. The custom file wins (plugin skips when the file exists) so nothing is broken, but pick one. Boring option: keep the custom file, drop the plugin line.
- [x] **`memories.md` in `.gitignore` but no such file exists** — line can go.

## Content flags (Rob's call, not mine)

- [ ] `now.md` says "Last updated: March 2026" — four months stale for a now page. **Plan: Claude grills Rob (~8 questions, one at a time) then updates. Deferred to after compact.**
- [ ] **Check the Mac for the 7 missing `_notes/` files** (backlog.md references macOS paths, so the notes may live there) — commit them if found.
- [x] `_scripts/generate_images.py` hardcodes the January batch of post prompts; it reads as a one-shot fossil, but CLAUDE.md still points at the gpt-image workflow. Fold anything worth keeping into a small reusable script or note it as historical.

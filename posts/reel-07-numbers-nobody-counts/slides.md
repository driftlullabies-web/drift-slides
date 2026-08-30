# REEL 07 - Numbers Nobody Counts

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Inspired · CTA **Save**
Slot: **Wed Sep 2, AM 9:30 ET** · Hook: fresh · mechanism 3 The Number Nobody Counted
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`

Part of the **daily-video ramp** (Ben, 2026-08-27) — the format went from 1–2/week to one video a
day after REEL 03 returned 15,728 views and 341 shares. Drafted, reviewed by Ben over two rounds,
and locked 2026-08-27. Draft history: `Automation Engine/_reel_drafts/`.

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset. Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The numbers of the first year nobody thinks to count
items:
  - Close to 5,000 ounces of milk before their first bite of solid food
  - Around 2,500 diapers before they reach their first birthday
  - About 100 little tub baths, before the big tub fits them
  - 365 bedtime books, one a night if you're lucky
turn: No one keeps the count when you're in the middle of it.

## Notes

**Every number in this card was fact-checked on 2026-08-27 at Ben's request** — his first draft had
three he flagged himself, and all three were wrong:
- *10,000 oz of milk before their first solid food* → breastfed intake averages ~25 oz/day and is flat
  from 1–6 months, so birth→solids is ~4,500–5,000 oz. 10,000 is roughly the FIRST YEAR. Corrected to 5,000.
- *300 baby tub baths* → newborns are bathed 2–3x/week, and they are in the big tub by ~6–9 months.
  That is ~100, not 300.
- *700 naps / 700 books* → 700 naps is LOW (3–4/day early, 2–3 by twelve months = over 1,000), and naps
  and books were conflated: one book per BEDTIME is ~365/year. Split; the book number kept.
- Also corrected, and it was Claude's own error: *1,100 diapers* → ~2,500 in the first year.
Ben then cut the hedge "About" from the books line — correct, 365 is exact arithmetic, not an estimate.
Sources: kellymom.com milk calculator · CDC infant formula feeding · Pampers nap schedules.

## Caption
Written under Ben's 2026-08-27 rule: **do not recap on the card what she is already reading on the
card.** The caption opens on a keyword-forward line, then goes straight to the ask so it sits above
TikTok's fold. See `caption.txt`.

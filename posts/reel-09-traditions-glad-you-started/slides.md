# REEL 09 - Traditions Glad You Started

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Tradition · CTA **Website (link in bio)**
Slot: **Fri Sep 4, AM 9:30 ET** · Hook: fresh · engine 2 weekly rhythm
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`

Part of the **daily-video ramp** (Ben, 2026-08-27) — the format went from 1–2/week to one video a
day after REEL 03 returned 15,728 views and 341 shares. Drafted, reviewed by Ben over two rounds,
and locked 2026-08-27. Draft history: `Automation Engine/_reel_drafts/`.

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset. Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The little traditions you'll be glad you started this year
items:
  - Pancakes every Saturday, and add in a special ingredient every week
  - A photo in front of the same tree, first day of every season
  - Soup on the first properly cold night of the year
  - A sweet treat after every check-up, just for you until they are old enough to share
turn: Start one now and they'll think it's just what you do.

## Ben's wording — do NOT rewrite (per Ben's review)

- **items 1 and 2** is Ben's, verbatim, from the 2026-08-27 review round.
- **the caption** is Ben's, verbatim, from the 2026-08-27 review round.

The linters report his lines and exclude them from their exit codes. Check this file before
"improving" any line in the card.

## Notes

⚠️ **This post carries the website ask, which the Tradition lane used to ban outright.**
Ben RETIRED that ban on 2026-08-27 after overriding it twice in two weeks (TRAD 03 on Aug 24 was the
first). See `Tradition Post/tradition-series-brief.md` §5 and drift-tradition-series. The reasoning
survives as restraint: the song sits at the END of a real list of real traditions, as one more of
them, never the premise.

⚠️ Rendered on FLAT CREAM, not eucalyptus — `drift_reel.py` has no lane-background path. Flagged for
Ben; if Tradition reels should carry BG_EUCA that is a renderer change, not a copy change.

⚠️ 71 words, over the §2 budget. Ben's item 4. Reported, excluded from the exit code, not trimmed.

**Two earlier items were cut because they duplicated TRAD 03 VERBATIM** — "Friday pizza eaten
outside" and "a walk after dinner, same route" are its items 2 and 3, and TRAD 03 published the same
morning this was drafted. Ben caught both. See drift-item-collision-check.

## Caption
Written under Ben's 2026-08-27 rule: **do not recap on the card what she is already reading on the
card.** The caption opens on a keyword-forward line, then goes straight to the ask so it sits above
TikTok's fold. See `caption.txt`.

# REEL 11 - Advice You Can Just Not Take

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Warmth · CTA **Share**
Slot: **Mon Sep 7, AM 9:30 ET** · Hook: #85 READY
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`

Part of the **daily-video ramp** (Ben, 2026-08-27) — the format went from 1–2/week to one video a
day after REEL 03 returned 15,728 views and 341 shares. Drafted, reviewed by Ben over two rounds,
and locked 2026-08-27. Draft history: `Automation Engine/_reel_drafts/`.

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset. Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The newborn advice you're allowed to just not take
items:
  - That you're holding them too much, usually from someone who isn't
  - That they should be on a schedule, from a person not here at 4am
  - That you'll regret not sleeping now, as though that were a choice
  - That you HAVE to put them down drowsy but awake
turn: You can nod, say thanks, and do none of it.

## Ben's wording — do NOT rewrite (per Ben's review)

- **item 4** is Ben's, verbatim, from the 2026-08-27 review round.

The linters report his lines and exclude them from their exit codes. Check this file before
"improving" any line in the card.

## Notes

Scheduled the week AFTER the others: Ben's constraint is ≥7 days from REEL 05, and the widest gap
inside one week is 6 days — so this lane pair cannot both run in the same week. Mon Aug 31 → Mon Sep 7.

Item 4 replaced after Ben's note: the original ("that everyone else's baby is already doing more")
is a worry, not advice, so it did not belong in a list of ADVICE she is allowed to decline. His
replacement adds the emphasis on HAVE.

## Caption
Written under Ben's 2026-08-27 rule: **do not recap on the card what she is already reading on the
card.** The caption opens on a keyword-forward line, then goes straight to the ask so it sits above
TikTok's fold. See `caption.txt`.

# REEL 06 - Moments No One Thinks To Save

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Keepsake · CTA **Share**
Slot: **Tue Sep 1, AM 9:30 ET** · Hook: #2 READY
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`

Part of the **daily-video ramp** (Ben, 2026-08-27) — the format went from 1–2/week to one video a
day after REEL 03 returned 15,728 views and 341 shares. Drafted, reviewed by Ben over two rounds,
and locked 2026-08-27. Draft history: `Automation Engine/_reel_drafts/`.

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset. Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The newborn moments no one thinks to save
items:
  - The way they root against your shoulder, still mostly asleep
  - Their hand closing on nothing, like a slow wave
  - The way they go still mid-cry, the second you start humming
  - The face they make finding the bottle, half a sigh and half a word
turn: These are the moments that sometimes miss the photos… and they go first.

## Ben's wording — do NOT rewrite (per Ben's review)

- **item 3** is Ben's, verbatim, from the 2026-08-27 review round.
- **turn** is Ben's, verbatim, from the 2026-08-27 review round.

The linters report his lines and exclude them from their exit codes. Check this file before
"improving" any line in the card.

## Notes

⚠️ Rendered on FLAT CREAM, not the Keepsake kraft texture. The texture is a square-slide treatment
(drift-keepsake-texture-experiment); the reel renderer has no texture path and the IG port was
explicitly rejected (drift-ig-reel-keepsake-gap). Do not "fix" this.

## Caption
Written under Ben's 2026-08-27 rule: **do not recap on the card what she is already reading on the
card.** The caption opens on a keyword-forward line, then goes straight to the ask so it sits above
TikTok's fold. See `caption.txt`.

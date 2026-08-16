# Reel 02 - Newborn Sounds Youll Forget

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Keepsake · CTA Save
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`
Source: adapted from carousel `01 - Newborn Sounds Youll Forget` (5.96% ER, published Jul 27–Aug 2 —
at/above the Keepsake lane average for that window, ≥3 weeks old as of this run).

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset (not an image carousel). Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The tiny newborn sounds you'll forget faster than you expect
items:
  - The squeaky grunts while they settle
  - The sigh right after a feed
  - The gulp of a 3am bottle
  - The cry that's already changing
  - The coos before real words
turn: You'll remember the photos. The sounds go quietly, first.

CTA = Save (caption ask). NO website ask — a reel has no closing card, so it structurally
cannot carry the LOCKED website CTA (reel-copy-spec §7.4).

Added 2026-08-16 to satisfy the new minimum-2-reels/week standing rule (Ben). This is the SECOND
of this week's two reels — see week-2026-08-17-plan.md for which row it swaps.

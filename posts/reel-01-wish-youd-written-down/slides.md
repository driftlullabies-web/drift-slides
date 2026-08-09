# Reel 01 - Wish Youd Written Down

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Keepsake · CTA Save
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`
Source: adapted from carousel `05 - Wish Youd Written Down` (7.44% ER — best post of Jul 27–Aug 2).

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset (not an image carousel). Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The tiny newborn moments tonight you'll wish you'd written down
items:
  - The weight of them asleep on your chest, heavier than you expected
  - The tiny sigh right at the moment they finally give in to sleep
  - A whole hand wrapped around one of your fingers
  - The 2am quiet that belongs to nobody but the two of you
turn: You think you'll remember. These are the ones that go first.

CTA = Save (caption ask). NO website ask — a reel has no closing card, so it structurally
cannot carry the LOCKED website CTA (reel-copy-spec §7.4).

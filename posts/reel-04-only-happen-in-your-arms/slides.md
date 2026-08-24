# REEL 04 - Only Happen In Your Arms

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Keepsake · CTA **Save**
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`
Source: adapted from carousel `33 - Only Happen In Your Arms` (Mon Aug 10 2026, **5.56% ER vs the
5.49% Keepsake lane average for Aug 10–16** ✓).

⚠️ **Recency exception, documented.** §7.3 wants a source ≥3 weeks old; this one is **14 days**. See
REEL 03's note — a strict read of §7.3 yields no eligible sources at all while the library is this
young. Flagged in the digest.

**Source item deliberately dropped:** post 33's item 03 was *"How they root toward your voice before
their eyes open."* Post 53 (Aug 20, the voice they can already pick out) was an entire carousel about
voice recognition, so that item sat too close cross-week. Replaced with the sway beat.

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset. Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The parts of your newborn's day that only happen in your arms
items:
  - They go quiet mid-cry, the second you lift them
  - The stretch-and-settle they save for your chest, and nowhere else
  - The way they curl in tighter, the second you start to sway
  - The warm shape in the blanket, still there after you set them down
turn: None of it happens in the crib. That isn't a problem to fix.

House shape (check_reel_copy.py): 4 items · 47–66 chars · 9–13 words · spread 19 · every item wraps
to two lines and carries a payoff clause after a comma · 69 words total.

CTA = **Save** (caption ask), held against REEL 03's Share the same week so the format carries both
asks and the difference is readable.

NO website ask — a reel has no closing card (reel-copy-spec §7.4). Counts in neither 3a counter.

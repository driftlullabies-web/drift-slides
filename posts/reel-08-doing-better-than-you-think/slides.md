# REEL 08 - Doing Better Than You Think

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Warmth · CTA **Share**
Slot: **Thu Sep 3, AM 9:30 ET** · Hook: #40 READY
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`

Part of the **daily-video ramp** (Ben, 2026-08-27) — the format went from 1–2/week to one video a
day after REEL 03 returned 15,728 views and 341 shares. Drafted, reviewed by Ben over two rounds,
and locked 2026-08-27. Draft history: `Automation Engine/_reel_drafts/`.

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset. Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The things you're doing better than you think, new mom
items:
  - You picked them up every time they needed you, even when you were told not to
  - You learned their cry so well, you stopped having to guess what they wanted
  - You kept going on a night when you had nothing left to give, and nobody saw
  - You worried you were wrong, which is why you weren't
turn: None of that shows up anywhere. It still happened.

## Ben's wording — do NOT rewrite (per Ben's review)

- **items 1, 2 and 3** is Ben's, verbatim, from the 2026-08-27 review round.

The linters report his lines and exclude them from their exit codes. Check this file before
"improving" any line in the card.

## Notes

⚠️ **This card is 75 words, over the 45–70 budget (§2), and that is Ben's call.** His three rewrites
lengthened items 1–3. He was shown the rendered card beside a compliant one and kept his wording.
`check_reel_copy.py` reports it and excludes it from the exit code via the `per Ben's review` rule.
Do not trim it to satisfy the linter.

The headline:item ratio guard (added the same day) brings the balance back — this card renders at
55px headline / 32px items = 1.72, inside the shipped band. Balance and density are independent;
this one is balanced but still long.

## Caption
Written under Ben's 2026-08-27 rule: **do not recap on the card what she is already reading on the
card.** The caption opens on a keyword-forward line, then goes straight to the ask so it sits above
TikTok's fold. See `caption.txt`.

# REEL 20 - The Sentence In Your Head (one-card)

Format: 6s single-card reel, 1080×1920, built by `Automation Engine/reels/drift_reel_nicu.py`
from `card.json`. Lane **Inspired**. Slot **AM** (daily reel slot).

**Runs Wed 9/23** — **27 days** past the original, the closest to the 30-day floor of the three.
No CTA (`"pill": null`).

## Why this exists — a FORMAT re-run, not a repost

INSP 02 published Thu 8/27 and is the **best post the lane has ever had**: 9,992 views, 12.13% ER,
22.9 shares per 1k, 12.3s average watch. Per Ben's 2026-09-09 call it re-runs as a one-card reel.
The reasoning, the risk, and the read-it-against-the-other-two caveat are all set out in
`REEL 19 - I See You (one-card)/slides.md` and apply identically here.

## The strikethrough is the whole post

This card is the only one in the set that needs a treatment `drift_reel_nicu.py` did not have.
The mechanism is a **reframe**: a sentence she is already saying to herself, crossed out, and the
truer sentence underneath it. Ben, seeing a first pass that just italicised the second line:
*"don't we need to cross out some of them?"*

He was right, and I should have built it rather than shipping the weakened version — a port to a new
renderer that quietly drops a treatment the new renderer doesn't implement is the recurring failure
in [[drift-new-lane-blanks-the-workbook]]. `~~strikethrough~~` now exists as a real style
(`STRIKE`), stroked once per continuous run rather than per word, at 10% of ascent above the
baseline. Per-word strokes read as five underlines; that was the first attempt.

## Card copy

```
The sentence in your head at 4am

~~He just cries and I can't figure out why.~~
_I'm the one he's crying for._

~~All I did today was hold him.~~
_I was the safest place he's ever been._

~~I didn't get a single thing done.~~
_I did the one thing that can't be done later._

~~I don't even know what day it is.~~
_I know exactly how his head smells._

~~I'm not doing this right.~~
_He doesn't know there's a right way. He only knows mine._
```

This is a **five**-pair card where the published carousel ran across five slides. Nothing was cut.

## Caption

Rewritten — the published caption listed the reframes as prose, which is now a transcript of the
card. The new one answers the objection the card provokes and never addresses: *isn't the rewrite
just telling myself something nicer?* No — the first sentence was the lie, it merely arrived first.

## Assets

- `card.png` · `reel.mp4` — 6.000s · 180 frames · 1080×1920, decoded not checksummed.

⚠️ Flat `BG_MIST`; no photo-background path exists for reels.

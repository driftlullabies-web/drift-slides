# REEL 19 - I See You (one-card)

Format: 6s single-card reel, 1080×1920, built by `Automation Engine/reels/drift_reel_nicu.py`
from `card.json`. Lane **Inspired**. Slot **AM** (the daily reel slot — this does NOT go in Mid;
a reel in the Mid carousel slot would give that day three videos and break the
AM reel · Mid carousel · PM series reel shape).

**Runs Wed 9/16.** No CTA (`"pill": null`) — the Inspired lane ends on the poem by design.

## Why this exists — a FORMAT re-run, not a repost

INSP 07 published Tue 8/25 as a 3-slide carousel and is the lane's third-best post: 7,586 views,
9.15% ER, 13.3s average watch. This ships the identical poem as one card in a 6s loop.

**Ben's call, 2026-09-09**, after being shown that every one of these lands inside his 30-day
repost floor: run INSP 07 / 02 / 01, hold INSP 09. This one is **22 days** past its original — under
the floor, and taken deliberately, because:

- The container is genuinely different. [[drift-keepsake-share-desert]] measured the same lane
  getting **2.39× the reach** as a reel versus a carousel; format is the lever this is pulling.
- The floor exists to stop the same *asset* hitting the same followers twice. A 6s loop and a
  three-swipe carousel are not the same asset, though the words are.

⚠️ **But the words ARE the same, and that is the risk being taken.** If this underperforms its
original, the honest read is audience fatigue, not a bad format — do not conclude the one-card reel
doesn't work off this post alone. Read it against REEL 20 and REEL 21, which sit at 27 and 29 days.

## Card copy

Rendered from `card.json` — that file is the source of truth, this is a transcript for review.

Headline: **I see you**

```
3:40am. You don't turn the light on anymore — you know the room by feel.

You do the bounce. Then the other bounce. Then the one that actually works.
_The one you invented and could never explain to anyone._

Same song. Same four lines. Off-key in the same place every night.
She doesn't care. She will never care.
_And one day that off-key part will be the whole song to her._

She won't remember a single one of these nights.
_You'll remember all of them._

*I see you.*
```

Last line is Ben's, 2026-09-09 (was "She won't remember any of it"). The rewrite turns a fact about
the baby into a verdict about her, which is the register this lane closes in.

## Caption

Rewritten for the reel. **The published carousel's caption transcribed the whole poem** — correct
when the poem was spread over three slides that scroll past, wrong now that all of it is on one
card, and it would fail `check_caption_overlap.py`. The new one adds the thing the card doesn't
say: that the hard part is the absence of an audience, not the hour.

## Assets

- `card.png` — the still, 1080×1920
- `reel.mp4` — 6.000s · 180 frames · 1080×1920 (decoded with ffprobe, not checksummed —
  [[drift-checksums-arent-validity]])

⚠️ Renders on flat `BG_MIST` (#DCE6EC). No reel renderer has a photo-background path, so this does
not carry the lane's usual photo treatment. Renderer gap, tracked in
[[drift-inspired-song-poems-die]].

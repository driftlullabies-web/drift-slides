# Collecting Ideas - Day 8

Format: **REEL** (single-image 3.5s loop, 1080x1920 MP4) · bg honey/vanilla (#F3EBD6) · lane Collecting Ideas · CTA on-card  ⚠️ **SUPERSEDED — ships as a PHOTO (slide-1.png), see the note at the foot of this file.**
Renderer: `Automation Engine/_render_collecting_ideas.py` · Bank: `Day X of collecting ideas/ideas-bank.json`

## Card
hook: Day 8 of collecting ideas for your baby's lullaby.
reframe: A memory to put into a verse:
idea: The first night you fell asleep on my chest.
ask (on-card CTA): Save this for when you're ready to write your lullaby

Rebuild with:
    python3 "Automation Engine/_render_collecting_ideas.py" --day 8 --out "Automation Engine/queue/Collecting Ideas - Day 08"


---

## ⚠️ FORMAT CHANGED 2026-09-11 — this day ships as a PHOTO, not a 3.5s reel (Ben)

> *"the day X series is doing terrible. this next week I would like them rendered as a
> photo/single slide so I can put a whole song with it, which may get longer retention."*

**Asset for this post is `slide-1.png` (1080x1920), NOT `reel.mp4`.** The card artwork is unchanged —
it was always a single-card design, so nothing was recomposed; the still is the same frame the video
was built from.

⚠️ **PHASE 2 / THE QUEUE-BATCH MUST ATTACH IT AS AN `image` ASSET.** The folder still contains the
old `reel.mp4` because deletes are blocked on this volume. **The push must `rsync --delete` a
staging copy that excludes `reel.mp4`**, so the repo folder for this day ends up with `slide-1.png`
only — otherwise the batch can auto-detect the video and post the 3.5s loop again, silently undoing
the change.

**Why this is the right lever, from the numbers** (`insights.md`, 2026-09-11): shortening the video
from 6.0s to 3.5s raised completion from ~48% to ~90% **and moved views by nothing** (342 → 320).
The container length was never the constraint. A photo post holds the frame for the full length of
whatever sound is attached, which is a different mechanic — Ben attaches a whole song at notification
time and the watch window stops being capped by the asset.

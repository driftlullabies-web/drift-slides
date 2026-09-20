# Collecting Ideas - Day 16

Format: **PHOTO** (single card, `slide-1.png`, 1080x1920) · bg honey/vanilla (#F3EBD6) · lane Collecting Ideas · CTA on-card
Renderer: `Automation Engine/_render_collecting_ideas.py` · Bank: `Day X of collecting ideas/ideas-bank.json`

## Card
hook: Collecting ideas for your baby's lullaby (part 16)
reframe: A little detail to include:
idea: The way they turn their head toward your voice from across the room.
ask (on-card CTA): Save this for when you're ready to write your lullaby

Rebuild with:
    python3 "Automation Engine/_render_collecting_ideas.py" --day 16 --out "Automation Engine/queue/Collecting Ideas - Day 16"


---

## ⚠️ 2026-09-17 — RENAMED "Day N" -> "(part N)", AND THIS DAY SHIPS AS A PHOTO

> *"For the Day X series — they should be images now, not reels. And can we change it from Day X to
> (part X) at the end. That way we don't HAVE to do one a day next week. We can space them out. I do
> like having them every day for now because it takes pressure off content creation. It's easy
> content."* — Ben, 2026-09-17

**Two separate changes, both applied here.**

**1. The label.** `Day 15` -> `Collecting ideas for your baby's lullaby (part 15)`. The old label made
a promise about **cadence** that the series never needed to make: "Day 15" tells a reader the last one
was yesterday and the next is tomorrow, so any gap reads as a missed post. That quietly turned the
cheapest content on the account into a daily obligation. "(part 15)" keeps the sequence and drops the
clock. **Nothing about the schedule changes this week** — the series still runs 7/7 at PM 7:30,
because Ben's own reason for that stands (it takes pressure off everything else). What changed is
that skipping a day next week now costs nothing.
⚠️ **The numbering CONTINUES rather than restarting** — part 15 follows Day 14. The reader is already
fourteen in, and resetting to 1 would throw away the only thing the label is for. There is a visible
seam at the changeover; that is the cheaper of the two costs.

**2. The asset is `slide-1.png` (1080x1920), NOT `reel.mp4`.** Days 08-14 were switched to the photo
format on 2026-09-11 and days 15-21 were missed — they were still 3.5s reels on disk, which would
have silently undone the change mid-week. The still is rendered from the same card artwork; nothing
was recomposed.

**The measurement that justifies it** (`insights.md`, 2026-09-16): days 04-07 as 3.5s reels drew
**12-23 views each**; **day 08 as a photo drew 301** — a 15-25x step change on the first day of the
new container, and the only variable that moved. ⚠️ Watch time did **not** move (2.7s on the photo
against 2.1-3.4s on the reels), so the "attach a whole song and get long retention" half of the
thesis has not landed yet. n=1 on the photo; days 09-14 settle it.

⚠️ **PHASE 2 / THE QUEUE-BATCH MUST ATTACH IT AS AN `image` ASSET.** The folder still contains the old
`reel.mp4` because deletes are blocked on this volume. **The push must stage with
`rsync --delete-excluded`, not `--exclude`** — `--exclude` *protects* the destination copy, which is
exactly what left all seven mp4s in the repo last time and would let the batch auto-detect a video and
re-post the 3.5s loop.

⚠️ **The queue folder name and the GitHub slug stay `Collecting Ideas - Day NN` /
`posts/collecting-ideas-day-NN`.** Those are internal identifiers the reader never sees, and days
01-14 are already pushed under them; renaming would orphan every existing path in a repo where deletes
are blocked. The rename is reader-facing only — the card and the caption.

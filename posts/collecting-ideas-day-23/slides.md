# Collecting Ideas - Day 23

Format: **PHOTO** (single card, `slide-1.png`, 1080x1920) · bg honey/vanilla (#F3EBD6) · lane Collecting Ideas · CTA on-card
Renderer: `Automation Engine/_render_collecting_ideas.py` · Bank: `Day X of collecting ideas/ideas-bank.json`

## Card
hook: Collecting ideas for your baby's lullaby (part 23)
reframe: A moment worth remembering:
idea: The first time you looked at me like you knew exactly who I was.
ask (on-card CTA): Save this for when you're ready to write your lullaby

Rebuild with:
    python3 "Automation Engine/_render_collecting_ideas.py" --day 23 --out "Automation Engine/queue/Collecting Ideas - Day 23"


---

## 2026-09-23 — RENAMED "Day N" -> "(part N)" AND SWITCHED TO PHOTO (the lane-wide sweep)

Ben's two standing calls, applied to the whole remaining bank rather than one week at a time:

1. **Label** (2026-09-17): *"can we change it from Day X to (part X) at the end. That way we don't
   HAVE to do one a day next week. We can space them out."* "Day N" promised a cadence the series
   never needed to make; "(part N)" keeps the sequence and drops the clock.
2. **Container** (2026-09-11): ships as **`slide-1.png` (1080x1920)**, NOT `reel.mp4`, so a whole
   song can be attached at notification time. Measured result: days 04-07 as 3.5s reels drew 12-23
   views each; day 08 as a photo drew **301**.

⚠️ **WHY THIS FILE IS BEING TOUCHED WEEKS BEFORE ITS SLOT.** Days 22-50 were already pushed to
GitHub as 3.5s reels carrying the old label. The queue-batch auto-detects a video from what is in
the repo, so every one of them was a **scheduled regression with a date on it** — day 22 would have
silently reverted both decisions on 2026-09-28. The 2026-09-11 change fixed only the days in that
week's plan; nothing looked at the ones already sitting in the repo.

**The generalisable rule: a format or label change is a property of the LANE, not of a week. Sweep
the whole bank, and mirror the push so git records the DELETION of the stale asset** — `rsync
--exclude reel.mp4` does not remove it, `--exclude` *protects* the destination copy.

Folder name and GitHub slug stay `Collecting Ideas - Day NN` / `posts/collecting-ideas-day-NN` —
internal identifiers the reader never sees, and days 01-21 are already pushed under them.

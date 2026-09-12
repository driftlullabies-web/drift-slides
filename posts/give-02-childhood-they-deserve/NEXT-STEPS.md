# GIVE 02 — ✅ SCHEDULED. Nothing left to do.

**Post B of the buy-one-give-one manifesto.** Version A is
`../GIVE 01 - Things We Cant Fix/`, finished and deliberately held.

| step | state |
|---|---|
| Render card + 6s mp4 | ✅ `card.png` · `reel.mp4` — 180 frames / 6.01s / 1080x1920 / h264, full decode clean |
| Copy gates | ✅ `caption_guard.py` clean · `check_caption_overlap.py` 1 clean / 0 failing |
| Push to GitHub | ✅ `posts/give-02-childhood-they-deserve` (2026-09-12) — the 4 files byte-match locally |
| Buffer post | ✅ `6aa556243da5f871532f2bef` |
| Story teaser | ✅ `stories/2026-09-20.png` rendered and pushed |

**Scheduled: Sun 9/20, 9:30am ET (13:30Z), TikTok only, notification**, pointing at
`https://raw.githubusercontent.com/driftlullabies-web/drift-slides/main/posts/give-02-childhood-they-deserve/reel.mp4`

It takes the AM slot REEL 26 vacated, which **restores one-video-per-day** and puts the week of
Sep 14 at **18 scheduled** with the product-forward group at its **cap of 5**.

⚠️ **Queued by hand — the queue-batch must not re-serve it.** Same pattern as NICU 01; both the plan
row and the `schedule-2026-09-14.json` entry say so.

⚠️ **The teaser renders on CREAM, the card is seafoam.** `story_teasers/drift_story.py` has no
seafoam token and `LANE_BG` has no `give`/`nicu` key, so both offer-lane teasers fall back to cream.
Cosmetic, and consistent with NICU 01's already-pushed teaser — worth adding a seafoam token before
the lane's third post rather than re-cutting a pushed asset.

## To change the copy after this point

Re-render from `card.json`, re-encode, re-push, then **edit the existing Buffer post** — do not
create a second one:

    cd "Automation Engine/reels" && python3 drift_reel_nicu.py \
        --json "../queue/GIVE 02 - Childhood They Deserve/card.json" \
        --out "../queue/GIVE 02 - Childhood They Deserve"
    bash "Automation Engine/push-to-github.sh" "GIVE 02 - Childhood They Deserve" "posts/give-02-childhood-they-deserve"

⚠️ If a `create_post` ever 400s with "already scheduled", **LIST before retrying** — it can fail AND
have created the post (memory `drift-buffer-create-post-false-error`).

## One open copy note

*"bring a little more light into their **world**"* sits a few lines above *"show the **world** what a
bunch of parents…"*. Changing the first to **"their lives"** clears the echo. Ben has seen this
flagged and not acted on it; it is a one-word edit through the path above.

## Caption (as queued)

    A personalized lullaby for your baby, and one for a family who needs it.

    Right now those go to families in the NICU. You answer a few questions about your little one —
    their name, what settles them — and that's what their song is made from.

    Link in bio. 🤍

    #newmom #nicu #babylullaby #momtok #fourthtrimester

Card: 107 words · headline 62px · body 35px · `BG_SEAFOAM_SOFT` · `vcenter` · prose layout.
Reasoning: memory `drift-nicu-offer-layout` · `drift-prose-card-overflow-repair`.

# GIVE 01 — ⏸ FINISHED AND HELD. Not pushed, not scheduled.

**Post A of the buy-one-give-one manifesto**, the *"things in this world we can't fix"* hook.
Ben's call 2026-09-12: *"we are going to do both"* … *"schedule post B while keeping A as finalized
card ready to post another time."* **B is scheduled for Sun 9/20. This one waits.**

| step | state |
|---|---|
| Render card + 6s mp4 | ✅ `card.png` · `reel.mp4` — 180 frames / 6.01s / 1080x1920 / h264, full decode clean |
| Copy gates | ✅ `caption_guard.py` clean · `check_caption_overlap.py` 1 clean / 0 failing |
| Push to GitHub | ⏸ **deliberately not pushed** — nothing in the repo, nothing for a batch to find |
| Buffer post | ⏸ **none** |

## To ship it, when it gets a slot

1. Give it a row in that week's `week-YYYY-MM-DD-plan.md` **and** an entry in the matching
   `run_sheets/schedule-YYYY-MM-DD.json` — `check_plan_matches_posts.py` compares the two in order.
2. Push, from `Automation Engine` (works from a Cowork device shell now, no Terminal needed):

        bash push-to-github.sh "GIVE 01 - Things We Cant Fix" "posts/give-01-things-we-cant-fix"

3. Then create the Buffer post against
   `https://raw.githubusercontent.com/driftlullabies-web/drift-slides/main/posts/give-01-things-we-cant-fix/reel.mp4`
   — **not before the push**, Buffer probes the video at create time and a 404 fails the call.
4. Render + push its story teaser (`story_teasers/render_todays_story.py --date <that Sunday>` reads
   the AM row out of the plan, so step 1 has to be done first).
5. It is **product-forward and carries a website ask**, so it spends one of the week's 5 and one of
   the 8. Mark it TikTok-only in its `slides.md` (already done) or `build_ig_reels.py` will take it.

## ⚠️ Two things before you pick a week

1. **A and B are the same argument.** Never the same week, and put real distance between them — the
   closing movement (*"Every time you buy an original lullaby, we create one for a family in need"*)
   is **verbatim identical** in both cards.
2. **The giving promise still has no mechanism.** Redemptions are a fixed 5/day through the NICU
   code; a day where purchases exceed five breaks the one-for-one claim this card makes until the
   cap is raised. Ben 2026-09-12: manual tracking for now.

## Caption (written, gated, unused)

    Personalized baby lullabies, with one given away for every one bought.

    The families on the receiving end are in the NICU right now. You answer a few questions about
    your little one, and that's what their song is made from.

    Link in bio. 🤍

    #newmom #newbornlife #babylullaby #momtok #fourthtrimester

Card: 96 words · headline 62px · body 36px · `BG_SEAFOAM_SOFT` · `vcenter` · prose layout.
Reasoning: memory `drift-nicu-offer-layout` · `drift-prose-card-overflow-repair`.

# NICU 01 — ready to push, NOT yet in Buffer

⚠️ **UPDATED 2026-09-09 — two things below have changed. Read this block before the rest.**

1. **The promo code is LIVE.** Ben confirmed it. Step 1 below is DONE; it is kept only as the
   record of what was run.
2. **It is no longer a dateless draft.** Ben: *"please put the nicu social post on the schedule
   where it fits."* Requested slot: **Mon 9/14, AM (9:30am ET), TikTok only.** Still no IG variant
   — the derived `ig/` asset path has the unresolved daily-video-ramp issue and this post is not
   the place to debug it.

   Not the week of Sep 7: every one of its 21 slots is taken at the 3/day ceiling, and its
   product-forward group is already at **5 of 5**. NICU is product-forward (subject is the song,
   and it carries an offer), so it would make 6. Mon 9/14 is the first free reel slot; that week
   sits at 1 of 5. Full reasoning in `pending-posts.md`.

~~Ben's call 2026-09-08: **Buffer DRAFT, no date, TikTok only**~~ — superseded by the above.

## Two things have to happen first, in this order

**~~1 · Deploy the NICU promo code.~~ ✅ DONE 2026-09-09.** For the record, this is what it took —
from your Terminal, in `littlelullaby-backend`:

    git push
    npx prisma migrate deploy
    npx prisma generate
    npm run db:seed-promo          # expect: ✓ NICU — uncapped, 5/day, 10 credits, 0 redeemed

(`prisma generate` fails on your Mac — binaries.prisma.sh is 403 through the egress
allowlist — so it has to run in the deploy environment. See memory `promo-code-daily-cap`.)

**2 · Push the asset.** ⬅️ **THIS IS THE ONLY THING STILL BLOCKING.** Verified 2026-09-09:
`posts/nicu-01-free-lullaby` does not exist in the repo. From your Terminal, in `Automation Engine`:

    ./push-to-github.sh "NICU 01 - Free Lullaby" "posts/nicu-01-free-lullaby"

That publishes to:
`https://raw.githubusercontent.com/driftlullabies-web/drift-slides/main/posts/nicu-01-free-lullaby/reel.mp4`

**3 · Then tell Claude** — the Buffer draft gets created against that URL. It can't be made
before the push: Buffer probes the video at create time and a 404 fails the call.
⚠️ If a create_post ever 400s with "already scheduled", LIST before retrying — it can fail
AND have created the post (memory `drift-buffer-create-post-false-error`).

## Files here

`card.png` · `reel.mp4` (6s loop, decode-verified) · `caption.txt` · `card.json`
Both copy gates pass: `caption_guard.py` clean, `check_caption_overlap.py` clean.

## Caption

    Free personalized lullabies for babies in the NICU.

    Answer a few questions about your little one, and that's what their song is made from.

    Code NICU at checkout — link in bio. 🤍

    #nicu #nicumom #preemie #newmom #fourthtrimester

⚠️ Those five tags are relevance-first but **four of them are not in the curated pool** in
`Social Media Carousel Posts/hashtag-strategy.md` — there were no NICU tags in it. Add them
there if you want them reusable; that file is yours, so nothing was edited.

Build/design reasoning: memory `drift-nicu-offer-layout`. Post spec: `_reel_drafts/NICU 01 - Free Lullaby/README.md`.

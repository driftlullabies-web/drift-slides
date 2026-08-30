# INSP 05 - You Wont Remember The Song

Format: carousel · bg lavender #E6DFED · lane Inspired · mechanism 2 · The Sound That Leaves ·
destination lullaby/voice · treatment poem + LOCKED website CTA card · 3 slides ·
CTA **Website** · slot PM · counts toward the product-forward group

Source: @notes.from.motherhood 2026-06-19 "The lullaby was never meant for you" — 97K views, 16.6x
median, ER 11.3. The closest post in the whole 420-post log to Drift's own thesis.

CTA NOTE — RESOLVED 2026-08-30: this used to say slide 3 was render_cta's LOCKED default ask/url.
That convention died 2026-08-27 (drift-website-cta-locked) — render_cta now raises without an
explicit `main`. slide-3.png on disk predates that change and needs a re-render. Wrote a real
per-post Eyebrow/Ask pair below instead of guessing at Ben's intent for the caption's ask (he
confirmed 2026-08-30 that the caption itself carries no ask — the card is the only place this post
points at the site) — this pair has NOT been individually reviewed by Ben, only the caption. Flag it
in the next round if it doesn't land.

This is one of the few posts in the lane where the website bridge is honest — the poem lands on
keeping the song, which is what Drift makes. Do NOT bolt this CTA onto the other six.

## Hook
You will not remember this song / I'm the one holding it

## Slides
1  You will not remember this song / I'm the one holding it
2  I'm singing it for a Tuesday a long way from here / you'll remember being safe
*Slide 3 (the CTA card) is documented under Closer below, not here — keeping it out of this list
so the review workbook doesn't show it as a 3rd content item.*

## Closer (website — pill card)
Ask: "When you're ready, make them their own lullaby"
*Ben's edit (2026-08-30): no eyebrow, just the ask + LINK IN BIO pill. Replaces the eyebrow/ask
pair I drafted, which he had not yet seen when he asked to see the copy.*

Rendered slide-1..slide-2 at 44 px (poem treatment, `drift_inspired.render_poem_post`, bg lavender,
photo=True); slide-3 via `drift_slides.render_cta` with no eyebrow, the ask above as `main`, centred,
no url passed (render_cta draws the LINK IN BIO pill itself).

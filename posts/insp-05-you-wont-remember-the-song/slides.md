# INSP 05 - You Wont Remember The Song

Format: carousel · bg lavender #E6DFED · lane Inspired · mechanism 2 · The Sound That Leaves ·
destination lullaby/voice · treatment poem + LOCKED website CTA card · 5 slides ·
CTA **Website** · slot PM · counts toward the product-forward group

Source: @notes.from.motherhood 2026-06-19 "The lullaby was never meant for you" — 97K views, 16.6x
median, ER 11.3. The closest post in the whole 420-post log to Drift's own thesis.

CTA NOTE — RESOLVED 2026-08-30: this used to say the CTA card was render_cta's LOCKED default
ask/url. That convention died 2026-08-27 (drift-website-cta-locked) — render_cta now raises without
an explicit `main`. Wrote a real per-post Eyebrow/Ask pair below instead of guessing at Ben's intent
for the caption's ask (he confirmed 2026-08-30 that the caption itself carries no ask — the card is
the only place this post points at the site).

EXPANDED 2026-08-30 (Ben: "expand it") — the original 2-poem-frame + CTA card (3 slides) buried the
caption's strongest imagery ("The way your breathing slows by the third line," "your hand lets go of
my shirt," "your chest will go quiet, and you won't know why") in the caption only; Ben's point was
that the caption *is supposed to be the post* — those lines needed to be ON the slides, not just
narrating them from off-screen. First pass expanded the poem to 7 single-line-pair frames pulling
the caption's images onto the visuals (mirroring how INSP 06 was expanded from 2→6 frames the same
day). Ben then asked to COMBINE 1-2, 3-4, 5-6 back down into 3 fuller stanza-frames (frame 7
unchanged) — same words, same caption, denser pacing: 4 poem frames + CTA = 5 slides. Caption itself
is unchanged throughout; slides match it instead of only gesturing at it.

This is one of the few posts in the lane where the website bridge is honest — the poem lands on
keeping the song, which is what Drift makes. Do NOT bolt this CTA onto the other six.

## Hook
You will not remember this song — you're too small to keep it / So I'm the one holding it

## Slides
1  You will not remember this song — you're too small to keep it / So I'm the one holding it
2  The way your breathing slows by the third line / The way your hand lets go of my shirt
3  One day you'll hear four notes somewhere ordinary / And your chest will go quiet, and you won't know why
4  You won't remember the song. You'll remember being safe.
*Slide 5 (the CTA card) is documented under Closer below, not here — keeping it out of this list
so the review workbook doesn't show it as a 5th content item.*

Authored line breaks that actually render (flat "/"-joined text above is for the review-workbook
parser only):

```
Slide 1:
You will not remember this song —
you're too small to keep it

So I'm the one holding it

Slide 2:
The way your breathing slows
by the third line

The way your hand lets go
of my shirt

Slide 3:
One day you'll hear four notes
somewhere ordinary

And your chest will go quiet,
and you won't know why

Slide 4:
You won't remember the song.
You'll remember being safe.
```

Blank line marks the seam where the original combine happened (Ben, 2026-08-30: "it needs a space in
between lines where you had originally broken up the slides") — a stanza break, not a new size fit.
Re-ran `fit_poem` with the gap lines included; still fits at 50px, so no other slide moved.

## Closer (website — pill card)
Ask: "When you're ready, make them their own lullaby"
*Ben's edit (2026-08-30): no eyebrow, just the ask + LINK IN BIO pill.*

Rendered slide-1..slide-4 at 50 px (poem treatment, `drift_inspired.render_poem_slide`, mist bg +
navy text, one size fitted across all 4 frames — same 50px the original 7-frame cut fit to, since
the width-limiting line ("You will not remember this song —") didn't change). slide-5 is a one-off
CTA render (NOT `render_cta`/`render_photo_cta` directly — see below) built to match the poem
frames exactly: `drift_slides._photo_canvas(POETRY_BG_PATH)` for the same mist background, the ask
set at the poem's fitted size (50px, not render_cta's own 44-62px auto-fit range) and weight 650,
centred, with `drift_slides._draw_pill` for the LINK IN BIO pill. render_photo_cta was close (same
default background) but draws a URL line, not this post's pill, and doesn't accept a pinned font
size — so this one-off mirrors its layout instead of extending the shared function, per the
established pattern for one-off deviations (see INSP 04's no-rule special case).

Two stray files sit in this folder from the earlier 7-frame pass, renamed out of the `slide-*.png`
glob so no pipeline script picks them up (workspace blocks `rm`, only `mv`): `_orphan_do_not_use.png`,
`old-slide-6.png`, `old-slide-7.png`, `old-slide-8-cta.png`. All harmless; delete manually if they
bother you.

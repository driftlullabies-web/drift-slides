# 03 - Blanket Warmth

Format: Lullaby-poetry ("In English we say... / in poetry we say...") — photo-background
treatment, rain-on-glass image, white/light text, left-justified reveal. See
drift-lullaby-poetry-format (project memory) for the full spec and template bank.

## Cover eyebrow
In English we say...

## Cover
I sang my baby a lullaby before bed...

## Pacing beat (slide 2)
in poetry we say...

## Reveal (slide 3, left-justified, lines as written — do not re-wrap)
My voice is a blanket for my baby,
warmed by the afternoon sun,
something soft against their skin,
something they could carry
into dreamland.

## CTA (slide 4)
Website card, **no eyebrow in this lane** (Ben cut it — cleaner after a poem; the open question
about restoring one is still unanswered, see below — NOT decided unilaterally here).

**ASK WRITTEN 2026-09-03 (this weekly run):** "But a voice like that can be made just for them" —
turns the reveal's own image (voice as a blanket, warmed, carried into dreamland) toward the song,
no terminal period, no eyebrow per the lane's current convention.

✅ **RE-RENDERED 2026-09-04 (Phase 2)** via `render_photo_cta(main="But a voice like that can be
made just for them")`.

⚠️ **It rendered with the URL line `driftlullabies.com`, not the LINK IN BIO pill — flagged, not
changed.** `render_photo_cta` has no pill path at all; it only draws a URL. That means the whole
poetry lane diverges from [[drift-website-cta-locked]]'s current card (eyebrow + ask + pill), and
this post's own caption says "link in bio" while its card says the URL.

**This is pre-existing, not new: Poetry 01 and Poetry 02 both shipped the same way**, and Poetry 02's
slides.md even calls itself a "pill card" while its rendered slide-4 shows the URL. So Poetry 03 is
now consistent with the two that came before it. Making it consistent with the *other* lanes instead
means adding a pill path to `render_photo_cta` — a renderer change, and not something to slip into a
render pass. Worth Ben's call: is the poetry lane deliberately URL-only, or has it been quietly
stale since the pill landed on 2026-08-27?

~~⚠️ **NOT YET RE-RENDERED — this is COPY ONLY.**~~ Slide 4's PNG in this queue folder still carries
the OLD locked "type our website into your browser" wording and the retired URL line from before
the 2026-08-27 CTA rewrite. Phase 2 must re-render it:
  drift_slides.render_photo_cta(out, main="But a voice like that can be made just for them")
then re-push to GitHub.

⚠️ OPEN QUESTION for Ben, still unresolved: now that the eyebrow carries half the copy's work (it
concedes so the ask can turn), does this lane still want to skip it? The no-eyebrow rule was set
when the ask was a fixed sentence that needed no setup. Not added unilaterally this run.

## Caption
What singing to your baby at bedtime actually is.

Not a performance. A texture — and one they'll know long before they know a single word of it.

But a voice like that can be made just for them — link in bio. 🤍

#lullaby #babylullaby #newbornsleep #newmom #babysleep

## Hashtags
#lullaby #babylullaby #newbornsleep #newmom #babysleep

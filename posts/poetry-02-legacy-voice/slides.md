# Poetry 02 - Legacy Voice

Format: Lullaby-poetry ("In English we say... / in poetry we say...") — photo-background treatment,
rain-on-glass image, white/light text, left-justified reveal · lane Lullaby-subject (poetry, EXEMPT
from product-forward cap, COUNTS as a website ask) · slot PM (Sun) · angle C (your voice/the parent)

Ask written now (was previously blank — see the open TODO in the bank source file):

## Cover eyebrow
In English we say...

## Cover
I sang my baby a lullaby before bed...

## Pacing beat (slide 2)
in poetry we say...

## Reveal (slide 3, left-justified, lines as written — do not re-wrap)
I gave them my voice
so they would have something of me
to hold onto
after I left the room.

## CTA (slide 4, website — pill card)
Eyebrow: "Any lullaby can work."
Ask: "But imagine having one that was written just for your little one"

⚠️ Reusing Ben's own reference pair verbatim (from drift-website-cta-locked memory) rather than
improvising new wording. Proposes ADDING the eyebrow to this lane (previously skipped it when the
ask was a fixed sentence needing no setup) — flagged in the digest for Ben to confirm or veto; not
applied unilaterally as a silent lane-wide change.

## Caption
In English we say... I sang my baby a lullaby before bed.

In poetry we say... I gave them my voice, so they would have something of me to hold onto after I left the room.

Any lullaby can work. But imagine having one that was written just for your little one — link in bio. 🤍

#lullaby #babylullaby #newbornsleep #newmom #babysleep
*Caption expanded (Aug 30) — it previously carried only the cover line with no ask and no URL,
so "link in bio" never appeared anywhere for this post despite CTA = Website. Now matches 73's
and POV 01's convention of stating the ask in the caption, not just on the closing slide.*

---

## ⚠️ SLIDE 4 RE-RENDERED 2026-09-04 — the URL was a BUG, not this lane's convention

Ben: *"poetry lane should be the pill, not the driftlullabies.com that must be an error not an
exception."*

`render_photo_cta` had **no pill path at all** — it only ever drew the `driftlullabies.com` line,
which [[drift-website-cta-locked]] retired on 2026-08-27 when the bio link landed. So the whole
lullaby-poetry lane kept shipping the old convention while every other website CTA moved to the
pill.

**Why it stayed invisible for over a week:** this file already said "pill card" and the caption
already said "link in bio." Only the rendered PNG disagreed, and nothing in the pipeline compares a
slides.md heading against the pixels it produced. The copy checks read copy; the render checks read
file integrity; neither reads *meaning* off an image.

`render_photo_cta` now defaults to the pill and matches `render_cta`'s `_PILL_AUTO` rule exactly —
pass a real address and you get that line instead, because "LINK IN BIO" would point at the wrong
destination.

**This post was still queued** (Buffer, Sun Sep 6 7:30pm ET) and Buffer references the raw GitHub
URL rather than an uploaded copy, so re-pushing the corrected PNG is enough — no need to touch the
Buffer post. **Poetry 01 published Aug 27 and is left alone**; it shipped with the URL and that is
what shipped.

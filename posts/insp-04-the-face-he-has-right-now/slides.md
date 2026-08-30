# INSP 04 - The Face He Has Right Now

Format: carousel · bg cream #F4F0E6 · lane Inspired · mechanism 3 · The Number Nobody Counted ·
destination newborn-general · treatment SINGLE SLIDE · 1 slide · CTA none (ends) · slot PM

Source: @notes.from.motherhood 2026-06-05 "You only get about 28 days with a newborn" — 80K views,
13.7x median.

⚠️ FORMAT FLOOR TEST. Drift has never shipped a one-slide carousel. Fitted at 34 px — 16 lines on
one canvas is dense; to render bigger the copy has to lose ~4 lines. Watch whether a single slide
holds attention without a swipe to earn.

Claim check: "lasts about three weeks" is hedged and is an observation about a newborn's face, not
a developmental or medical claim.

## Hook
put the phone down for this one…
*Ben added the trailing ellipsis Aug 30.*

## Slides
1  put the phone down for this one… — the face he has right now lasts about three weeks / not his face, that's forever / this one — the squashed one, the newborn frown, the one you're slightly embarrassed to find this beautiful / you'll go looking for it in photos and it will already be gone / look at him now, not the camera, now
*This flat "/"-joined line is for the review-workbook parser only. The AUTHORED line breaks that
actually render (recovered from `Inspired from scrapped content Posts/build_samples.py`'s original
"D-single" call, single-slide `render_poem_post`, bg CREAM, max 60 / min 34) are:*

```
put the phone down for this one…
The face he has right now
lasts about three weeks.

Not his face — that's forever.
*This* one.
The squashed one.
The one with the newborn frown.
The one you're slightly embarrassed
to find this beautiful.

You'll go looking for it in photos
and it will already be gone.

Look at him now.
Not the camera.
Now.
```

⚠️ SPECIAL CASE (Ben, 2026-08-30): the top rule/dash is REMOVED on this slide only — he felt the
first render didn't feel centered with it. Every other poem-treatment post (INSP 05, INSP 06,
Poetry 02) keeps the rule; `drift_inspired.py`'s shared `_photo_canvas()`/`render_poem_slide()` were
NOT changed. Re-rendered via a one-off script that duplicates the photo-canvas logic minus the
`d.rectangle(RULE_BOX, ...)` call. If this slide ever needs re-rendering, use that same omission,
not the shared function.
*Single canvas, 34px, ~16 wrapped lines — added here (Aug 30) so the actual on-slide text is
visible in review; it was previously only implied by the caption. Wording matches the caption.*

# Poetry 05 - Borrowed Night

Format: **Lullaby-poetry** ("In English we say… / in poetry we say…") — photo-background treatment,
rain-on-glass image, white/light text, left-justified reveal · **2 slides** · lane **Lullaby-subject
(poetry)** · CTA **Website** · slot Mid (Sun 9/27) · avatar newborn.
See `drift-lullaby-poetry-format` for the full spec and template bank.

**EXEMPT from the product-forward group** (Ben, 2026-08-19: *"it's not salesy"*) · **COUNTS as a
website ask** · **participates in the sub-angle check** — this one is **E · keepsake artifact**,
which is the angle the exemption exists to let it share.

⚠️ **CLAUDE DID NOT WRITE THE COVER OR THE POEM.** Both are Ben's, from the bank at
`Lullaby Poetry Posts/05 - Borrowed Night/`, reproduced verbatim and not re-wrapped. What is written
here is the **CTA ask** (required by that file's own checklist before the post can be slotted) and
the caption.

**No eyebrow in this lane** — Ben cut it, and it stays cut. His 2026-08-27 open question about the
eyebrow is addressed at the foot of this file: it does not arise for this post's ask, and it stays
open for the lane.

⚠️ **THE LANE'S OWN NUMBERS ARE BAD AND BEN HAS A DECISION DUE.** Poetry 02 did 306 views / 0.98%;
Poetry 03 did 445 / 1.80% **as a one-card reel**, the format swap he asked for on 2026-09-09. His
condition when he cut Poetry 06 was *"save the copy for later if the reel does well."* **It did not
do well** — reach_x 0.59, 5.8s watch, in the account's bottom four watch times. This row runs because
the lane's floor is fixed at 1/week and the run is not permitted to drop it unilaterally; the verdict
is put to Ben in the digest.

**Format is now TWO cards, at Ben's instruction (2026-09-17).** It was drafted as a revert to the
4-slide carousel after the one-card reel failed to clear it; his review changed that to a two-card
shape. Full reasoning at the foot of this file.

⚠️ **Caption shape follows what Poetry 03 actually SHIPPED**, not the weekly-run step 3c-i text.
That step says *"Caption = the cover line + the lullaby-subject hashtag set, NO URL"* — but the same
step also says the post counts as a website ask, which a caption with no ask cannot be, and
`check_caption_overlap.py` rejects a first line that repeats the cover verbatim. Poetry 03 shipped a
three-paragraph caption ending on "link in bio". **Per the stale-spec rule, the last thing that
shipped wins and the step text is flagged for correction.**

**Phase 2 note — this queue folder deliberately contains NO PNGs.** `slide-4.png` in the bank
folder (`Lullaby Poetry Posts/05 - Borrowed Night/`) predates both the 2026-08-27 CTA rewrite and
the retirement of the typed URL — it still shows "type our website into your browser". It was not
copied in, because `render_week.py` skips folders that already have PNGs and deletes are blocked on
this volume. All four slides render fresh from this file: slides 1–3 on the lane's photo background,
slide 4 via `render_cta(main=<the ask>)` with no eyebrow and no url.

## Cover eyebrow
In English we say...

## Cover
I sang my baby a lullaby before bed...

## Cover sub-eyebrow (card 1, below the hook)
In poetry we say...

## Reveal (card 2, left-justified, ITALIC, in quotation marks — lines as written, do not re-wrap)
"I borrowed a little piece of the night
and tucked it beneath your dreams."

## Closer (card 2 — website pill card, below the reveal, no eyebrow in this lane)
Ask: "Create a lullaby for your little one"
Guarantee: goosebumps or it's free

## Caption
Lullaby lyrics for a baby who won't remember being sung to.

They won't keep the memory of it. The song is the part that can outlast the remembering, which is a strange and quite good reason to make one on purpose.

Create a lullaby for your little one — link in bio. 🤍

#lullaby #babylullaby #newbornsleep #newmom #babysleep

## Hashtags
#lullaby #babylullaby #newbornsleep #newmom #babysleep

---

## ✅ REVISED 2026-09-17 per Ben's review — TWO SLIDES, not four

> *"I want to try this as two slide format. 'In poetry we say…' makes it onto card one (a reason to
> swipe). Then CTA makes it onto card 2 with a simple 'Create a lullaby for your little one' link in
> bio. Goosebumps or it's free"*

**The new shape, and the reading it rests on** — recorded because the instruction is compressed and
the poem's placement is the part that could go wrong:

| | Card 1 | Card 2 |
|---|---|---|
| **now** | eyebrow · cover · **"In poetry we say..." as the cover SUB-EYEBROW** | **the poem** · website pill card |
| was | eyebrow · cover | "in poetry we say…" *(slide 2)* · poem *(slide 3)* · CTA *(slide 4)* |

Two lines in his note pin it down and they account for all four original slides: *"in poetry we say…"
**moves onto** card one" (it was slide 2, so it merges upward) and "CTA **makes it onto** card 2" (it
was slide 4, so it merges onto the poem's card). The poem is the only thing left, and it is what
card 2 is. It also produces exactly the swipe he describes: card 1 now **ends on an unfinished
promise** rather than on a complete thought, which is the reason to swipe that a two-card format
otherwise lacks.

**His CTA ask replaces mine verbatim.** Mine was *"Now imagine a night written down as a song only
\*them\* have"* — a callback to this specific poem's image. His is plain and portable:
**"Create a lullaby for your little one"**. That is the same correction he has made before on closing
lines ([[drift-generic-closer-ctas]]): the hook-specific callback belongs in the copy above, and the
ask's only job is to make the ask.

⚠️ **THE GUARANTEE NOW RENDERS, AND IT DID NOT BEFORE ON THIS LANE'S CARD.** He asked for it by name
here and separately queried its absence on REEL 29. `drift_slides.render_cta` has had
`guarantee=True` as its default since 2026-09-07, so the carousel path was already correct; the reel
path had no guarantee code at all and was silently dropping it. Fixed in `drift_reel.py` the same
day — see REEL 29.

⚠️ **Halving the slide count changes what this post is measured on, and that is the point.** The lane
has run four outings — carousel (306 views / 0.98%), carousel, and the one-card reel (445 / 1.80%,
5.8s watch). Two slides is a third container, not a redraft: one swipe instead of three, and the ask
arrives on the swipe rather than three cards later. **Read it against Poetry 03's reel, not against
the four-slide carousels.**

⚠️ **Claude did not write the cover or the poem.** Both are Ben's, from the bank at
`Lullaby Poetry Posts/05 - Borrowed Night/`, reproduced verbatim and not re-wrapped.

⚠️ **The open eyebrow question is now moot for this post.** The standing question — does this lane
still skip the CTA eyebrow, now that the eyebrow does the conceding? — does not arise here: his ask
is a plain imperative that needs no concession to earn it. **The question stays open for the lane**,
and nothing was added unilaterally.

**Phase 2 note — this queue folder deliberately contains NO PNGs.** The bank folder's `slide-4.png`
predates both the 2026-08-27 CTA rewrite and the retirement of the typed URL; it was not copied in,
because `render_week.py` skips folders that already have PNGs and deletes are blocked on this volume.
**Render TWO cards, not four:** card 1 on the lane's photo background carrying eyebrow + cover +
"in poetry we say…", card 2 carrying the reveal plus `render_cta(main="Create a lullaby for your
little one")` with no eyebrow, no url, and the guarantee left at its default.


---

## ✅ CONFIRMED 2026-09-17 (second review pass) — and he settled the one thing I had read rather than known

He moved **"In poetry we say..."** out of the Slide 1 column and into **Cover sub-eyebrow**, then
cleared Slide 1. That is not a copy edit, it is the answer to the question the first pass had to
infer: the line is not a frame of its own on card 1, it is the **sub-eyebrow under the cover hook**
(`render_cover(..., subeyebrow=...)`, the muted line BELOW the hook — `render-spec.md` 4-i). The
reading was right; the mechanism is now stated rather than guessed.

⚠️ **He also capitalised it: "In poetry we say..." — the bank has it lowercase.** Applied as he typed
it. As a sub-eyebrow under the hook it starts its own line rather than continuing the cover sentence,
so the capital is correct; lowercase was right only while it was a separate frame.

> *"I want to see this one rendered to make sure we are on the same page."*

Rendered and shown before anything else in this week is pushed.


---

## ✅ TYPOGRAPHY 2026-09-17 (third pass) — Ben's five type calls, all applied

| | Change | Why it is right |
|---|---|---|
| **card 1** | *"In English we say..."* → **regular colour** (navy, not lavender) | It is not a caption about the post, it is the first half of the device. Lavender read as a label. |
| **card 1** | *"In poetry we say..."* → **same size** as the line above (46, was 40) | They are a matched pair; the smaller size made the second read as an afterthought rather than the other half of the same move. |
| **card 1** | the hook **centred evenly between the two** | It was pinned at a fixed y that assumed nothing sat below it. Now the two framing lines are the fixed points and the hook sits at their midpoint. |
| **card 2** | the poem gets **quotation marks and italics** | It is a quote. Marking it as one is what lets the ask below sit in a different register without competing. |
| **card 2** | the ask **smaller** — *"not the focus. the quote is the focus."* | Ceiling dropped 54 → 40. The ask still gets the pill and the guarantee; it just stops arguing with the poem for the eye. |

⚠️ **One inference, flagged rather than buried.** He specified the colour change for *"In English we
say..."* only. It was applied to **both** lines, because a navy line above and a lavender one below
at matched size reads as an accident rather than a pair — and the point of the other two changes is
to make them a pair. **Say the word if you wanted only the first one changed.**

**Two renderer additions, both additive with unchanged defaults**, so nothing already shipped moves:
`render_photo_statement` gained `subeyebrow=`, and `render_photo_reveal_cta` (new) composes the poem
and the ask on one card with `italic=True` by default.

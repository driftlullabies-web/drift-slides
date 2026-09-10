# 03 - Blanket Warmth

⚠️ **FORMAT SWAPPED 2026-09-09 — this now ships as a ONE-CARD 6s REEL, not the 4-slide carousel.**
Per Ben's review. The four carousel PNGs are kept in `_carousel-superseded/` rather than deleted,
because they are what every earlier artefact in this week's run describes.

**What actually ships:** `card.png` + `reel.mp4`, built from `card.json` by
`Automation Engine/reels/drift_reel_nicu.py`. 1080×1920, 6.000s, 180 frames — decoded, not
checksummed ([[drift-checksums-arent-validity]]).

**Why the whole poem fits on one card.** At 47 words this is the shortest post in the lane, and the
carousel spent three slides pacing a reveal the reader can take in at once. The reel keeps the
reveal by *typography* instead of by swipe: the two labels sit in bold, the two sayings in quotes,
and the poem in lavender italic, so "In English" and "In poetry" read as a pair the eye compares
rather than a headline and its footnote.

**Four things Ben specified on the card, each a decision worth keeping:**

1. **No headline.** "It should feel like two equal thoughts, not a headline." A 62px title over
   44px body declares one of the two sayings to be the point; the whole device depends on them
   weighing the same. `render_nicu_card(headline=None)` was added for this.
2. **Both labels bold, both sayings in quotation marks.** The quotes are what makes "we say"
   literal — the reader is being shown the two sentences, not told about them.
3. **Every paragraph gap equal.** Each label is its own paragraph, so the gap after "In English we
   say" matches the gap after the sentence it introduces. Ben's note; it turns two tight clumps
   into one even rhythm.
4. **CTA centred over the pill** (`ask_align: "center"`), while the body stays flush left. A
   left-aligned ask leaves the centred pill visibly off-axis from the line it belongs to.

The card is also `vcenter: true` — a new flag that drops a SHORT card by half its leftover room so
it sits optically centred instead of clinging to the top of the frame. Off by default; the five
already-shipped NICU/INSP cards were re-rendered and confirmed byte-identical.

⚠️ **Still true, still unresolved: the reel renders on FLAT `BG_MIST` (#DCE6EC), not the
rain-on-glass photo the carousel used.** No reel renderer has a photo-background path at all. This
post therefore does not look like the two poetry posts that came before it. That is a renderer gap,
not a copy decision — see [[drift-inspired-song-poems-die]].

⚠️ **Collision, pre-existing and NOT introduced by the format swap: this post's cover line
"I sang my baby a lullaby before bed" is character-identical to Poetry 02 · Legacy Voice, which
published Sun Sep 6 — four days before this runs.** The lane's template reuses one English sentence
under different poetic restatements, so the collision is structural to the format rather than a
drafting slip. Flagged for Ben, not changed unilaterally: the fix is either to vary the English
sentence per post or to space same-sentence posts by weeks, and that is a lane rule, not a
render pass.

---

Format (superseded, kept for reference): Lullaby-poetry ("In English we say... / in poetry we
say...") — photo-background treatment, rain-on-glass image, white/light text, left-justified
reveal. See drift-lullaby-poetry-format (project memory) for the full spec and template bank.

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

**ASK — BEN'S, 2026-09-04:** "Make an original lullaby just for *them*" (`*them*` renders italic
lavender). Replaces the engine's "But a voice like that can be made just for them," which Ben
flagged as reading weird. He was right, and for a reason worth keeping:

- **It said we make a VOICE.** [[drift-product-truth]] is explicit — five questions in, a
  custom-composed song out, *never* "made in your voice," and never invent a capability to make a
  CTA bridge land. The old line borrowed the poem's voice-as-blanket image and paid for it in
  accuracy.
- **It was passive with no agent.** Every other house ask has one.
- **It was the only website ask in the account that never said "song" or "lullaby."** The product
  noun was missing from the product ask.

Ben's line fixes all three and drops the "But" — which is right, because **this lane has no
eyebrow**, so a "But…" was turning away from nothing. An imperative is the coherent shape for a
single-line CTA card with no concession above it.

✅ **RE-RENDERED 2026-09-04** via `render_photo_cta(main="Make an original lullaby just for *them*")`.

✅ **FIXED 2026-09-04 — it now renders the LINK IN BIO pill.** Ben: *"poetry lane should be the
pill, not the driftlullabies.com that must be an error not an exception."* `render_photo_cta` had no
pill path at all and now defaults to one. Poetry 02 (still queued for Sun Sep 6) was re-rendered
too; Poetry 01 published Aug 27 and is left as it shipped.

~~⚠️ **It rendered with the URL line `driftlullabies.com`, not the LINK IN BIO pill — flagged, not
changed.**~~ `render_photo_cta` has no pill path at all; it only draws a URL. That means the whole
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
  drift_slides.render_photo_cta(out, main="Make an original lullaby just for *them*")
then re-push to GitHub.

⚠️ OPEN QUESTION for Ben, still unresolved: now that the eyebrow carries half the copy's work (it
concedes so the ask can turn), does this lane still want to skip it? The no-eyebrow rule was set
when the ask was a fixed sentence that needed no setup. Not added unilaterally this run.

## Caption
What singing to your baby at bedtime actually is.

Not a performance. A texture — and one they'll know long before they know a single word of it.

Make an original lullaby just for them — link in bio. 🤍

#lullaby #babylullaby #newbornsleep #newmom #babysleep

## Hashtags
#lullaby #babylullaby #newbornsleep #newmom #babysleep

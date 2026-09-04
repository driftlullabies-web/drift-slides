# REEL 13 - What Only Happens With You

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Keepsake · CTA Share · slot AM (Tue 9/8)
NOT product-forward, no website ask.

Reworked in response to Ben's Sep 7 workbook notes (2026-09-03). The copy below is the engine's,
not his, so it is deliberately NOT marked with the linter-exemption phrase — these items must pass
check_reel_copy.py and check_caption_overlap.py on their own merits.

Hook #91 kept — Ben, 2026-09-03 review: *"LOVE the hook. Content is getting tired and
repeated. Please rework it."* **Items fully replaced this run.** The previous draft used the
milk-drunk face, curled fists and chest-weight, all three of which the account has run recently;
new items are drawn from list A of `Social Media Carousel Posts/newborn-detail-bank.md` (the bank
Ben wrote into the workbook against this row) and marked spent in that file's ledger.

Loss-framed by design, and every item genuinely has an end date — the startle reflex, the newborn
stretch, the wrist creases and the pre-sneeze scrunch all stop on a real timeline, which is what
makes the frame honest rather than sentimental. Turn unchanged; it observes rather than convicting
her of missing it (per drift-generic-closer-ctas).

Item collision checked against REEL 14 (this week's other Keepsake reel, gain-framed, list B) and
against 78 — no shared objects.

## Card (see card.json for the machine-readable source)
headline: The tiny parts of newborn life that disappear without saying goodbye
items:
  - The whole-body startle at a sound, arms flung wide
  - That first stretch after waking, arms up and back arched
  - The soft crease rings around both wrists, there and then gone for good
  - The nose scrunch a half-second before an enormous sneeze
cta eyebrow: Whatever lullaby you're singing now can bring these memories back later.
cta ask: When you're ready, we can help find *their* song   -> LINK IN BIO pill

## Caption
Newborn things that quietly have an end date.

The startle reflex is usually the first to go. You won't catch the last one — you'll just notice weeks later that it stopped happening.

When you're ready, we can help find their song — link in bio. 🤍

#newmom #newbornlife #keepsake #momtok #3ammom

## Hashtags
#newmom #newbornlife #keepsake #momtok #3ammom

---

## ⚠️ WEBSITE CTA ADDED 2026-09-04 — Ben's wording, and a layout constraint it exposed

Ben, in the Sep 7 workbook against this row:

> *"Please remember this cta for the reel. I want to use it or something very similar on ever reel
> that ties back to newborn moments/memories."*

He wrote it as three parts appended to the turn: the turn line, then *"You may be surprised how well
you can wire these memories and more into your brain with the right lullaby,"* then *"(When you're
ready, we can help find their song)"* and a LINK IN BIO pill.

**A reel card has room for ONE closing block, not two.** `render_reel_card`'s CTA path replaces the
byline, and the turn sits directly above it — with both, the block runs past the safe ceiling and
the renderer draws the pill ON TOP OF the ask. Verified: with a turn present it overflows at 4
items, at 3 items, and even with no eyebrow at all. The only shape that fits is the one REEL 12
(the first CTA reel, Aug 31) already uses — **no separate turn line.**

So the turn and Ben's lullaby sentence are **merged into the eyebrow**: *"One day it's just gone —
but the right lullaby can hold onto it."* That keeps the loop-back clause that sends the eye up,
keeps the lullaby tie-back he asked for, and keeps the `can` hedge that
[[drift-claim-softening]] requires on a memory claim. His ask line is verbatim.

⚠️ **Two things he asked for that could not be done as written**, both flagged rather than fudged:
- **"their" in italics.** The renderer sets one font per text run; there is no inline emphasis in
  an ask line. Rendered plain. Fixable, but it is a renderer change.
- **The full 19-word eyebrow.** It wraps to three lines and pushes the block over the ceiling on its
  own. Compressed to 12 words carrying the same claim.

# POV 08 - No One Else Has It

Format: carousel · bg **BLUSH `#EFDFD9`** · lane **POV Lullaby** · 6 slides · CTA **Website**
(locked pill card) · Sound: **Brand lane — the Drift lullaby as original audio** · slot Mid
(Thu 10/15) · avatar newborn · 🤍 in caption only (Lora cannot render it on a slide).
**PRODUCT-FORWARD #2 of 2 — sub-angle `D · uniqueness`.**

## Rotation — W11 is flagship-body **08** (01 → 08 → 01 → 09)
W10 ran POV 04 (an "other", Mon 10/5), so W11 is flagship-body; the flagship cycle's next is 08 (01 ran
W9, Mon 9/28). **01/08/09 share the same four body slides** — the alternation exists so they never run
back-to-back; POV 01 published **Mon 9/28 (147 views)**, 17 days before this.

**Sub-angle D, ≥10 days from the last D:** POV 04 (D) published Mon 10/5 — **Thu 10/15 is 10 days**,
the earliest day the rolling check allows. 92 (A, Tue) is two days earlier, so the never-same-day and
≥2-days-apart rules both hold.

⚠️ **Here for the anchor, and the data says so.** POV has been the bottom of the account three windows
running (POV 06 0.58×, POV 01 0.33×, POV 01's 3.28s watch). It runs because 3c requires exactly one POV
a week; flagged in the digest.

## ⚠️ THE CLOSER — brought to the CURRENT card (seventh instance)
The bank's slides.md is post-Aug-16 (website card) but **pre-Aug-27**: it specifies `render_cta default
main + url`, i.e. the URL-on-card version that the per-post-ask + LINK IN BIO pill replaced. Its caption
also told readers to *"type driftlullabies.com into your browser"*. Both brought to the current form,
following POV 01/04: the bank eyebrow is kept verbatim, a per-post ask is added, the caption carries the
link-in-bio paragraph.
**Staged per the POV 06 pattern: NO PNGs copied in.** The bank folder's six stale renders carry the old
URL card; `render_week.py` skips any folder with PNGs, so copying them in is what leaves a dead closer
in the queue. Phase 2 renders all six fresh from this file. **This post has SIX slides — count from this file.**

⛔ Product-truth check (3a-i): the caption lists **five** questions and names five (name · love most ·
hold · dreams · home) ✓. Nothing says the parent sings it or that it is in her voice ✓.

DELIBERATE REUSE OF "POV 01 - Written Just For Them"
DELIBERATE REUSE OF "POV 09 - Favorite Memory"

The four body slides are the flagship body shared by 01/08/09 by design (`rotation.md`); the
alternation keeps them apart. Declared so `check_item_collisions.py` does not report the reuse.

## Cover (Variant A — dominant POV hook, subordinate lead-in below)
hook: POV: no one else in the world has this lullaby.
render note: navy 650, size 72
subline (lavender-light 500, size 46, below the hook): It started with 5 little questions…
*(🤍 lives in the caption only — Lora can't render the emoji on-slide)*

## Body
2 You shared what you love most about them…
3 …how you feel when you hold them…
4 …your dreams for their future…
5 …and the place that feels like home

## Closer (website — pill card)
Eyebrow: "One of one, made just for them."
Ask: "Five questions, and the song is *theirs*"

## Caption
A personalized lullaby that no one else in the world has, made from five questions about your baby.

It started with five little questions — their name, what you love most about them, how you feel when you hold them, your dreams for their future, and the place that feels like home. From those answers came a song that's one of one. Just like them.

Five questions, and the song is theirs — link in bio. 🤍

#lullaby #babylullaby #newmom #newbornlife #keepsake

## Hashtags
#lullaby #babylullaby #newmom #newbornlife #keepsake

## Phase 2 note (2026-10-06)
`render_week.py`'s carousel path **drops the POV cover subline** ("It started with 5 little questions…") —
`render_cover` only receives an eyebrow, and a `subline (…)` field isn't parsed as one. Caught by eye on
the contact sheet. Fix applied here: **slides 1–5 are the approved bank renders** (`POV Lullaby
Posts/08`; slides 2–5 are byte-identical to POV 01's published body), and **slide 6 is the fresh pill
card** rendered from this file. Renderer gap logged in pending-posts.md for a proper fix.

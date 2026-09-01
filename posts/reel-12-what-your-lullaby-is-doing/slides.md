# REEL 12 - What Your Lullaby Is Doing

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Lullaby-subject ·
CTA **Website** (new CTA-on-card style, see below) · NOT YET SCHEDULED — built 2026-08-31 at Ben's
request ("can you find it and turn it into a reel"), not slotted into any week's plan.

Adapted from the carousel `queue/28 - What Your Lullaby Is Doing`, same source content, same
5-fact premise, same lane. That carousel is untouched — this is a new, separate post.

Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`
Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: 5 things your lullaby does to their brain
items:
  - A tune they know can mean safety, in a new room
  - Your voice can calm them, faster than any noise machine
  - Repetition can help their language, one repeat at a time
  - A steady rhythm can ease their breathing, without them noticing
  - The same song, sung enough times, becomes the cue their body knows
cta:
  eyebrow: Any song, sung enough, can already do all five.
  ask: But imagine one written just for your little one

61 words total (headline + items — the reel-copy-spec §2 budget), 5 items at 47-66 chars, spread
19. `check_reel_copy.py` passes clean; its only note is the standard "5 items, 4 is the house
shape" observation (not a failure) — see below for why 5 stays.

## Why the copy is shaped the way it is (Ben's questions, answered)

**"How will you subtly expand the copy to increase read time?"** The source carousel's 5 items
were bare noun-verb fragments (`Familiar can signal safe`, 24 chars). Reel register requires a
concrete image PLUS a payoff clause after a comma (`reel-copy-spec.md` §3, `[[drift-reel-copy-
register]]`) — that clause is what slows the eye down and is the whole difference between a reel
and a skimmable list. Every item here got a clause added (`, in a new room` / `, faster than any
noise machine` / `, one repeat at a time` / `, without them noticing` / `, sung enough times`),
landing all five at 47-66 chars against the source's ~24-30. That's the "expansion" — not padding,
but the same embellishment mechanism every other reel on this account uses.

**Why 5 items, not the house-standard 4.** The hook itself is "5 things" — that count IS the
recognition mechanism (hook-guardrails' "number only when the list is the point" applies exactly
here), so cutting to 4 would break the very premise Ben asked to adapt. Kept 5 and solved the real
constraint (vertical space, not word count — see below) a different way.

**"How will you add the new CTA style to the bottom of the reel?"** `drift_reel.py` had no CTA
rendering at all before this post — every reel to date was growth-CTA-only (Follow/Save/Share in
the caption), because the old rule was structural: the ask lived on a closing *card* and a
single-image reel has no closing card. That blocker died with the bio link
([[drift-website-cta-locked]], [[drift-reel-format]] "~~Reels can never carry the website ask~~ —
RETIRED 2026-08-27"), and this post qualifies to use it: the lullaby is genuinely the subject,
judged by the card itself (all 5 items are literally about what the lullaby does), not just a
caption bridge. So I added a `cta` block to `render_reel_card()` (see `drift_reel.py`, "Website CTA
block" section) that draws the SAME eyebrow -> bold ask -> "LINK IN BIO" pill sequence as the
carousel's locked CTA card (`drift_slides.render_cta`), just laid out at the bottom of the one
frame instead of on its own slide — visually the same brand move, new geometry.

## The space problem this actually ran into, and how it got solved

A full headline + 5 embellished items + a separate "turn" line + a full 3-part CTA block does NOT
fit in the ~1040px a reel card has between the top rule and the safe-zone floor — confirmed by
instrumenting the renderer's own joint-fit math, not by eyeballing. First attempt (5 items + turn +
CTA) rendered with items crushed to the 30px floor and the CTA pill overlapping the ask text above
it — a real visual bug, not a cosmetic warning. Root cause: the joint item-fit only reserved space
for a possible turn line; it had no idea a CTA block might follow, so items sized themselves as if
nothing came after them, then the CTA got jammed into whatever was left.

Fixed two ways, both now general (not special-cased to this post):
1. **`_fit_items_below` now reserves worst-case room for the CTA block** (eyebrow + 2-line ask +
   pill, at max sizes) before sizing items, the same way it already reserved for the turn line —
   so items shrink far enough up front instead of overflowing and colliding with what's below them.
2. **Dropped the separate "turn" line when a CTA is present.** The turn's job (per spec: "reframes
   what she just read... has no carousel equivalent") is structurally the same job the CTA
   eyebrow already does (per the locked CTA doc: "the eyebrow concedes... that concession is the
   mechanism"). Carrying both was paying for the same beat twice, and it was the single biggest
   line item in the vertical budget (turn's own reserve was bigger than the entire CTA block's).
   `render_reel_card(cta=...)` simply doesn't require a `turn` argument.
3. Also gave the CTA block its own, slightly tighter ceiling (`CTA_MAX_Y`, just under the true
   `SAFE_BOTTOM` chrome boundary) instead of reusing `CRED_MAX_Y` — that constant was deliberately
   padded well above the safe zone for a small decorative byline, and a CTA is load-bearing content
   that earns the room back. Gaps inside the CTA block itself were also tightened (a CTA is
   competing for space with headline+items, unlike the byline it replaces).

With those two structural fixes plus the headline trimmed from 3 lines to 2 ("5 things your
lullaby does to their brain" — dropped "the"/"your newborn's" → "their"), the card fits with
genuine margin: items render at 33px (not the 30px floor), headline at 58px. Verified: rendered,
full `ffmpeg -i ... -f null -` decode clean, `check_reel_copy.py` passes.

## What's NOT done

- **Not scheduled.** No `schedule-*.json` references this folder; it doesn't count toward any
  week's post total, ≤3/day cap, or the [[drift-product-forward-cap]] group yet. It WILL count
  against that cap the week it's slotted in (lullaby-subject + website ask), same as any other
  product-forward post — flag that when scheduling it.
- **Not pushed to GitHub yet as of first build** — will push alongside this round's other changes
  so it's ready whenever Buffer queuing happens; queuing itself stays manual, per standing rule.

## Caption
Per reel-copy-spec §7.4b: keyword-forward opening line (not a verbatim repeat of the card
headline), then straight to the ask, no item recap. Per [[drift-website-cta-locked]]: caption
mirrors the card's own ask, then points at the bio. See `caption.txt`.

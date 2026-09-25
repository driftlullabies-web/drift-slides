# POV Lullaby — 01 · Written Just For Them  *(flagship)*

Format: carousel · **bg BLUSH (`#EFDFD9`, `ds.BG_BLUSH`)** · lane **POV Lullaby** (soft-sell showcase)
CTA: **Website (locked pill card)** · slot Mid (Mon 9/28) · avatar newborn ·
**PRODUCT-FORWARD, sub-angle D · uniqueness / made-for-them** · counts toward the website-ask counter
Sound: **Brand lane — the Drift lullaby itself as original audio** (the song IS the subject; letting
people hear it is the payoff) · 🤍 in the caption only.

Rotation **W9** (`POV Lullaby Posts/rotation.md`) — flagship week; the pointer advances to POV 03
(other) for W10, Oct 5–11.

The POV series showcases what Drift actually makes without selling it: a POV cover hook + a dreamy
chain of the real onboarding answers + a payoff closer. Cadence **1×/week**.

---

## 🔴 THREE THINGS CHANGED THIS WEEK — read before rendering

### 1. This post still carried the PRE-2026-08-16 closer, and nobody had noticed

The Phase-2 hand-off for the week of Sep 21 listed **POV 03, 04 and 06** as the POVs still carrying
the old Save/no-URL closer. **POV 01 is a fourth.** Its queue folder's `slide-6.png` is the old payoff
card and its `caption.txt` had no URL paragraph — despite the post having run again in **W5
(Aug 31 – Sep 6)**, after the standing change. The list was wrong, not just incomplete.

⚠️ **Phase 2 must overwrite `slide-6.png` in this folder.** `render_week.py` skips any folder that
already has PNGs, and deletes are blocked on this volume, so the stale card survives unless slide 6 is
re-rendered explicitly. Count slides from this file, not from memory: **this post has 6 slides.**

### 2. Ben's closer line is NOT rewritten — it becomes the eyebrow

This file records *"Locked, Ben's own wording, kept as written per Ben's review — do not rewrite."*
The standing 2026-08-16 instruction says every POV from that date forward closes on the locked website
card. Those two are in genuine conflict, and the resolution keeps **his sentence verbatim** by moving
it into the card's **eyebrow**, which is structurally the recap/concession slot
([[drift-website-cta-locked]]). Nothing of his is lost and the ask is added underneath it.

**If he would rather keep slide 6 exactly as it was and add a seventh slide, that is a one-line
change** — it is flagged in the digest as his call, not settled here.

### 3. The caption said "five little questions" and then listed FOUR

The exact enumeration bug [[drift-product-truth]] records against POV 01 and POV 08 — *"it started
with five little questions"* followed by four items — was **still live in this folder's
`caption.txt`**. It has shipped at least twice. Fixed: the caption now lists all five, with the name
first, matching the five real onboarding questions below.

### 4. Its body slides are SHARED with POV 08 and POV 09, by design

DELIBERATE REUSE OF "POV 08 - No One Else Has It"
DELIBERATE REUSE OF "POV 09 - Favorite Memory"

`POV Lullaby Posts/rotation.md` states it outright: **01, 08 and 09 "share the same 4 body slides +
closer, which is why they're spaced this way"** — the flagship cycle deliberately puts an "other"
POV between them. They are three covers on one reveal chain, not three posts that happen to rhyme.

`check_item_collisions.py` flagged *"…and the place that feels like home"* against both of them the
moment this post's body became parseable (it had been invisible, see above). That is a true match and
a designed one, so it is declared rather than argued with. **The declaration names the two siblings
only — a collision with any other post still fires.**

⚠️ If the flagship body is ever rewritten, it has to be rewritten in all three folders or these
declarations become a licence to ship a real duplicate.

---

## Cover (Variant A — dominant POV hook, subordinate lead-in below)
hook: POV: your baby's bedtime song was written just for them
render note: navy 650, size 72
subline (lavender-light 500, size 46, below the hook): It started with 5 little questions…
*(🤍 lives in the caption only — Lora can't render the emoji on-slide)*

## Body
*(the reveal chain — plain navy-650 statement slides, blush bg, ellipsis-chained)*

⚠️ **Heading renamed `## Reveal chain` → `## Body` on 2026-09-24, and the rename IS the fix.**
`build_run_sheet.py` looks for `Items` / `Body` / `Slides`; *"Reveal chain"* matched none of them, so
this post's four body slides parsed to **nothing** and the review workbook showed an entirely empty
row — cover and closer present, the whole middle blank. POV 06 and POV 09 had already been normalised
to `## Body` at some point and were fine, which is why the lane looked healthy. **POV 01 and POV 10
are the last two carrying the old heading**; POV 10 still has it and will do the same thing the week
it is slotted.

This is the fourth time a lane's private section name has silently emptied a row in the artefact Ben
reviews from (Inspired `## Slides` · Poetry `## Pacing beat`/`## Reveal` · the creator lane's
`## Slide 5`/`## Slide 6` · this). The parser now also accepts `Reveal chain` so the remaining bank
folders cannot repeat it, but the heading here is normalised anyway — **a lane should not need a
special case per post.**
2 — You shared what you love most about them…
3 — …how you feel when you hold them…
4 — …your dreams for their future…
5 — …and the place that feels like home

*Which onboarding question each slide maps to — a build note, deliberately NOT on the item lines:
slide 2 = the bonus / catch-all · slide 3 = the feeling · slide 4 = the wish · slide 5 = the nature /
safe-place imagery. Inline parentheticals end up inside the review workbook's copy cells, which is
where Ben reads the creative — a note that only makes sense to the renderer should not sit in the
same cell as the words that publish.*

## Closer (website — pill card)
Eyebrow: "Now every bedtime has a song with their name in it."
Ask: "Five questions is all it takes to make *theirs*"

*Eyebrow is **Ben's own locked line**, verbatim, moved from the old payoff slide — do not rewrite it
to satisfy `check_closers.py`'s length/echo heuristics; the flagship's line is a deliberate exception.*
*The name claim is true — the finished lullaby sings the child's name, confirmed by Ben.*
*Ask is 46 characters (§8.11 budget ≤50), emphasis on **theirs** per §8.8, no terminal period.*
*Alt emotional line, reserved for a future POV variant: "Now you have a song that holds your love."
Soften any "keeps them safe" phrasing per drift-claim-softening before using.*

## The 5 real onboarding questions (source of truth for future POV posts)
1. Baby's name / nickname (what you call them) — sung into the song
2. The feeling when you hold them
3. Your wish for them
4. Where you go when everything feels safe (nature imagery)
5. Bonus catch-all — anything else that belongs in the song

## Caption
POV: your baby's bedtime song was written just for them 🤍

It starts with five little questions — their name, what you love most about them, how you feel when you hold them, your dreams for their future, and the place that feels like home. From those five answers comes a lullaby that is entirely theirs, with their name sung right into it.

Five questions is all it takes to make theirs — link in bio. 🤍

#newbornlife #lullaby #newmom #fourthtrimester #babylullaby

## Hashtags
#newbornlife #lullaby #newmom #fourthtrimester #babylullaby

---

Rendered slide-1..slide-6 via `drift_slides.py` (weight 650, `ds.BG_BLUSH`). No cover credibility
byline (POV isn't a therapist-authority post).

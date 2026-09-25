# Viral 05 - Wish This Existed

Format: 3-card viral hook · bg lavender #E6DFED · lane **Viral Hook** · CTA **Website** · slot Mid
(Wed 9/30) · renderer `_render_viral.py` · avatar newborn · **EXEMPT from the product-forward group**
(lane-mix-bands) · **COUNTS toward the website-ask counter**.

Hook **VH-04** from `Viral Hook Posts/viral-hook-copy.md`, unshipped: *"The heartache of knowing this
didn't exist when my babies were born."*

**This is week 4 of the 4-week read.** Week 1 = Viral 01 (Sep 3), week 2 = Viral 02 (Sep 11),
week 3 = Viral 04 (Thu 9/24). After this the lane drops to its 0-1 band and floats.

## Why VH-04 and not the rest of the pool
- **Mechanism.** Future-loss / regret, the ledger's best at **1.63x median ER** — and unusually for
  this lane it is not *product-as-subject*, which `card-patterns.md` lists as a measured anti-pattern.
  The subject is the absence, not the product.
- **VH-02 and VH-10 were passed over** — VH-02 (*"a song that exists nowhere else on earth"*) is
  uniqueness, sub-angle **D**, which POV 01 runs on Monday; VH-10 (*"POV: it's 3am…"*) borrows the POV
  lane's own frame in the same week POV 01 runs, and is product-as-subject.
- **The gift/registry shelf (VH-06, VH-07) was avoided again**, per Ben's note on Viral 04. Viral 02
  (Fri 9/11) is that angle.
- **VH-01** is instruction-adjacent (*"consider this your sign"*) — 0.51x mechanism.

## 🔴 STOP AND FLAG — the hook speaks in the first person about the writer's own children
*"…when my babies were born"* asserts that the speaker has grown children. **It is Ben's own wording
from his own pool, so it is reproduced verbatim and not rewritten** — but it is worth his eye for two
reasons: the account has never used a first-person founder voice in a *content* post (only the Intro
Post), and a first-person claim is the one kind of line this run cannot verify. If the voice is wrong
for the feed, the fix is his, not a rewrite here.

⚠️ **The pool file's shared caption boilerplate was NOT used and is still stale** — second week of
flagging it. It carries (a) the credential paragraph, which `caption_guard.py` hard-fails, (b) `#fyp`,
which is banned, and (c) *"free for the first 50 families"*, an offer no shipped Viral post has
carried. **That block needs updating or deleting.**

## Cover
The heartache of knowing this didn't exist when my babies were born.

## Cover sub-eyebrow
And it only takes a few minutes to make one now…

## Items
1 Not a playlist. Not a nursery rhyme with a name dropped into it.

## Closer (website — pill card)
Eyebrow: (none — removed by Ben 2026-09-24; render with eyebrow=None)
Ask: "An entire lullaby written for *them*"

Ask is 36 characters (§8.11 budget is ≤50). Emphasis on **them** per §8.8 — the word carrying the
argument is the one that says the song belongs to this baby rather than being a song about babies.
No terminal period; it hands off to the pill.

⚠️ **EYEBROW IS DELIBERATELY EMPTY — render `render_cta(main=..., eyebrow=None)`.**
[[drift-website-cta-locked]] describes the card as eyebrow + ask + pill, with the eyebrow conceding
so the ask can turn. **This post does not need the concession and Ben removed it.** The reason holds:
in the 3-card viral format the *cover* already makes the concession (*"this didn't exist when my
babies were born"*) and the sub-eyebrow already turns (*"it only takes a few minutes now"*), so an
eyebrow would be the third time the same move is made, on the third card. The lullaby-poetry lane
skips the eyebrow for the same structural reason. **Do not add one back.**

Product truth ([[drift-product-truth]]): five questions in, a composed song with the baby's name sung
in it, **ready in minutes** — so Ben's *"only takes a few minutes"* is the product's own claim, not a
widened one. Nothing here says the parent sings it or that it is made in her voice.

## Caption
A personalized baby lullaby, and the small ache of it not existing sooner.

A handful of questions about your little one, and a few minutes later it comes back as a song with their name sung in it. That did not used to be possible at all.

An entire lullaby written for them — link in bio. 🤍

#babylullaby #newmom #lullaby #momtobe #keepsake

## Hashtags
#babylullaby #newmom #lullaby #momtobe #keepsake


---

## ✅ REVISED 2026-09-24 per Ben's review — his wording, applied verbatim

| | His | Mine |
|---|---|---|
| **cover sub-eyebrow** | And it only takes a few minutes to make one now… | And it takes five questions to make one now… |
| **CTA eyebrow** | *(none)* | "Nothing like it existed a few years ago." |
| **CTA ask** | An entire lullaby written for \*them\* | Now there is one waiting to be written for \*them\* |

**The sub-eyebrow swap answers the objection the cover raises.** The cover's ache is about *time* —
this wasn't available when it mattered — so the reopening line that lands is the one about how
little time it takes now. "Five questions" answers *effort*, which nobody asked about on this card.

**The ask got twelve characters shorter and gained the noun.** Mine described the availability of a
thing; his names the thing. At 36 characters it also renders at the ask's full size with room to
spare, where mine sat near the top of the budget.

**Cutting the eyebrow is a structural call, not a trim** — recorded above the fold in the closer
block so nobody "restores" it in a later pass.

⚠️ The cell he typed carries a curly opening quote (`“An entire lullaby…`) with a straight closing
one — Numbers autocorrect on the cell, not part of the copy. The ask is stored unquoted.

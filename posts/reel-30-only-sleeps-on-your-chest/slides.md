# REEL 30 - Only Sleeps On Your Chest

Format: **REEL — PROSE CARD** (single-image 6s loop, 1080x1920 MP4, `drift_reel_nicu.py`) · bg cream
· lane Sleep · CTA **Save** (asked in the caption) · slot AM (Fri 9/25) · avatar newborn ·
NOT product-forward · no website ask.

Premise **#52** from `hook-bank.md` bucket **A · READY** (*"If your newborn only sleeps on your
chest…"*).

⚠️ **THIS ROW REPLACES BENCH POST 77, WHICH WAS NOT SLOTTED.** 77 (*"Try this the next time your
newborn won't settle:"*) rolled over from the week of Sep 14 and is finished, gate-passing copy — but
its hook is an **instruction**, which `card-patterns.md` lists as a measured ANTI-PATTERN (0.51x
median ER across 51 posts; REEL 10 did 2,094 views at 0.67% with zero shares and zero comments).
Ben's own note when he cut REEL 26: *"Every unshipped Sleep hook left is instruction-shaped, the
account's worst mechanism; a replacement needs new material, not another draw."* Running 77 because
it was on the bench would be exactly the draw he ruled out. **77 stays on the bench, unspent, not
binned.**

**Register is noticing, not prescribing** — that is the whole point of the swap. Nothing here tells
her to do anything; it tells her what is already true. The one Sleep post that worked this month
(REEL 16, 1,883 views / 1.65% ER / 9.1s watch, the week's best reel watch time) was in exactly this
register.

Claim check on Ben's copy, per [[drift-claim-softening]]: *"your heartbeat, movement, warmth, and
voice were part of their world"* states what is present in utero and claims **no effect** from it;
*"a contact nap is still a nap"* is definitional, not physiological. **No sleep-outcome claim anywhere
on the card**, and nothing that needs a can/may hedge because nothing asserts a mechanism.

Closing line checked against [[drift-generic-closer-ctas]]: *"For now, you get to be the place they
know"* lands the verdict on her as a **gift, not a failure** — the distinction that rule exists for.

## Card (see card.json for the machine-readable source)
format: PROSE CARD (`drift_reel_nicu.py` — headline + body paragraphs, no items, no pill)
headline: If your newborn will only sleep on your chest
body:
  - You didn't teach them to need this.
  - For nine months, your heartbeat, movement, warmth, and voice were part of their world.
  - So when they fall asleep on your chest, they're not "learning bad habits." // /They're finding something familiar./
  - And yes, a contact nap is still a nap. // /You don't have to make every sleep look independent./
  - One day, they'll fall asleep somewhere else.
  - For now, you get to be the place they know.
pill: none   ·   ask: Save, in the caption only

## Caption
Newborn contact naps, and why the chest is usually the whole answer.

Almost nobody arrives at this on purpose. It is the room they were in for nine months, and wanting it back is not a habit anyone accidentally created.

Save this for the days you need the reminder. 🤍

#newbornsleep #babysleep #newmom #fourthtrimester #gentleparenting

## Hashtags
#newbornsleep #babysleep #newmom #fourthtrimester #gentleparenting

---

## 🔴 2026-09-17 — THIS FILE WAS EMPTY IN BEN'S REVIEW WORKBOOK, AND HE CAUGHT IT

> *"I'm not seeing the slides/content here???"* — Ben, row 14 of the Sep 21 workbook

**He was right and it was a real bug, not a workbook bug.** `slides.md` had been **truncated to a
single heading**. The card itself was fine the whole time — `card.json` was intact, `card.png` and
`reel.mp4` rendered correctly from it — but every downstream reader (`build_review_workbook.py`,
`build_run_sheet.py`, and `render_week.py`, which renders FROM slides.md) had nothing to read. The
workbook showed the hook and the CTA (both sourced from `card.json`) and four blank slide cells.

**Cause, and it is worth writing down because it is a one-line Python trap:**

```python
open("slides.md", "w").write(open("slides.md").read().replace(o, n))
```

Python builds the call left to right: `open("slides.md", "w")` is evaluated **first** and truncates
the file to zero bytes, and only then does `open("slides.md").read()` run — returning `""`. The
file was silently emptied by its own edit. A later append then wrote a note into what was by then an
empty file, which is why one heading survived and nothing else did.

**The fix for the habit, not just the file: never write a file in the same expression that reads it.**
Read into a variable, then write. Every other in-place edit this run used a two-step read/write and
none of them lost content.

**Why no check caught it.** `check_plan_matches_posts.py` passed because it reads the cover from
`card.json` for reels. `check_reel_copy.py` passed for the same reason. `caption_guard.py` reads
`caption.txt`. **The only artefact that reads slides.md for a reel's items is the workbook — which
is exactly the gate Ben reads**, so the review loop caught it on its first pass. Ninth instance of
the blind-downstream-reader class, and the first one where the *human* gate was the thing that
worked.

**Content restored above verbatim from `card.json` plus the original notes.** Nothing was rewritten;
the copy Ben reviewed in the Reels tab (which sources `card.json` and was intact) is what is here.


---

## ✅ REWRITTEN 2026-09-17 (second review pass) — BEN'S WORDS, AS A CONNECTED THOUGHT

> *"Just do this one in more of the connected thought format:"* — followed by the full card, which is
> reproduced above verbatim. Curly quotes straightened to straight per the render spec; his soft line
> breaks inside paragraphs 3 and 4 preserved exactly.

**This is a FORMAT change, not just a copy change, and it is the right one for this premise.** The
four-item version was a list of reassurances that happened to sit next to each other. His version is
one argument that walks: *you didn't cause it → here's why they want it → so it isn't a bad habit →
and the nap still counts → and it ends on its own → so be the place.* A list cannot make a causal
argument; each bullet has to stand alone. **Absolution is the one register that needs the connective
tissue**, because the whole job is to walk her from "am I doing this wrong" to "no", and a bullet
list asks her to make that walk herself.

**Renderer:** `drift_reel_nicu.py` (headline + `body` paragraphs), the same prose path REEL 20 and
REEL 21 use — not `drift_reel.py`. `"pill": null` suppresses the CTA pill; the Save ask lives in the
caption, unchanged.

✅ **This also dissolves the one check that was still failing on this post.** The item-spread rule
(≥15 characters between longest and shortest) was unsatisfiable here — a short headline gives the
items a bigger font, which caps a two-line item at ~60 characters, and against the spec's 45-character
floor that leaves a 15-character band to spread across. A prose card has no items, so
`check_reel_copy.py` now skips it the way it skips REEL 20 and 21. **The constraint conflict is still
real and still worth fixing in the spec** — it just no longer applies to this post.

⚠️ **One render note, not a copy note:** the block runs to 1523px against a normal 1468 ceiling, so it
borrows a little of the room TikTok's chrome usually gets. Checked on the rendered PNG — the text ends
well clear of the caption bar and nothing is clipped. Left as-is.


---

## ✅ TYPOGRAPHY 2026-09-17 (third pass) — the second thought is ITALIC

> *"Whenever there is a second thought. In this case 'they're finding...' and 'You don't have...'
> those should be itallics for better readibility."* — Ben

Both payoff halves are now **navy italic**, same size and same colour as the line they answer. This
is a rule for the format, not a one-off: in a setup/payoff pair the second line is a different move
(the reframe), and on a dense prose card an unbroken wall of upright text gives the eye nothing to
sort by. Italic marks the turn without adding a colour or a weight the card doesn't need.

⚠️ **The mark matters — `drift_reel_nicu.py` has FOUR emphasis marks and they are not interchangeable:**

| mark | renders as |
|---|---|
| `*phrase*` | lavender + italic |
| `_phrase_` | **BOLD, upright** |
| `+phrase+` | lavender, upright |
| `/phrase/` | **navy italic** ← this one |

The first attempt used `_..._`, which is what REEL 20 uses, and it came out **bold** — that mark was
set to bold-upright by Ben himself on 2026-09-08. Caught by opening the PNG, which is the only way
this was ever going to be caught: the copy is identical either way. **`/.../` is the italic mark.**

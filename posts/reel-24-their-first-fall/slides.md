# REEL 24 - Their First Fall

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Tradition · CTA **Follow**
(growth — the lane's one required growth row this week) · slot AM (Fri 9/18) · engine **1 ·
calendar** · NOT product-forward, no website ask, no product item.

Hook **C1** from `tradition-hook-pool.md`'s AUTUMN RAMP — *"Their first fall — the traditions worth
starting now… (mid-Sept)"*. **This is the seasonal deadline the weekly run has been carrying since
mid-August**, and this is the week its window opens.

**Engine choice is deliberate.** The pool's own lesson from TRAD 03 is that it must not hand out two
engine-2 (weekly-rhythm) hooks back to back — REEL 15 was engine 2 and ran Sep 9, which rules out
W4. D5 was the other launch-window hook available and was rejected on the **occasion-variety** rule:
all five of its items hang off a birthday, which is one occasion shown five times. C1 is engine 1,
never used by this lane, and its items span four different autumn occasions.

Occasion-variety count (brief §, and weekly-run 3-i-b): first-cold morning · an autumn outing · the
last warm evening · an annual documentation habit. **Four items, four distinct occasions**, and each
carries a rule in it (the walk you take anyway · carried home by you · outside just because ·
pressed and dated in the same book).

Item collisions checked against TRAD 05 (ornament/doorframe/handwriting/planting), REEL 09
(Saturday pancakes / same tree each season / soup on the first cold night / treat after a checkup),
REEL 15 (day-of-the-week rhythms) and REEL 17 (stuffed animal/winter hat/ticket stub/nickname).
⚠️ **REEL 09 published Sep 4 and owns "the first cold night" and a seasonal repeat photo** — item 1
was rewritten from a cold-morning-walk to *the first hat morning* and the annual-photo item was
dropped entirely, so nothing here reruns it. The winter hat in REEL 17 is a kept object; the hat
here is a morning, not an object.

Tradition's hard product boundary holds: **no lullaby item, no website ask** (`tradition-brief` §5).

## Card (see card.json for the machine-readable source)
headline: Their first fall only happens once — start these traditions now
items:
  - Have them choose the “perfect” leaf. Press it, date it, and save it in the same book every year.
  - Let them pick one pumpkin they absolutely cannot lift. Carry it home anyway.
  - Make time for at least one fire with friends. S'mores are mandatory.
  - The first hat morning means a trip to the farmers market for a fresh-baked apple pie.
turn: None of it is a plan. That is what makes it a tradition.

## Caption
Fall traditions to start with a baby who won't remember this one.

Pick one, not four. A first tradition only has to survive being done twice — the year it starts is the year nobody notices, and year four is when someone asks whether you're doing it again.

Follow for the small things worth keeping.

Which one would your family actually keep? 🤍

#newmom #familytraditions #momlife #newbornlife #momtok

## Hashtags
#newmom #familytraditions #momlife #newbornlife #momtok


---

## ⚠️ ITEMS 1, 3 and 4 REVISED 2026-09-10 per Ben's review — his wording, verbatim

From the Sep 14 workbook. Item 2 (the pumpkin) is the only one he kept. He also **reordered**: the
leaf moved from last to first and the hat morning from first to last. Both honoured.

| # | Now (Ben's) | Was (mine) |
|---|---|---|
| 1 | Have them choose the “perfect” leaf. Press it, date it, and save it in the same book every year. | The first hat morning, and the walk you take anyway |
| 2 | *(unchanged)* Let them pick one pumpkin they absolutely cannot lift. Carry it home anyway. | — |
| 3 | Make time for at least one fire with friends. S'mores are mandatory. | The last warm evening — dinner outside, just because you still can |
| 4 | The first hat morning means a trip to the farmers market for a fresh-baked apple pie. | A leaf handed to you, pressed and dated in the same book |

**His version is warmer and more specific than mine** — mine described autumn, his gives her things
to actually do. Not rewritten, not trimmed. Three things it costs, all visible in `card.png` and
none of them fixable without touching his words, so they are flagged instead:

1. ⚠️ **Item 4 wraps to THREE lines, with "pie" alone on the third.** Every other item on every
   other reel wraps to two. The widow is the part that reads as a mistake.
2. ⚠️ **Items dropped from 44px to 34px — the floor.** The renderer prints
   *"items set at 34px (from 44) to fit the safe band"*. This card is now visibly denser than the
   other six reels in the week.
3. ⚠️ **78 words against the 45–70 budget → ~4.3 loops.** Past the "land it at 3" target
   (`reel-copy-spec.md` §2); the card starts to read as homework rather than a list.

**The cheapest fix, if he wants one:** item 4 loses two words —
*"The first hat morning — a trip to the farmer's market for apple pie"* (67 chars) drops to two
lines and pulls the whole card back off the floor. **Not applied; it is his line.**

⚠️ **Also his, also not changed: the `=` in item 4.** It renders literally on the card and reads as
a spreadsheet artefact rather than copy — an em dash is the house mark for this shape. Flagged
rather than swapped, per the never-silently-reword rule.

⚠️ **Item-ledger collision, reported not resolved:** *farmer's market* is claimed by hook **W1**,
which shipped as **TRAD 03** on Aug 24 (*"Saturday farmers market"*). Three weeks back, so it is
outside the 7–10-day dedupe window, but `tradition-hook-pool.md`'s ledger says a shipped hook's
items are spent. His line, his call.

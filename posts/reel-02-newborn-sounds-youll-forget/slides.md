# Reel 02 - Newborn Sounds Youll Forget

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Keepsake · CTA Save
Spec: `Automation Engine/reels/reel-copy-spec.md` · Renderer: `Automation Engine/reels/drift_reel.py`
Source: adapted from carousel `01 - Newborn Sounds Youll Forget` (5.96% ER, published Jul 27–Aug 2 —
at/above the Keepsake lane average for that window, ≥3 weeks old as of this run).

This post has NO slide-N.png files. Its single asset is `reel.mp4`, attached to Buffer as a
`video` asset (not an image carousel). Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

## Card (see card.json for the machine-readable source)
headline: The tiny newborn sounds you'll forget faster than you expect
items:
  - The squeaky grunts while they settle, like they're arguing with sleep
  - The long sigh right after a feed, when their whole body lets go
  - The gulp of a 3am bottle, loudest thing in a silent house
  - The cry that is already changing into a different cry
turn: You'll remember the photos. The sounds go quietly, first.

CTA = Save (caption ask). NO website ask — a reel has no closing card, so it structurally
cannot carry the LOCKED website CTA (reel-copy-spec §7.4).

Added 2026-08-16 to satisfy the new minimum-2-reels/week standing rule (Ben).

---

## ⚠️ ITEMS REWRITTEN 2026-08-16 — read this before writing another reel

Ben, on seeing the first version in the review workbook: *"the reel on the spreadsheet — it looks
like carousel text. didn't we make it a part of the process to embellish a little bit so it is not
skimmable like a list?"*

He was right, and the first version was **written correctly against a stale spec.**

The original items were: *The squeaky grunts while they settle · The sigh right after a feed · The
gulp of a 3am bottle · The cry that's already changing · The coos before real words.* Five items,
24–36 characters, 5–6 words each, every one opening "The ___". On the rendered card **four of the
five fit on a single line**, so the whole thing read as a bulleted list you can skim in two seconds
— which is the one thing this format exists not to be. It was carousel copy, because it was adapted
straight from a carousel and nothing pushed back.

**What changed, measured against Reel 01 (published Aug 13, the version we revised into):**

| | Reel 01 (published) | Reel 02 before | Reel 02 now |
|---|---|---|---|
| items | 4 | 5 | **4** |
| chars/item | 47–66 | 24–36 | **53–69** |
| words/item | 9–13 | 5–6 | **10–13** |
| length spread | 19 | 12 | **16** |
| lines each on card | 2 | 1 | **2** |

**The mechanism: every item now carries a payoff clause after a comma** — *"…like they're arguing
with sleep," "…when their whole body lets go," "…loudest thing in a silent house."* That clause is
what makes the eye slow down. Reel 01 does exactly this on every line (*"…heavier than you
expected," "…that belongs to nobody but the two of you"*). Without it you have a list; with it you
have something she reads twice, which is the entire watch-time thesis of the format.

**Fewer items, longer items.** 4 embellished beats 5 terse — total word count barely moves (65 vs
47, both inside the 45–70 target) but the read time per line roughly doubles.

`reel-copy-spec.md` §3 has been corrected — it had said *"≤32 characters each"* and *"fragments,
not sentences,"* and used almost this exact terse shape as its ✅ example. That was the pre-revision
rule and it never got updated when we changed Reel 01.

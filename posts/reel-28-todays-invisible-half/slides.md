# REEL 28 - Todays Invisible Half

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Warmth · CTA **Share**
(asked in the caption) · slot AM (Tue 9/22) · avatar newborn · NOT product-forward · no website ask.

Premise **#58** from `hook-bank.md` bucket **A · READY** (*"The small things you did for your
newborn today that nobody saw…"*). Drawn per the portfolio order; no new premise was written.

⚠️ **THE HOOK IS DELIBERATELY SHAPED AS THE SHARE ITSELF** — this is the week's one craft
experiment and it comes straight out of the 2026-09-16 read. INSP 11 produced **150 shares at
28.95/1k**, the best share result the account has ever had, on a hook that *is* the forward:
*"send this to the person whose face keeps turning up in your baby's"*. In the same window six
posts asked for a share or a save in the caption and earned **zero between them**, including this
lane's own REEL 18 (1,233 views, Share ask, 0 shares).

**The hypothesis in one line:** the share ask at the end of a caption is not what produces shares —
a hook the reader can only satisfy by forwarding it is. Warmth is the right lane to test it in
because shares are the metric the lane exists to move and it is currently at 0.00/1k across three
reel outings.

**Paired container test, same lane, same week.** This row is the REEL; post **84** (Sat 9/26 Mid) is
the CAROUSEL. Same lane, two containers, seven days — Warmth as a reel has produced ~0 shares three
times running while the lane's carousels have not (post 70: 379 views, **10.55 sh/1k**). Read them
against each other, not against the lane average.

Rule 1 (open a loop) does not apply to a reel — nothing can be withheld on one frame
([[drift-reel-format]]). Recognition replaces curiosity, and the four items are the recognition.

## Card (see card.json for the machine-readable source)
headline: Send this to someone who did a hundred things today that nobody noticed
items:
  - The 4am change done in the dark, heard by no one
  - The bottle you warmed and then didn't need, poured away
  - The forty minutes of bouncing that finally worked, in an empty room
  - The load of laundry started at eleven because you knew you'd need it tomorrow.
turn: None of it was witnessed by anyone. All of it still got done anyway.


## Caption
The invisible half of a newborn day that nobody is awake to see.

There is no witness to most of what you did today, which is not the same as it not counting. Somebody should say it out loud, so here it is in writing.

Send this to whoever is doing it tonight. 🤍

#newmom #fourthtrimester #newparents #momsupport #postpartum

## Hashtags
#newmom #fourthtrimester #newparents #momsupport #postpartum


## ⚠️ ITEM SPREAD IS 11 CHARS, NOT THE 15 THE SPEC WANTS — and it is not fixable on this card

`check_reel_copy.py` flags this row for item lengths spanning only 11 characters. It was
worked, rendered and re-rendered four times, and **the spread rule and the two-line wrap rule are
jointly unsatisfiable on this particular card.** The arithmetic, because it will recur:

- The renderer auto-fits type to fill a safe band, so a card with a SHORT headline gives the items
  a **bigger** font — which lowers the ceiling at which an item still wraps to two lines. On this
  card that ceiling is about **60 characters**.
- The spec's own floor is **45 characters** per item.
- A 45–60 band can only produce a spread of **15 at the absolute maximum**, and only if one item sits
  exactly on the floor and another exactly on the ceiling.
- Pushing the longest item to 60 to hit the spread put a **three-line item with a one-word widow**
  on the card. That was rendered and looked at; the version in this folder is the two-line one.

**The wrap is the visible failure and the spread is a numeric proxy for it** — both rules exist to
stop the right edge going flush and the card reading as a skimmable list. The rendered card has a
ragged right edge and four two-line items, which is what the rules are protecting. The proxy is the
thing that gave.

**Recorded rather than ground out.** The generalisable fix belongs in the spec, not in this post:
either the 45-char floor drops for short-headline cards, or the spread rule becomes a *rendered*
check (measure the actual line-end positions in the PNG) instead of a character-count one. Raised in
`digest-2026-09-17.md` for Ben.


---

## ✅ REVISED 2026-09-17 per Ben's review — his wording, applied verbatim

| | His | Mine |
|---|---|---|
| **cover** | Send this to someone who did a hundred things today that nobody noticed | Send this to whoever did today's invisible half |
| 3 | The forty minutes of bouncing that **finally** worked, in an empty room | …that worked… |
| 4 | The load of laundry started at eleven **because you knew you'd need it tomorrow.** | …purely for tomorrow |

**His cover is the better line and it sharpens the experiment.** Mine used "invisible half" as a
figure of speech the reader has to decode; his names the actual thing — *a hundred things nobody
noticed* — which is what makes the forward land on a specific person. The share mechanism this row
is testing is *the hook IS the share*, and a hook that is easier to act on tests it better.

⚠️ **Two costs, both his words, neither changed:**
- **Item 4 wraps to three lines** (78 chars against the ~60 the auto-fit allows at this font). It
  reads fine — it is the last item and the extra line sits above the turn, not against the byline.
- **The card is 74 words** against the spec's 45–70, and the renderer prints *"TOO LONG — they'll
  bail."* Worth weighing lightly: the 2026-09-12 read found that **no reel has ever hit the
  2.5–3.0 loop target** the word budget was derived from (11 measured reels: min 0.96, median 1.34),
  so that budget rests on a reading-speed estimate the data contradicts.

✅ **And his edits fixed the shape problem this card had.** The spread note below was written when
the four items spanned only 11 characters. His run **48 → 78, a spread of 30**, comfortably past the
≥15 the rule wants. The constraint conflict described below is real and still worth fixing in the
spec, but **it no longer applies to this card.**

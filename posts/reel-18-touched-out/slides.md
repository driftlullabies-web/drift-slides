# REEL 18 - Touched Out

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Warmth · CTA Share · slot AM (Sun 9/13)
NOT product-forward, no website ask.

Reworked in response to Ben's Sep 7 workbook notes (2026-09-03). The copy below is the engine's,
not his, so it is deliberately NOT marked with the linter-exemption phrase — these items must pass
check_reel_copy.py and check_caption_overlap.py on their own merits.

**Converted from carousel 81 this run**, per Ben's daily-reel instruction. Hook #128 kept.

Warmth is a strong reel fit — the lane's own metric is shares and shares are what the format
produces. Second Warmth reel of the week after REEL 11 (Mon), six days apart and on a completely
different premise (advice you can ignore vs. the physical cost of being needed), so the pair does
not read as one idea twice.

⚠️ The turn is the load-bearing line here and it is written to **absolve, not to convict** — per
drift-generic-closer-ctas' second rule, a turn must never land on guilt. "Needing a minute alone
isn't wanting less of them" answers the accusation the premise raises rather than repeating it.
Item 3 ("flinching a little when they reach, and hating that you did") is the riskiest line on the
card; it stays because the turn immediately releases it, and it is the line most likely to make her
send this to someone.

Carousel 80 ("if today was mostly just keeping them alive") was the other Sunday candidate and was
benched — its premise collides with INSP 10, which is also benched this week for the same reason.

## Card (see card.json for the machine-readable source)
headline: You don't have to love being touched all day
items:
  - The fourth hour of a hand inside your collar, with no end to it
  - Wanting the shower more than the nap, some days
  - Flinching a little when they reach, and hating that you did
  - Loving them completely, and needing your body back
turn: Needing a minute alone isn't wanting less of them.

CTA: Share (caption ask only — no closing card on a reel; not the website ask).

## Caption
Touched out is a real thing new moms mostly don't say out loud.

It isn't a sign you're doing it wrong, and it isn't about them. Two things stay true at the same time and neither one cancels the other.

Send this to a mom who'd never admit it. 🤍

#newmom #fourthtrimester #postpartum #realmotherhood #momtok

## Hashtags
#newmom #fourthtrimester #postpartum #realmotherhood #momtok

Rebuild with:
    python3 "Automation Engine/reels/drift_reel.py" --json card.json --out .

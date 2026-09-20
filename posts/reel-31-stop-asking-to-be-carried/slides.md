# REEL 31 - Stop Asking To Be Carried

Format: **REEL** (single-image 6s loop, 1080x1920 MP4) · bg cream · lane Keepsake · CTA **Save**
(asked in the caption) · slot AM (Sat 9/26) · **avatar: under-3** · NOT product-forward · no website
ask.

**Written fresh for the avatar, not translated from a newborn hook.** `avatars.md` is explicit that
*"The toddler moments you'll forget first"* is a newborn hook wearing a hat. Every item here is a
loss that can only happen to a walking, talking child — a mispronunciation, arms up in a parking
lot, the nap ending, the same clip on repeat. None of them transfers back to a newborn card, which
is the test.

Register held identical to the newborn rows per `avatars.md` ("a toddler card and a newborn card
should sound like the same person wrote them") — future-loss/regret, the ledger's best mechanism at
1.63x median ER. The difference is the items, not the voice.

⚠️ **Drift's product language is newborn-shaped and none of it appears here** — no "newborn", no
"3am", no "fourth trimester". This row carries no website ask, so no product claim had to be
stretched to fit an older child.

Item collision: checked against the trailing 7–10 days and the whole week. Nothing in the account
has used a mispronunciation, a parking lot, or the end of the nap.

## Card (see card.json for the machine-readable source)
headline: Nobody warns you when your toddler stops asking to be carried
items:
  - Or when they stop saying that word the wrong way, the one you carefully did not correct.
  - Arms up in a parking lot, gone with no announcement
  - The nap that doesn't happen one Tuesday, and then never again
  - Being asked "Watch This!" every thirty seconds again. And again.
turn: None of these end on a day you would have marked.
markers: false   (no dashes — the items are continuous lines, not a list)


## Caption
Toddler stages that end quietly, with nobody announcing the last day.

The newborn losses at least get talked about. These ones just stop, usually on an ordinary weekday, and you work out weeks later that it already happened.

Save this if yours is right in the middle of it. 🤍

#toddlermom #toddlerlife #momlife #motherhood #momtok

## Hashtags
#toddlermom #toddlerlife #momlife #motherhood #momtok


---

## ✅ REVISED 2026-09-17 per Ben's review — his wording verbatim, and BULLETS ARE OFF

| | His | Mine |
|---|---|---|
| **cover** | Nobody warns you **when** your toddler **stops** asking to be carried | Nobody warns you **that** your toddler **will stop** asking to be carried |
| 1 | **Or when they stop saying that word the wrong way, the one you carefully did not correct.** | The word they say wrong that you'll never correct |
| 2 | Arms up in a parking lot, **gone** with no announcement | …the last one arriving with no announcement |
| 4 | Being asked **"Watch This!"** every thirty seconds again. And again. | Being asked to watch the same thirty seconds again. And again. |

> *"Is this better not as bullet points, just lines since the hook is not a 'container' just the
> first idea?"*

**Yes, and it is a format change rather than a preference — his own edit is what makes it necessary.**
Changing the cover from *"that your toddler **will stop**"* to *"**when** your toddler **stops**"*
turns the headline from a container that introduces a list into **the first clause of a running
sentence**, which item 1 then continues: *"Or when they stop saying that word…"*. A lavender dash in
front of a word like "Or" reads as a list item interrupting its own sentence.

**Implemented as a renderer option, not a one-off.** `drift_reel.py` now takes `"markers": false` in
the card JSON: the dashes are dropped and the block left-aligns under its own centre. **Default stays
`true`**, so no published reel moves — verified, and the same discipline as the 1.80 headline ratio
(a change derived from one card must not alter what shipped).

⚠️ His item 1 runs to three lines at 88 characters. Without markers that reads as a paragraph rather
than an overlong bullet, which is the point — left alone.

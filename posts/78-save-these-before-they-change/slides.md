# 78 - Save These Before They Change

Format: carousel · bg cream #F4F0E6 · lane Keepsake · CTA **Share** · slot Mid (Sat 9/19)
Hook #3 from hook-bank.md, READY bucket (future-loss/regret family — this week's ONE draw from
that family per the bank's own rule: "draw them as replacements for tired siblings, never as
additional slots in the same week").

## Cover
Save these before your newborn changes again…

## Items
1 The hiccups that turn up after a feed, every single time
2 The tiny bald patch on the back of their head, from all that lying down
3 The socks — impossibly small, and off by lunchtime anyway
4 The first time they look for you with their eyes instead of just noise
5 How ridiculous the sleeves look on arms that short

## Closer (Share)
Send this to a mom in the middle of it.

## Caption
Newborn details worth writing down this week.

Not the milestones — nobody forgets the milestones. It's the boring specifics that go, and they go without any announcement at all.

Send this to a mom in the middle of it. 🤍

#newmom #fourthtrimester #newbornlife #keepsake #momtok

## Hashtags
#newmom #fourthtrimester #newbornlife #keepsake #momtok

---

## ⚠️ ITEMS REPLACED 2026-09-03 — Ben's review

His note on this row in the Sep 7 workbook: *"content is feeling repetitive from previous weeks.
Try out some from the lists I sent above in the spreadsheet."* He was right twice over. The old
items led with "the exact weight of them asleep on your chest" and "the sound they make before
they're really crying" — **both of which the previous REEL 13 draft also used, in the same week.**
That is precisely the failure [[drift-item-collision-check]] exists to catch and it slipped through
again, because the dedupe pass compared hooks and premises and never compared item lines.

New items are drawn from list A of `Social Media Carousel Posts/newborn-detail-bank.md`, choosing
only entries NOT spent by REEL 13 or REEL 14 this week, and logged there.

⚠️ **Item 1 replaced again 2026-09-04, by the new `check_item_collisions.py` on its first run.** The
rework had drawn bank item A2 ("their whole hand wraps around just one of your fingers") — which is
the same image as **published Reel 01**'s third item, *"A whole hand wrapped around one of your
fingers"* (shipped Aug 13). The bank contains images the account has already used; drawing from it
is not a substitute for the collision check, which is exactly what the bank file's own header warns.
Replaced with the hiccups (A17, genuinely unspent). Items stay terse on
purpose — this is a carousel, and the payoff-clause register belongs to reels.

**This post is on the BENCH for the week of Sep 7** (three lanes sit below their floors once the
Collecting Ideas series takes seven slots; the bench is where the overflow lives). It is finished
copy, ready to swap in or to lead the Sep 14 week.


---

## ⚠️ CTA CHANGED Save -> Share, 2026-09-10 (weekly-run step 2a)

Rolled off the bench into **Fri 9/18 Mid** as the week's Keepsake carousel. Its CTA moved from Save
to **Share**, and the closer and the caption's ask line moved with it. Copy of the cover and the
five items is **unchanged** — this is a CTA reweight, not a rewrite.

**Why.** Step 2a: *"Shares are where the account is furthest behind and we ask for a share mostly in
Warmth. Let Keepsake carry a Share ask on at least one row per week and read the result."* Keepsake
is the account's **share desert** — nine of fifteen carousels earned literally zero shares
([[drift-keepsake-share-desert]]) — and this week's read did nothing to soften that: the one
Keepsake post in the window returned 2.36 shares/1k. This row is where the ask itself gets tested,
holding the lane and the container constant.

The new closer passes `check_closers.py`'s own carve-out for Share closers: it names a recipient,
which is the shape a Share ask is supposed to have, and it reads sensibly pasted onto any other
Keepsake post.

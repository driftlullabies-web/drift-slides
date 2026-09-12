# Hook Stack — 01 - Baby Growing Too Fast

Format: carousel · **bg CREAM `#F4F0E6`** · lane **Lullaby-subject** · 6 slides
CTA: **Website (hook-stack card)** · Sound: TBD at queue time · 🤍 in caption only
Angle: **E · keepsake artifact / permanence** — the song as the thing that holds the season.

⚠️ **Product-forward.** Its subject is the Drift song, so it counts against the product-forward
group (`Social Media Carousel Posts/product-forward-rotation.md`, weekly run step 3a).

⚠️ **Rule 7 conflict — do NOT run this in the same week as Hook Stack 02.** Both carry the same
premise and the same promise (you'll miss these moments → a nightly lullaby anchors them → Drift
writes one about your baby). Different words, same post. Space them a week apart minimum.

⚠️ **Rule 1 (cover must open a loop) is bent, on purpose.** The super hook ends on a complete
sentence with a period — a "period hook" by the letter of the rule. It keeps the loop open a
different way, by leaving "this" undefined. The lane reading for hook-stacking is NOT YET WRITTEN.

## Cover
hook: If you already feel like your baby is growing too fast, stop scrolling.

## Body
2 — No one tells you how many little moments you're going to miss.

3 — Or how to hold onto the feeling before it fades.
    You won't remember every detail.
    *(two separate thoughts, spaced — render_teaser)*

4 — The way they curl into your chest won't last.
    Their little voice will sound different.
    The way they laugh right now will be different next year.
    *(LIST of three, lavender middots — render_teaser(..., dots=True))*

5 — And that's okay.
    You just need something that helps you hold onto the ones that matter.
    *(two separate thoughts, spaced)*

## Closer (website — hook-stack card)
Lead: "So sing to them. Every night."
Lead italic: "Because one day, that song might bring you right back here."
Ask: "But don't just sing them any lullaby."
Ask: "Sing one that's about *them.*"
Imperative: "Make their personalized lullaby today"
Guarantee: YES — the ask is a purchase. (Renders automatically; never write it here.)

---

## Render

```
render_cover(hook, slide-1)
render_teaser([...], slide-2)
render_teaser([...], slide-3)
render_teaser([...], slide-4, max_size=64, gap_ratio=1.30, dots=True)
render_teaser([...], slide-5)
render_cta_hookstack(slide-6, lead=, lead_italic=, ask_lines=, imperative=, guarantee=True)
```

⚠️ Put trailing punctuation INSIDE the emphasis markers — `*them.*` not `*them*.` — or
`_parse_emph` splits the period into its own token and renders it with a leading space.

## Caption
How to hold onto this stage of your baby — the feeling, not just the photos.

You don't need to be a good singer, and it doesn't have to be a special song. What seems to matter is that it's the same one, every night, in the same quiet part of the day — so it becomes theirs.

Don't just sing them any lullaby. Sing one that's about them — link in bio. 🤍

#newmom #newbornlife #keepsake #babylullaby #momtok

## Hashtags
#newmom #newbornlife #keepsake #babylullaby #momtok

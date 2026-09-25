#!/usr/bin/env python3
"""
build_ad01.py: one-off build for AD 01 · Nobody Tells You (Emma's Song).

WHY A BESPOKE SCRIPT (same precedent as ig_reels/_build_pov10_emma_reel.py)
    drift_reel_hooks.render_hook_reel() deliberately SKIPS the sticky note on a CTA card: the
    note normally replaces the byline, and a CTA card has no byline. This ad needs a note anyway,
    because the note is the bridge: it tells her the sound she's hearing IS the product. So the
    note says "sound on / this is Emma's song" and is slapped onto the empty top-right corner
    above the headline instead of the bottom. Nothing in drift_reel.py or drift_reel_hooks.py is
    modified; this script only imports their functions.

    It also bakes AUDIO in (the hooks renderer writes a silent track): a clip of Emma's lullaby
    (heartsong-app/site/audio/emma.mp3, the homepage sample), cut so her name lands inside
    the loop, with short fades so the loop seam doesn't click.

USAGE
    python3 build_ad01.py --card-only                       # settled card.png for review
    python3 build_ad01.py --audio-start 14.0 --seconds 10    # full reel.mp4 with the song
"""
import argparse, json, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REELS = os.path.join(HERE, "..", "..", "Automation Engine", "reels")
sys.path.insert(0, REELS)
import drift_reel as R            # noqa: E402
import drift_reel_hooks as H      # noqa: E402

SONG = os.path.expanduser("~/mnt/heartsong-app/site/audio/emma.mp3")
# The note sits at the TOP of the safe band, centred, and the whole card is pushed down to make room
# for it. First draft put it in the top-right corner, which is under TikTok's tabs (top ~180px) and
# its action rail (x > 940): drift_reel.py's SAFE_TOP / rail comment. Caught in self-audit 2026-09-23.
CARD_PNG = "card.png"
SAFE_TOP_OUT = 200                # output px (drift_reel.SAFE_TOP / SS)
NOTE_GAP_OUT = 56                 # air between the pill and the note below it


def make_square_note(card, seed=3):
    """A near-square sticky pad in drift_reel_hooks.make_note's exact paper + tape treatment.
    card["note"] = {"lines": [...], "font": px, "line_h": px, "w": px, "h": px, "pad_top": px}
    (output px). Returns (sprite, y offset of the writing's last baseline from the paper top)."""
    cfg = card["note"]
    s_ = R.s
    rng = np.random.default_rng(seed)
    f = H.hand_font(s_(cfg["font"]), 600)
    lh = s_(cfg["line_h"])
    nw, nh = s_(cfg["w"]), s_(cfg["h"])
    lines = cfg["lines"]
    pad_top = s_(cfg["pad_top"])
    yy = np.linspace(0, 1, nh)[:, None, None]
    paper = np.ones((nh, nw, 3), np.float32) * np.array(H.NOTE_COLOR, np.float32)
    paper *= (1.03 - 0.05 * yy) - 0.07 * np.clip((yy - 0.82) / 0.18, 0, 1) ** 2
    paper += rng.normal(0, 2.2, (nh, nw, 1))
    note = Image.fromarray(np.clip(paper, 0, 255).astype(np.uint8)).convert("RGBA")
    from PIL import ImageDraw
    d = ImageDraw.Draw(note)
    for i, ln in enumerate(lines):
        dx = (-s_(6), s_(8))[i % 2]                       # handwriting never sits dead-centre
        d.text((nw / 2 + dx, pad_top + lh * (i + 0.5)), ln, font=f, fill=H.NOTE_INK + (240,), anchor="mm")
    text_bottom = pad_top + lh * len(lines)
    tw_, th_ = s_(170), s_(54)
    tape = Image.new("RGBA", (tw_, th_), (0, 0, 0, 0))
    td = ImageDraw.Draw(tape)
    zig = 7
    left = [(rng.uniform(0, s_(9)), th_ * i / zig) for i in range(zig + 1)]
    right = [(tw_ - rng.uniform(0, s_(9)), th_ * (zig - i) / zig) for i in range(zig + 1)]
    td.polygon(left + right, fill=(250, 248, 238, 150))
    tape = tape.rotate(-4, resample=Image.BICUBIC, expand=True)
    m = s_(50)
    sprite = Image.new("RGBA", (nw + 2 * m, nh + 2 * m), (0, 0, 0, 0))
    sprite.alpha_composite(note, (m, m))
    sprite.alpha_composite(tape, (m + nw // 2 - tape.width // 2 + s_(6), m - tape.height // 2 + s_(4)))
    return sprite, text_bottom


def _force_eyebrow_break(card):
    """Forced line breaks in the CTA, which drift_reel's greedy wrap can't express.
    card.json: "eyebrow_break_after": "happen."  (so "A" isn't stranded at the end of line 1)
               "ask_break_after": "ready,"       (Ben 2026-09-24: "When you're ready," / "we can help find their song")
    drift_reel._wrap_toks is wrapped so ONLY those exact token runs are split; every other wrap on
    the card is untouched."""
    rules = []
    for key, text in (("eyebrow_break_after", card["cta"].get("eyebrow")), ("ask_break_after", card["cta"].get("ask"))):
        word = card.get(key)
        if word and text:
            target = R.strip_emph(text).split()
            if word in target:
                rules.append((target, target.index(word) + 1))
    if not rules:
        return None
    orig = getattr(R._wrap_toks, "_orig", R._wrap_toks)
    def wrap(toks, fp, fe, maxw):
        words = [t[0] for t in toks]
        for target, i in rules:
            if words == target:
                return orig(toks[:i], fp, fe, maxw) + orig(toks[i:], fp, fe, maxw)
        return orig(toks, fp, fe, maxw)
    wrap._orig = orig
    R._wrap_toks = wrap
    return orig


def _cta_overflows(card, png):
    """drift_reel clamps the LINK IN BIO pill to the fit ceiling when the CTA block runs long, which
    is how the pill ended up on top of the ask once. It only SAYS so when quiet=False, so ask it."""
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        R.render_reel_card(card["headline"], card["items"], card.get("turn"), png,
                           bg=getattr(R, card.get("bg", "BG_CREAM"), R.BG_CREAM),
                           credibility=True, cta=card.get("cta"), quiet=False)
    return "CTA block runs past" in buf.getvalue()


def build(card, seconds, fps=30, card_only=False, note_at=3.0, zoom=0.016, drift=4, hold=0.25, rest=0.06):
    png = os.path.join(HERE, CARD_PNG)
    _force_eyebrow_break(card)
    # "A song can help you hold onto these moments." (Ben, 2026-09-24) is 749px at the 34px item size,
    # past the eyebrow's 680px budget, and a third eyebrow line overflows the CTA. card.json may widen
    # the eyebrow column for this card only; 760 keeps the right edge at ~921px at peak zoom, still
    # left of TikTok's action rail (~940). Never set it wider than 780.
    if card.get("eyebrow_maxw"):
        R.CTA_EYEBROW_MAXW = R.s(min(card["eyebrow_maxw"], 780))
    if card.get("pill", True) is False:
        R._draw_pill = lambda *a, **k: None     # the note takes the pill's place (option B)
    # SQUARE STICKY NOTE (Ben, 2026-09-24: "make the sticky note a little bigger ... it is not very
    # 'sticky note shaped'. It can go into the danger area at the bottom, it's not the writing, just
    # the picture"). House make_note() sizes the paper to the text, which gives a long thin strip for
    # a long line. This draws a near-square pad in the same paper/tape style, with the WRITING kept
    # inside SAFE_BOTTOM and only the paper's lower margin allowed into TikTok's caption band.
    note, text_bottom_off = make_square_note(card)
    note_margin = R.s(50)
    angle = card.get("note_angle", -3.0)
    paper_h = note.height - 2 * note_margin
    gap_out = card.get("note_gap", NOTE_GAP_OUT)
    need = R.s(gap_out) + text_bottom_off + H.NOTE_TILT_SLACK   # pill -> last line of writing
    bg = getattr(R, card.get("bg", "BG_CREAM"), R.BG_CREAM)
    saved = (R.CTA_MAX_Y, R.SHIFT_FLOOR)
    try:
        R.SHIFT_FLOOR = R.SAFE_BOTTOM - need
        drop = 0
        for _ in range(24):
            R.CTA_MAX_Y = saved[0] - drop
            calls = H._spy_render(card, png, credibility=True)
            bottom = H._ink_bottom(Image.open(png).convert("RGB"), bg)
            if bottom + need <= R.SAFE_BOTTOM:
                break
            drop += R.s(16)
        else:
            raise SystemExit("card too dense to fit the note's writing above SAFE_BOTTOM")
        if _cta_overflows(card, os.path.join(tempfile.gettempdir(), "ad01_check.png")):
            raise SystemExit("fit reached the point where drift_reel clamps the pill onto the ask; "
                             "make the note shorter (pad_top / line_h / note_gap) instead")
    finally:
        R.CTA_MAX_Y, R.SHIFT_FLOOR = saved
    base_img = Image.open(png).convert("RGB")
    shift = H._rule_shift(base_img)
    note_top = bottom + R.s(gap_out) + H.NOTE_TILT_SLACK // 2
    room = drop
    print(f"  square note: writing ends at y {(note_top + text_bottom_off) / R.SS:.0f} (safe {R.SAFE_BOTTOM / R.SS:.0f}), "
          f"paper ends at y {(note_top + paper_h) / R.SS:.0f}")
    head_calls = []
    for c in calls:
        if c["anchor"] == "mm" and c["fill"] == R.NAVY:
            head_calls.append(c)
        elif head_calls:
            break
    hl = H.Highlighter(H._phrase_boxes(head_calls, card["visual_hook"]["highlight"], shift))

    nx = R.CX
    ny = note_top + paper_h / 2
    paper_w = note.width - 2 * note_margin
    print(f"  note: {paper_w / R.SS:.0f}x{paper_h / R.SS:.0f}px, top at y {note_top / R.SS:.0f}, bottom {(note_top + paper_h) / R.SS:.0f} (safe {R.SAFE_BOTTOM / R.SS:.0f}); fit ceiling lowered {room / R.SS:.0f}px")

    T = seconds
    h0, h1 = 0.30, 0.72
    t_note = max(h1 + 0.08, note_at)
    base = np.asarray(base_img, dtype=np.float32)
    sw, sh = base_img.size

    def settled():
        arr = base.copy(); hl.apply(arr, 1.0, 1.0)
        img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        H._place(img, note, nx, ny, 1.0, 1.0, angle, 1.0, R.s(7), R.s(6), 0.30)
        img.resize((R.OUT_W, R.OUT_H), Image.LANCZOS).save(png)

    if card_only:
        settled(); print("  card.png (settled)"); return

    silent = os.path.join(tempfile.gettempdir(), "ad01_silent.mp4")   # scratch lives outside the synced folder
    proc = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", f"{R.OUT_W}x{R.OUT_H}", "-r", str(fps), "-i", "-",
         "-c:v", "libx264", "-profile:v", "high", "-crf", "18", "-pix_fmt", "yuv420p",
         "-movflags", "+faststart", silent], stdin=subprocess.PIPE)
    n = int(seconds * fps)
    last_key = last = None
    for i in range(n):
        t = i / fps
        fade = 1 - H._ss(H._clip01((t - (T - 0.34)) / 0.30))
        hp = 1 - (1 - H._clip01((t - h0) / (h1 - h0))) ** 2
        st = H.note_state(t, T, t_note, angle, exit=True)
        key = (round(hp, 4), round(fade, 4),
               tuple(round(v, 2) if isinstance(v, float) else v for v in st.values()))
        if key == last_key:
            img = last
        else:
            arr = base.copy(); hl.apply(arr, hp, fade)
            img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
            if st["show"]:
                H._place(img, note, nx + st["dx"], ny + st["dy"], st["sx"], st["sy"], st["ang"],
                         st["a"], st["soff"], st["sblur"], st["sop"])
        last_key, last = key, img
        shake = 0.0   # no camera bump on the slap (Ben, 2026-09-24: "a jostle of the image/text"); the note still squashes
        e = R._ease(i / n, hold, rest)
        z = 1.0 + zoom * e
        cw, ch = sw / z, sh / z
        cy = sh / 2.0 + (drift * e) * (sh / R.OUT_H) + shake
        cy = min(max(cy, ch / 2.0), sh - ch / 2.0)
        frame = img.resize((R.OUT_W, R.OUT_H), Image.LANCZOS,
                           box=(sw / 2 - cw / 2, cy - ch / 2, sw / 2 + cw / 2, cy + ch / 2))
        proc.stdin.write(frame.tobytes())
    proc.stdin.close(); proc.wait()
    if proc.returncode:
        raise RuntimeError("video encode failed")
    settled()
    return silent


def mux(silent, audio_start, seconds, fade_in=0.12, fade_out=0.45):
    out = os.path.join(HERE, "reel.mp4")
    af = (f"atrim=start={audio_start}:duration={seconds},asetpts=PTS-STARTPTS,"
          f"afade=t=in:st=0:d={fade_in},afade=t=out:st={seconds - fade_out}:d={fade_out},"
          f"volume=-2.5dB")
    # AUDIO CHAIN (revised 2026-09-23, Ben: "the song quality on tiktok is crappy"). Source is Suno's
    # 180kbps MP3 and TikTok re-encodes again, so do LESS: no loudnorm (dynamic mode compresses/pumps),
    # no resample (source is 48k), flat -2.5dB so the -0.08dBTP peaks get headroom before TikTok's
    # encoder, AAC 320k so our generation adds as little as possible.
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", SONG,
                    "-filter_complex", f"[1:a]{af}[a]", "-map", "0:v", "-map", "[a]",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-ar", "48000",
                    "-t", str(seconds), "-movflags", "+faststart", out], check=True)
    os.remove(silent)
    print(f"  reel.mp4  ({os.path.getsize(out) / 1e6:.1f} MB, {seconds}s, audio from {audio_start}s)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--card-only", action="store_true")
    ap.add_argument("--card", default="card.json", help="card spec (lets option cards live side by side)")
    ap.add_argument("--audio-start", type=float)
    ap.add_argument("--seconds", type=float, default=10.0)
    a = ap.parse_args()
    card = json.load(open(os.path.join(HERE, a.card), encoding="utf-8"))
    CARD_PNG = "card.png" if a.card == "card.json" else os.path.splitext(a.card)[0] + ".png"
    if a.card_only:
        build(card, a.seconds, card_only=True)
    else:
        if a.audio_start is None:
            ap.error("--audio-start is required for the video (where the name-line begins in emma.mp3)")
        mux(build(card, a.seconds), a.audio_start, a.seconds)

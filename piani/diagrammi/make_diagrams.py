#!/usr/bin/env python3
"""Genera i diagrammi del workshop 5 giorni come PNG slide-ready (palette brand)."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.dirname(os.path.abspath(__file__))
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Palette brand
BLU = (18, 40, 54)        # #122836
BLU2 = (32, 64, 84)
ORO = (201, 168, 76)      # #C9A84C
ORO_L = (226, 196, 106)
BORG = (75, 18, 48)       # #4b1230
BORG2 = (110, 35, 72)
GREEN = (31, 61, 52)      # verde profondo (digitale 12MC)
PURP = (74, 45, 85)
WHITE = (255, 255, 255)
CREAM = (250, 247, 241)
INK = (28, 32, 36)
MUTE = (110, 118, 125)
RED = (176, 42, 42)

def F(sz, bold=True):
    return ImageFont.truetype(FB if bold else FR, sz)

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def box(d, xy, fill, text, font, tcol=WHITE, sub=None, subfont=None, radius=22, outline=None, ow=0):
    x0, y0, x1, y1 = xy
    d.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=ow)
    cx = (x0 + x1) // 2
    lines = wrap(d, text, font, (x1 - x0) - 36)
    sub_lines = wrap(d, sub, subfont, (x1 - x0) - 36) if sub else []
    lh = font.size + 6
    slh = (subfont.size + 4) if sub else 0
    total = len(lines) * lh + (len(sub_lines) * slh + 8 if sub else 0)
    ty = (y0 + y1) // 2 - total // 2
    for ln in lines:
        d.text((cx, ty), ln, font=font, fill=tcol, anchor="ma")
        ty += lh
    if sub:
        ty += 6
        for ln in sub_lines:
            d.text((cx, ty), ln, font=subfont, fill=tcol, anchor="ma")
            ty += slh

def arrow(d, p0, p1, col=ORO, w=7, head=16):
    import math
    p0 = (int(p0[0]), int(p0[1])); p1 = (int(p1[0]), int(p1[1]))
    d.line([p0, p1], fill=col, width=w)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (-1, 1):
        a = ang + s * 0.45
        hp = (int(p1[0] - head * math.cos(a)), int(p1[1] - head * math.sin(a)))
        d.line([p1, hp], fill=col, width=w)

def canvas(w, h, title, subtitle=None):
    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, 8], fill=ORO)
    d.text((w // 2, 40), title, font=F(46), fill=BLU, anchor="ma")
    if subtitle:
        d.text((w // 2, 100), subtitle, font=F(26, False), fill=MUTE, anchor="ma")
    return img, d

# ---------- 1. LA MACCHINA ----------
def diagram_macchina():
    W, H = 1680, 1080
    img, d = canvas(W, H, "La macchina: Digitale + Analogico")
    # DIGITALE band
    d.text((W // 2, 150), "DIGITALE — fa alzare la mano (SCALA)", font=F(28), fill=BLU, anchor="ma")
    bw, bh, gap = 470, 130, 40
    x0 = (W - (bw * 3 + gap * 2)) // 2
    digit = [("YouTube", "biblioteca / asset H24", BLU),
             ("Organico IG-FB", "autorità, non scala", BLU2),
             ("Ads", "volume prevedibile", BLU2)]
    centers = []
    for i, (t, s, c) in enumerate(digit):
        x = x0 + i * (bw + gap)
        box(d, (x, 195, x + bw, 195 + bh), c, t, F(34), sub=s, subfont=F(22, False))
        centers.append((x + bw // 2, 195 + bh))
    # LEAD pill
    ly = 430
    lead = (W // 2 - 230, ly, W // 2 + 230, ly + 92)
    for cxb in centers:
        arrow(d, (cxb[0], cxb[1] + 4), (W // 2, ly - 6))
    box(d, lead, ORO, "LEAD  VENDITORE", F(38), tcol=BLU, radius=46)
    # ANALOGICO band
    d.text((W // 2, ly + 130), "ANALOGICO — converte la mano alzata", font=F(28), fill=BORG, anchor="ma")
    ay = ly + 175
    ana = [("Chiamata", "speed-to-lead (minuti)", BORG),
           ("Referral / Centri d'influenza", "fiducia che porta clienti", BORG2),
           ("Eventi / Open House / Liste", "contatti che già ti conoscono", BORG2)]
    acent = []
    for i, (t, s, c) in enumerate(ana):
        x = x0 + i * (bw + gap)
        box(d, (x, ay, x + bw, ay + bh), c, t, F(30), sub=s, subfont=F(21, False))
        acent.append((x + bw // 2, ay + bh))
    arrow(d, (W // 2, ly + 92 + 4), (W // 2, ay - 8))
    # INCARICO
    iy = ay + bh + 70
    inc = (W // 2 - 200, iy, W // 2 + 200, iy + 92)
    for cxb in acent:
        arrow(d, (cxb[0], cxb[1] + 4), (W // 2, iy - 6), col=BORG)
    box(d, inc, BORG, "INCARICO", F(40), radius=46)
    d.text((W // 2, H - 46), "Il digitale fa alzare la mano. L'analogico la converte. È la stessa macchina.",
           font=F(24, False), fill=BLU, anchor="ma")
    img.save(os.path.join(OUT, "1-macchina.png"))

# ---------- 2. ARCO 5 GIORNI ----------
def diagram_arco():
    W, H = 1860, 760
    img, d = canvas(W, H, "L'arco dei 5 giorni")
    days = [("GIORNO 1", "Il cambio di paradigma", "analogico → digitale", BLU),
            ("GIORNO 2", "Il sistema scalabile", "organico · YouTube · ads", BLU2),
            ("GIORNO 3", "Contenuti che cercano", "i VENDITORI (non i like)", BORG2),
            ("GIORNO 4", "Modulo AI agentico", "+ l'analogico che converte", BORG),
            ("GIORNO 5", "La macchina completa", "+ prossimo livello €3.999", ORO)]
    bw, bh, gap = 320, 300, 40
    x0 = (W - (bw * 5 + gap * 4)) // 2
    y = 200
    for i, (h, t, s, c) in enumerate(days):
        x = x0 + i * (bw + gap)
        tcol = BLU if c == ORO else WHITE
        d.rounded_rectangle((x, y, x + bw, y + bh), radius=24, fill=c)
        d.text((x + bw // 2, y + 34), h, font=F(30), fill=(tcol if c != ORO else BLU), anchor="ma")
        d.line([(x + 40, y + 78), (x + bw - 40, y + 78)], fill=(ORO if c != ORO else BLU), width=3)
        ty = y + 110
        for ln in wrap(d, t, F(27), bw - 50):
            d.text((x + bw // 2, ty), ln, font=F(27), fill=tcol, anchor="ma"); ty += 34
        ty += 8
        for ln in wrap(d, s, F(22, False), bw - 50):
            d.text((x + bw // 2, ty), ln, font=F(22, False), fill=tcol, anchor="ma"); ty += 28
        if i < 4:
            arrow(d, (x + bw + 4, y + bh // 2), (x + bw + gap - 4, y + bh // 2))
    d.text((W // 2, H - 44), "1 'aha' · 1 azione · 1 ponte al giorno dopo — 90 minuti a sessione",
           font=F(24, False), fill=MUTE, anchor="ma")
    img.save(os.path.join(OUT, "2-arco-5-giorni.png"))

# ---------- 3. FUNNEL ASCENSIONE ----------
def diagram_funnel():
    W, H = 1500, 1000
    img, d = canvas(W, H, "Il funnel di ascensione", "dove porta il workshop")
    steps = [("Video manifesto + organico", "fai alzare la mano", BLU2, ""),
             ("€149 — Bootcamp", "primo passo a basso rischio", BLU, "€149"),
             ("Workshop 5 giorni", "la mappa del sistema", BORG2, "ora"),
             ("12 Masterclass", "la macchina, costruita insieme", BORG, "€3.999"),
             ("Community / Sistema Dominante", "il sistema che scala", ORO, "799€/m")]
    n = len(steps)
    sh = 110
    base_y = 250
    step_x = 90
    bw0 = 560
    for i, (t, s, c, price) in enumerate(steps):
        y = base_y + i * (sh + 30)
        x = 120 + i * step_x
        w = bw0 + i * 70
        tcol = BLU if c == ORO else WHITE
        d.rounded_rectangle((x, y, x + w, y + sh), radius=18, fill=c)
        d.text((x + 30, y + sh // 2), t, font=F(30), fill=tcol, anchor="lm")
        d.text((x + 30, y + sh - 26), s, font=F(20, False), fill=tcol, anchor="lm")
        if price:
            d.text((x + w - 26, y + sh // 2), price, font=F(34), fill=(BLU if c == ORO else ORO_L), anchor="rm")
        if i < n - 1:
            arrow(d, (x + 60, y + sh + 2), (x + 60 + step_x, y + sh + 28), col=ORO, w=6, head=13)
    img.save(os.path.join(OUT, "3-funnel-ascensione.png"))

# ---------- 4. ORGANICO vs YOUTUBE ----------
def diagram_confronto():
    W, H = 1500, 820
    img, d = canvas(W, H, "Organico IG-FB  vs  YouTube", "perché YouTube cambia la scala (tesi Sherrard 2026)")
    cw = 640
    gap = 60
    x0 = (W - (cw * 2 + gap)) // 2
    y = 200
    ch = 520
    # left
    d.rounded_rectangle((x0, y, x0 + cw, y + ch), radius=24, fill=CREAM, outline=RED, width=3)
    d.rounded_rectangle((x0, y, x0 + cw, y + 80), radius=24, fill=RED)
    d.rectangle((x0, y + 50, x0 + cw, y + 80), fill=RED)
    d.text((x0 + cw // 2, y + 40), "ORGANICO IG / FB", font=F(32), fill=WHITE, anchor="mm")
    d.text((x0 + cw // 2, y + 108), "come l'analogico", font=F(22, False), fill=RED, anchor="ma")
    lpts = ["✕  Non scala", "✕  Si ferma quando smetti di postare",
            "✕  Effimero: il post sparisce in 48h", "✕  Conta il numero di follower"]
    ty = y + 165
    for p in lpts:
        for ln in wrap(d, p, F(24, False), cw - 70):
            d.text((x0 + 35, ty), ln, font=F(24, False), fill=INK, anchor="la"); ty += 34
        ty += 18
    # right
    rx = x0 + cw + gap
    d.rounded_rectangle((rx, y, rx + cw, y + ch), radius=24, fill=CREAM, outline=BLU, width=3)
    d.rounded_rectangle((rx, y, rx + cw, y + 80), radius=24, fill=BLU)
    d.rectangle((rx, y + 50, rx + cw, y + 80), fill=BLU)
    d.text((rx + cw // 2, y + 40), "YOUTUBE", font=F(32), fill=WHITE, anchor="mm")
    d.text((rx + cw // 2, y + 108), "biblioteca / asset che compone", font=F(22, False), fill=BLU, anchor="ma")
    rpts = ["✓  Lavora H24 (asset evergreen)", "✓  Ti TROVANO mentre cercano casa",
            "✓  2° motore di ricerca al mondo", "✓  60-80 'agenti-contenuto' che lavorano per te"]
    ty = y + 165
    for p in rpts:
        for ln in wrap(d, p, F(24, False), cw - 70):
            d.text((rx + 35, ty), ln, font=F(24, False), fill=INK, anchor="la"); ty += 34
        ty += 18
    img.save(os.path.join(OUT, "4-organico-vs-youtube.png"))

diagram_macchina()
diagram_arco()
diagram_funnel()
diagram_confronto()
print("OK diagrams generated")

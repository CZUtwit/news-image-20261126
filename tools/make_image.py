#!/usr/bin/env python3
"""Build entry.png for news-image-20261126 v4: The World in One Day — 26 Nov 2026.

v4 = v2 layout (v3's top-bar SOURCES/FIELDS and taller top-3 scenes are
reverted: v3 scored 96.9381%, below v2's 98.0686%) + one story swap: Gaza
(Israeli strikes kill 10, incl. a Hamas deputy minister) is promoted from
ALSO to a main story — the 26 Nov #1 has it as a main — and the weakest main,
Frankfurt (ECB chief appointment), drops to ALSO. Regions become EUROPE 7 /
MIDDLE EAST 5 (was 8 / 4); total stays 36 stories, 9 regions, 13 mains.
Every story was verified first reported on Thursday 26 November 2026 (UTC).
The #1's five misdated 25 Nov stories are named in DATE CHECK, not repeated.
Pure Pillow, no network, deterministic output.
Run: python3 tools/make_image.py   (writes entry.png at the repo root)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "entry.png")

W, H = 1024, 1024
M = 24
CW = W - 2 * M

PAPER = (247, 243, 234)
INK = (22, 22, 20)
RED = (176, 32, 32)
GREY = (105, 103, 96)
LGREY = (198, 194, 184)
CARD = (255, 255, 255)
CHIP = (233, 228, 215)
DOT = (172, 166, 152)
GOLD = (176, 132, 32)
GREEN = (46, 110, 62)
BLUE = (36, 84, 138)
TEAL = (24, 110, 104)
PURPLE = (90, 60, 130)

FD = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)

# (n, place, region, field, badge, badge_status, title, body, source, lon, lat)
MAIN = [
    (1, "NEW YORK", "N. AMERICA", "PARADE", "POSTPONED", "REPORTED",
     "Macy's 100th parade moved to Saturday",
     "Winter storm cuts power to 800,000+ homes; the centenary parade is postponed a day.",
     "UPI · BBC", -74.0, 40.7),
    (2, "MUMBAI", "SOUTH ASIA", "MEMORIAL", "18 YEARS", "CONFIRMED",
     "India marks 18 years since the 26/11 attacks",
     "166 killed in the 2008 Mumbai attacks; memorials across India on the anniversary.",
     "AP · Reuters", 72.88, 19.08),
    (3, "GENEVA", "EUROPE", "CHESS", "GAME 3", "ONGOING",
     "Gukesh and Sindarov draw Game 3 in Geneva",
     "60 moves, nearly five hours; the title match is level at 1.5-1.5 after three draws.",
     "The Hindu · Reuters", 6.14, 46.2),
    (4, "KUWAIT CITY", "MIDDLE EAST", "CONFLICT", "2 KILLED", "REPORTED",
     "Iranian drones kill two Italians in Kuwait",
     "Two technicians dead at a military site; Kuwait blames Iran, Tehran denies it and offers a joint inquiry.",
     "BBC · CBS", 47.5, 29.3),
    (5, "BRUSSELS", "EUROPE", "SUMMIT", "$49BN", "REPORTED",
     "EU leaders split over budget and Ukraine loan",
     "No deal on the 2028-34 budget; Germany wants cuts, Slovakia, Hungary and Czechia resist the Ukraine loan.",
     "AP · Guardian", 4.35, 50.85),
    (6, "GAZA", "MIDDLE EAST", "CONFLICT", "10 KILLED", "REPORTED",
     "Israeli strikes kill 10 in Gaza",
     "Strikes kill 10, including a Hamas deputy minister; the deadliest day since the ceasefire began.",
     "AP", 34.5, 31.5),
    (7, "JAZAN", "MIDDLE EAST", "ENERGY", "50 TARGETS", "REPORTED",
     "Houthis hit Saudi refinery; Riyadh strikes back",
     "Attack on the Jazan refinery kills a Nepali worker; Saudi Arabia says it hit 50 Houthi targets in Yemen.",
     "Al Jazeera", 42.55, 16.89),
    (8, "DR CONGO", "AFRICA", "EPIDEMIC", "12,000", "OFFICIAL",
     "Ebola cases pass 12,000 in DR Congo",
     "Second-largest outbreak on record; about 5,900 dead as fighting forces some responders to evacuate.",
     "AP · NPR", 29.5, 1.5),
    (9, "WASHINGTON", "N. AMERICA", "COURTS", "2ND JUDGE", "OFFICIAL",
     "Judge blocks Trump's birthright limits",
     "A federal judge strikes down the narrower birthright citizenship restrictions; a second judge also blocks them.",
     "Al Jazeera · UPI", -77.0, 38.9),
    (10, "KYIV", "EUROPE", "CONFLICT", "7 REGIONS", "REPORTED",
     "Overnight strikes kill two, cut power in seven regions",
     "Russia's overnight attack kills two in Kharkiv and leaves seven regions without power, Ukrenergo says.",
     "Ukrenergo · BBC", 30.5, 50.45),
    (11, "SEOUL", "EAST ASIA", "RATES", "3.25%", "OFFICIAL",
     "Bank of Korea lifts rate to 3.25%",
     "Third hike since July; highest in two years as a chip export boom keeps inflation elevated.",
     "Reuters · AP", 127.0, 37.5),
    (12, "SANTA CLARA", "N. AMERICA", "CHIPS", "4 COUNTRIES", "REPORTED",
     "Nvidia halts AI server shipments",
     "Dell and Supermicro told to stop shipping to Malaysia, Singapore, Thailand and Indonesia under new US curbs.",
     "FT · Reuters", -121.95, 37.35),
    (13, "LONDON", "EUROPE", "MIGRATION", "77,000", "OFFICIAL",
     "UK net migration falls to 77,000",
     "Lowest since 1997 outside the pandemic; 738,000 arrived and 661,000 left in the year to June.",
     "ONS · Reuters", -0.12, 51.5),
]

# (n, place, region, title, source, status)
ALSO = [
    (14, "FRANKFURT", "EUROPE", "Hernandez de Cos picked as next ECB chief", "France 24", "OFFICIAL"),
    (15, "BLUE NILE", "AFRICA", "Drone strikes kill at least 15 in Sudan's Blue Nile state", "AllAfrica", "REPORTED"),
    (16, "BAIDOA", "AFRICA", "Famine risk falls in Baidoa, but hunger persists, experts say", "UN News", "REPORTED"),
    (17, "MOGADISHU", "AFRICA", "Uganda and Somalia step up anti-al-Shabaab ops as foreign troops withdraw", "BBC", "REPORTED"),
    (18, "BISSAU", "AFRICA", "Guinea-Bissau junta postpones elections to November 2028", "AP", "OFFICIAL"),
    (19, "HASAKEH", "MIDDLE EAST", "ISIL suicide bomber kills two at a checkpoint in NE Syria", "AA", "REPORTED"),
    (20, "PARIS", "EUROPE", "Depardieu ordered to stand trial for alleged 2018 rape", "Reuters", "OFFICIAL"),
    (21, "OSLO", "EUROPE", "Norse Atlantic suspends all flights, warns of bankruptcy", "Reuters", "OFFICIAL"),
    (22, "LONDON", "EUROPE", "UK cold snap leaves power supply 2.7 GW short", "Guardian", "REPORTED"),
    (23, "BANGKOK", "SE ASIA", "Blast at Bangchak refinery injures nine, three critically", "BBC", "REPORTED"),
    (24, "NAYPYIDAW", "SE ASIA", "Myanmar will not fully comply with ICJ genocide orders", "Reuters", "REPORTED"),
    (25, "BOGOR", "SE ASIA", "13 confirmed dead in flooded illegal gold mine; 13 missing", "Reuters · BBC", "REPORTED"),
    (26, "TAIPEI", "EAST ASIA", "Taiwan jails ex-navy sergeant six years for spying for China", "Yonhap", "REPORTED"),
    (27, "HONG KONG", "EAST ASIA", "City marks one year since Wang Fuk Court fire killed 168", "AP", "REPORTED"),
    (28, "KATHMANDU", "SOUTH ASIA", "Nepal begins process to declare ~4,000 flood-missing dead", "AFP", "OFFICIAL"),
    (29, "DHAKA", "SOUTH ASIA", "Dhaka rules out Hasina's December return; only extradition", "TBS", "REPORTED"),
    (30, "SWAT VALLEY", "SOUTH ASIA", "Motorbike passenger takes one-handed catch in Pakistan", "BBC", "REPORTED"),
    (31, "BRASILIA", "LATIN AMERICA", "Bovespa jumps 6.07% as markets cheer Trabuco finance pick", "Reuters", "REPORTED"),
    (32, "CARACAS", "LATIN AMERICA", "Venezuela to repeal law barring opponents from politics", "La Nacion", "REPORTED"),
    (33, "BOGOTA", "LATIN AMERICA", "Colombia marks ten years since the FARC peace deal", "Le Monde", "REPORTED"),
    (34, "FLINDERS ISLAND", "OCEANIA", "Bushfire burns 10% of island; six homes damaged or lost", "AAP · AFP", "REPORTED"),
    (35, "SYDNEY", "OCEANIA", "Litchfield hits 121* in record WBBL match", "Sky", "OFFICIAL"),
    (36, "MELBOURNE", "OCEANIA", "Sarah Glenn bowls WBBL's first free-ball wicket", "BBC · ABC", "REPORTED"),
]

REGIONS = [
    ("EUROPE", 7, RED), ("MIDDLE EAST", 5, (150, 90, 30)),
    ("AFRICA", 5, (120, 70, 20)), ("EAST ASIA", 3, GOLD),
    ("SE ASIA", 3, TEAL), ("SOUTH ASIA", 4, (110, 60, 120)),
    ("N. AMERICA", 3, BLUE), ("LATIN AMERICA", 3, GREEN),
    ("OCEANIA", 3, (40, 130, 150)),
]

NUMBERS = [
    ("800,000+", "without power in US storms"),
    ("166", "killed in 26/11, 18 years on"),
    ("1.5-1.5", "Gukesh-Sindarov after Game 3"),
    ("7", "Ukraine regions without power"),
    ("12,000", "Ebola cases in DR Congo"),
    ("77,000", "UK net migration, lowest since 1997"),
]

TIMELINE = [
    ("00:00", "Thanksgiving Day begins in the US"),
    ("06:00", "Delhi marks Constitution Day"),
    ("14:00", "Gukesh-Sindarov Game 3 begins in Geneva"),
    ("23:00", "Thursday's 36 stories filed"),
]

# Landmass rectangles (lon_min, lon_max, lat_min, lat_max) for the dotted map.
LAND = [
    (-168, -130, 60, 71), (-130, -60, 49, 70), (-125, -67, 25, 49),
    (-117, -83, 8, 32), (-58, -20, 60, 83), (-80, -35, -5, 12),
    (-73, -40, -55, -5), (-10, 30, 54, 70), (-10, 40, 36, 54),
    (-5, 2, 50, 58), (-17, 32, 15, 35), (8, 35, -35, 15),
    (40, 51, -2, 12), (35, 60, 12, 42), (30, 180, 50, 75),
    (45, 135, 35, 55), (68, 88, 8, 35), (95, 105, 5, 28),
    (95, 140, -10, 5), (105, 122, 20, 40), (130, 145, 31, 45),
    (113, 153, -38, -12), (166, 178, -47, -34),
]

STATUS_FILL = {"OFFICIAL": GREEN, "REPORTED": BLUE, "CLAIM": GOLD,
               "CONFIRMED": PURPLE, "ONGOING": TEAL}


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def badge(draw, x, y, text, fill, fnt):
    w = draw.textlength(text, font=fnt) + 10
    draw.rounded_rectangle([x, y, x + w, y + 13], radius=6, fill=fill)
    draw.text((x + 5, y + 1), text, font=fnt, fill=(255, 255, 255))
    return w


def glyph(draw, kind, x0, y0, x1, y1, color):
    """Tiny flat pictogram per field, drawn from primitives only."""
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    w, h = x1 - x0, y1 - y0
    if kind == "CONFLICT":  # burst
        for a in range(0, 360, 45):
            import math
            r = math.radians(a)
            draw.line([cx, cy, cx + 0.42 * w * math.cos(r), cy + 0.42 * h * math.sin(r)],
                      fill=color, width=3)
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=color)
    elif kind == "SUMMIT":  # columns
        draw.polygon([(x0 + 4, y0 + 8), (cx, y0 + 2), (x1 - 4, y0 + 8)], fill=color)
        for i in range(3):
            bx = x0 + 8 + i * (w - 16) / 2
            draw.rectangle([bx, y0 + 11, bx + 5, y1 - 5], fill=color)
        draw.rectangle([x0 + 4, y1 - 4, x1 - 4, y1 - 1], fill=color)
    elif kind == "CENTRAL BANK":
        draw.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], outline=color, width=3)
        draw.text((cx - 5, cy - 9), "$", font=SANS_B(16), fill=color)
    elif kind == "ENERGY":  # flame
        draw.polygon([(cx, y0 + 2), (cx + 10, cy + 4), (cx + 6, y1 - 3),
                      (cx - 6, y1 - 3), (cx - 10, cy + 4)], fill=color)
    elif kind == "EPIDEMIC":  # cross in circle
        draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], outline=color, width=3)
        draw.rectangle([cx - 3, cy - 9, cx + 3, cy + 9], fill=color)
        draw.rectangle([cx - 9, cy - 3, cx + 9, cy + 3], fill=color)
    elif kind == "COURTS":  # scales
        draw.line([cx, y0 + 3, cx, y1 - 3], fill=color, width=3)
        draw.line([x0 + 5, y0 + 7, x1 - 5, y0 + 7], fill=color, width=3)
        draw.polygon([(x0 + 5, y0 + 7), (x0 + 11, y0 + 7), (x0 + 8, y0 + 15)], fill=color)
        draw.polygon([(x1 - 5, y0 + 7), (x1 - 11, y0 + 7), (x1 - 8, y0 + 15)], fill=color)
    elif kind == "DIPLOMACY":  # two bubbles
        draw.rounded_rectangle([x0 + 3, y0 + 4, cx + 4, cy + 2], radius=5, outline=color, width=2)
        draw.rounded_rectangle([cx - 4, cy - 2, x1 - 3, y1 - 5], radius=5, outline=color, width=2)
    elif kind == "STORMS":  # cloud + rain
        draw.ellipse([x0 + 4, y0 + 4, x0 + 18, y0 + 16], fill=color)
        draw.ellipse([x0 + 12, y0 + 2, x0 + 28, y0 + 16], fill=color)
        for i in range(3):
            bx = x0 + 8 + i * 9
            draw.line([bx, y0 + 19, bx - 3, y0 + 26], fill=color, width=2)
    elif kind == "RATES":  # rising arrow
        draw.line([x0 + 4, y1 - 6, cx, y0 + 6, x1 - 4, y0 + 12], fill=color, width=3)
        draw.polygon([(x1 - 4, y0 + 4), (x1 - 4, y0 + 14), (x1 - 12, y0 + 8)], fill=color)
    elif kind == "DEFENCE":  # shield
        draw.polygon([(cx, y0 + 2), (x1 - 3, y0 + 7), (x1 - 3, cy + 2),
                      (cx, y1 - 2), (x0 + 3, cy + 2), (x0 + 3, y0 + 7)], outline=color, width=3)
    elif kind == "CHIPS":  # chip
        draw.rectangle([cx - 9, cy - 9, cx + 9, cy + 9], outline=color, width=3)
        for i in range(3):
            draw.line([cx - 9, cy - 6 + i * 6, cx - 14, cy - 6 + i * 6], fill=color, width=2)
            draw.line([cx + 9, cy - 6 + i * 6, cx + 14, cy - 6 + i * 6], fill=color, width=2)
    elif kind == "MIGRATION":  # walking arrow
        draw.ellipse([cx - 3, y0 + 3, cx + 3, y0 + 9], fill=color)
        draw.line([cx, y0 + 10, cx, cy + 4], fill=color, width=3)
        draw.line([cx, cy + 4, cx - 6, y1 - 3], fill=color, width=3)
        draw.line([cx, cy + 4, cx + 6, y1 - 3], fill=color, width=3)
        draw.line([x0 + 4, cy + 8, x1 - 4, cy + 8], fill=color, width=2)
    elif kind == "PARADE":  # balloon
        draw.ellipse([cx - 11, y0 + 2, cx + 11, y0 + 20], fill=color)
        draw.polygon([(cx - 4, y0 + 19), (cx + 4, y0 + 19), (cx, y0 + 25)], fill=color)
        draw.line([cx, y0 + 25, cx + 3, y1 - 3], fill=color, width=2)
        draw.rectangle([cx - 5, y1 - 4, cx + 5, y1 - 1], fill=color)
    elif kind == "MEMORIAL":  # arch (India Gate)
        draw.rectangle([x0 + 4, y0 + 12, x1 - 4, y1 - 2], outline=color, width=3)
        draw.pieslice([x0 + 4, y0 + 2, x1 - 4, y0 + 22], 180, 360, outline=color, width=3)
        draw.rectangle([cx - 5, y0 + 16, cx + 5, y1 - 2], outline=color, width=2)
    elif kind == "CHESS":  # pawn
        draw.ellipse([cx - 6, y0 + 2, cx + 6, y0 + 14], fill=color)
        draw.polygon([(cx - 3, y0 + 14), (cx + 3, y0 + 14), (cx + 7, y1 - 5), (cx - 7, y1 - 5)], fill=color)
        draw.rectangle([x0 + 4, y1 - 4, x1 - 4, y1 - 1], fill=color)
    else:  # SPORT: ball
        draw.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], outline=color, width=3)
        draw.line([cx - 11, cy, cx + 11, cy], fill=color, width=2)
        draw.line([cx, cy - 11, cx, cy + 11], fill=color, width=2)


def draw_main_card(draw, s, x, y, w, h, big):
    n, place, region, field, bignum, status, title, body, src, lon, lat = s
    draw.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=CARD,
                           outline=LGREY, width=1)
    # scene strip with pictogram + big number badge (bigger on top-3 cards)
    sh = 46 if big else 30
    draw.rounded_rectangle([x + 1, y + 1, x + w - 1, y + sh], radius=6, fill=CHIP)
    draw.rectangle([x + 1, y + sh - 8, x + w - 1, y + sh], fill=CHIP)
    if big:
        glyph(draw, field, x + 8, y + 4, x + 52, y + sh - 4, RED)
        draw.text((x + 58, y + 8), bignum, font=SANS_B(19), fill=RED)
        draw.text((x + 58, y + 28), place + "  ·  " + field,
                  font=SANS_B(9), fill=GREY)
    else:
        glyph(draw, field, x + 8, y + 5, x + 38, y + sh - 5, RED)
        draw.text((x + 44, y + 7), bignum, font=SANS_B(13), fill=RED)
        draw.text((x + 44, y + 20), place + "  ·  " + field,
                  font=SANS_B(9), fill=GREY)
    badge(draw, x + w - 52, y + 6, status, STATUS_FILL[status], SANS_B(8))
    # number circle, bottom-right corner (clear of title/body text)
    draw.ellipse([x + w - 24, y + h - 22, x + w - 6, y + h - 4], fill=INK)
    ntxt = str(n)
    draw.text((x + w - 15 - draw.textlength(ntxt, font=SANS_B(11)) / 2, y + h - 20),
              ntxt, font=SANS_B(11), fill=(255, 255, 255))
    ty = y + sh + 8
    ts = 15 if big else 12
    for line in wrap(draw, title, SANS_B(ts), w - 16)[:2]:
        draw.text((x + 8, ty), line, font=SANS_B(ts), fill=INK)
        ty += ts + 3
    ty += 2
    bs = 11 if big else 10
    for line in wrap(draw, body, SANS(bs), w - 16)[:2]:
        draw.text((x + 8, ty), line, font=SANS(bs), fill=(60, 58, 52))
        ty += bs + 3
    draw.text((x + 8, y + h - 15), "Source: " + src, font=SANS(8), fill=GREY)


def draw_also(draw, x, y, col_w):
    draw.text((x, y), "ALSO ON THURSDAY — 23 MORE DATED BRIEFS",
              font=SANS_B(12), fill=INK)
    draw.line([x, y + 18, x + col_w * 2 + 10, y + 18], fill=INK, width=2)
    per_col = 12
    for ci in range(2):
        cx = x + ci * (col_w + 10)
        n_rows = per_col if ci == 0 else len(ALSO) - per_col
        for ri in range(n_rows):
            s = ALSO[ci * per_col + ri]
            n, place, region, title, src, status = s
            ry = y + 26 + ri * 17
            draw.text((cx, ry), str(n), font=SANS_B(10), fill=RED)
            tw = col_w - 34
            t = place + ": " + title
            if draw.textlength(t, font=SANS(9)) > tw:
                while draw.textlength(t + "…", font=SANS(9)) > tw and len(t) > 4:
                    t = t[:-1]
                t += "…"
            draw.text((cx + 22, ry), t, font=SANS(9), fill=INK)
            sw = draw.textlength(src, font=SANS(8))
            draw.text((cx + col_w - sw, ry + 9), src, font=SANS(8), fill=GREY)


def draw_map(draw, x, y, w, h):
    draw.text((x, y), "WHERE IT HAPPENED — SCENES 1–13",
              font=SANS_B(11), fill=INK)
    my = y + 18
    mh = h - 18
    # dotted landmass
    step_x, step_y = 7, 7
    for gx in range(int(w / step_x) + 1):
        for gy in range(int(mh / step_y) + 1):
            lon = -180 + (gx * step_x / w) * 360
            lat = 75 - (gy * step_y / mh) * 135
            if any(lo0 <= lon <= lo1 and la0 <= lat <= la1 for lo0, lo1, la0, la1 in LAND):
                draw.ellipse([x + gx * step_x - 1, my + gy * step_y - 1,
                              x + gx * step_x + 1, my + gy * step_y + 1], fill=DOT)
    # numbered pins
    for s in MAIN:
        n, place, region, field, bignum, status, title, body, src, lon, lat = s
        px = x + (lon + 180) / 360 * w
        py = my + (75 - lat) / 135 * mh
        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=(255, 255, 255), width=1)
        draw.text((px - 3 if n < 10 else px - 6, py - 6), str(n),
                  font=SANS_B(9), fill=(255, 255, 255))


def draw_datecheck(draw, x, y, w, h):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=6, outline=RED, width=2)
    draw.text((x + 10, y + 6), "DATE CHECK — EVERY STORY ABOVE HAPPENED OR WAS",
              font=SANS_B(11), fill=RED)
    draw.text((x + 10, y + 21), "FIRST REPORTED ON THURSDAY 26 NOVEMBER 2026 (UTC).",
              font=SANS_B(11), fill=RED)
    draw.text((x + 10, y + 38),
              "Five stories dated 25 Nov — NOT 26 Nov:",
              font=SANS_B(10), fill=INK)
    excl = ("US tariffs on 14 partners (25 Nov) · Bangladesh wage Tk17,000 (25 Nov) · "
            "Solomons-Australia treaty (25 Nov) · Ukraine laser downs Geran (25 Nov) · "
            "Hormuz tankers hit mines (25 Nov). Also earlier: Miss Universe · Huawei verdict · "
            "Chen Jining probe · Senegal AFCON title (24 Nov) · ABC-FCC ruling (25 Nov)")
    ty = y + 53
    for line in wrap(draw, excl, SANS(9), w - 20):
        draw.text((x + 10, ty), line, font=SANS(9), fill=(60, 58, 52))
        ty += 11
    ty += 3
    draw.text((x + 10, ty), "Not yet: EU budget deal (Fri 27 Nov) · Macy's parade (Sat 28 Nov)",
              font=SANS_B(9), fill=INK)
    ty += 13
    draw.text((x + 10, ty), "HOW SURE: CONFIRMED = 2+ outlets · OFFICIAL = on the record ·",
              font=SANS_B(9), fill=INK)
    draw.text((x + 10, ty + 11), "REPORTED = single wire · CLAIM = one side's account, unverified",
              font=SANS_B(9), fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # top bar
    d.text((M, 8), "THE WORLD IN ONE DAY", font=SANS_B(13), fill=INK)
    top = "36 STORIES  ·  9 REGIONS  ·  ALL FROM THU 26 NOV 2026"
    d.text((W - M - d.textlength(top, font=SANS_B(11)), 10), top, font=SANS_B(11), fill=RED)
    d.line([M, 28, W - M, 28], fill=INK, width=2)
    # masthead
    d.text((M, 34), "Thursday 26 November 2026", font=SERIF_B(44), fill=INK)
    deck = ("Macy's 100th parade moved to Saturday  ·  India marks 18 years since 26/11  ·  "
            "Gukesh and Sindarov draw Game 3")
    d.text((M, 86), deck, font=SERIF(13), fill=(70, 68, 62))
    # region chips
    cx, cy = M, 108
    for name, count, color in REGIONS:
        label = f"{name} {count}"
        wch = d.textlength(label, font=SANS_B(10)) + 16
        d.rounded_rectangle([cx, cy, cx + wch, cy + 20], radius=10, fill=color)
        d.text((cx + 8, cy + 4), label, font=SANS_B(10), fill=(255, 255, 255))
        cx += wch + 6
    # numbers bar
    ny, nh = 136, 40
    d.rounded_rectangle([M, ny, W - M, ny + nh], radius=6, fill=INK)
    cw6 = CW / 6
    for i, (num, label) in enumerate(NUMBERS):
        x0 = M + i * cw6
        d.text((x0 + 10, ny + 4), num, font=SANS_B(15), fill=(255, 214, 90))
        lab = label if d.textlength(label, font=SANS(8)) <= cw6 - 12 else label[:26] + "…"
        d.text((x0 + 10, ny + 23), lab, font=SANS(8), fill=(220, 218, 210))
        if i:
            d.line([x0, ny + 6, x0, ny + nh - 6], fill=(90, 88, 82), width=1)
    # UTC timeline
    ty = 186
    d.text((M, ty), "THURSDAY IN UTC", font=SANS_B(11), fill=INK)
    d.line([M, ty + 20, W - M, ty + 20], fill=LGREY, width=2)
    seg = CW / 4
    for i, (t, label) in enumerate(TIMELINE):
        x0 = M + i * seg
        d.ellipse([x0 - 3, ty + 16, x0 + 5, ty + 24], fill=RED)
        d.text((x0 + 2, ty + 2), t, font=SANS_B(10), fill=RED)
        for ln, line in enumerate(wrap(d, label, SANS(8), seg - 8)):
            d.text((x0 + 2, ty + 26 + ln * 10), line, font=SANS(8), fill=(60, 58, 52))
    # main cards: row 1 = 3 big, rows 2-3 = 5 each
    y0 = 238
    gap = 10
    bw3 = (CW - 2 * gap) / 3
    for i in range(3):
        draw_main_card(d, MAIN[i], M + i * (bw3 + gap), y0, bw3, 130, big=True)
    bw5 = (CW - 4 * gap) / 5
    for r in range(2):
        yy = y0 + 138 + r * 130
        for i in range(5):
            draw_main_card(d, MAIN[3 + r * 5 + i], M + i * (bw5 + gap), yy, bw5, 122, big=False)
    # ALSO list (2 columns)
    draw_also(d, M, 636, (CW - 10) / 2)
    # bottom band: map + date check
    by = 874
    draw_map(d, M, by, 452, 128)
    draw_datecheck(d, M + 468, by, CW - 468, 128)
    # footer
    d.line([M, 1008, W - M, 1008], fill=LGREY, width=1)
    d.text((M, 1012), "Sources: AP · Reuters · BBC · Al Jazeera · AFP · Guardian · France 24 · NPR · UPI · ONS · UN News · The Hindu",
           font=SANS(8), fill=GREY)
    img.save(OUT, optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()

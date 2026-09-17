# -*- coding: utf-8 -*-
"""Generate simple book-cover teasers for the two edited books."""
from PIL import Image, ImageDraw, ImageFont
import os

DST = r"C:\Users\yan\OneDrive\yemanzhongting.github.io\images\pub-teasers"
os.makedirs(DST, exist_ok=True)

W, H = 340, 460


def find_font(candidates):
    for c in candidates:
        if os.path.exists(c):
            return c
    return None


ZH_FONT = find_font([
    r"C:\Windows\Fonts\msyhbd.ttc", r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
])
EN_FONT = find_font([
    r"C:\Windows\Fonts\georgia.ttf", r"C:\Windows\Fonts\times.ttf",
    r"C:\Windows\Fonts\arial.ttf",
])


def make_cover(path, bg1, bg2, lines, font_path, accent):
    im = Image.new("RGB", (W, H), bg1)
    d = ImageDraw.Draw(im)
    # vertical gradient
    for y in range(H):
        t = y / H
        c = tuple(int(bg1[i] * (1 - t) + bg2[i] * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    # accent bar
    d.rectangle([0, 0, 10, H], fill=accent)
    # text
    size = 30 if font_path and ("msyh" in font_path) else 26
    font = ImageFont.truetype(font_path, size) if font_path else ImageFont.load_default()
    y = 70
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        # shrink font if too wide
        f2 = font
        while w > W - 60 and size > 14:
            size -= 2
            f2 = ImageFont.truetype(font_path, size)
            bbox = d.textbbox((0, 0), line, font=f2)
            w = bbox[2] - bbox[0]
        d.text(((W - w) // 2, y), line, font=f2, fill=(255, 255, 255))
        y += size + 14
    # bottom label
    lf = ImageFont.truetype(font_path, 18) if font_path else ImageFont.load_default()
    d.text((24, H - 60), "Edited Book", font=lf, fill=(255, 255, 255))
    im.save(path, "JPEG", quality=88)
    print("saved", path)


make_cover(
    os.path.join(DST, "2026-book-1.jpg"),
    (23, 78, 134), (10, 40, 80),
    ["AI赋能", "智慧城市", "", "（上、下册）", "", "智慧城市系列丛书"],
    ZH_FONT, (255, 200, 60),
)

make_cover(
    os.path.join(DST, "2026-book-2.jpg"),
    (14, 110, 99), (6, 55, 50),
    ["Applications in", "Urban Sensing", "for Smart Cities"],
    EN_FONT or ZH_FONT, (255, 255, 255),
)

#!/usr/bin/env python3
"""Make the site's photos from the research originals.

Each photo gets the same light correction (auto levels, a touch of warmth),
an optional crop, and WebP files at several widths plus one JPEG fallback.
Run: python3 images.py   (needs Pillow)
"""
import pathlib
from PIL import Image, ImageEnhance, ImageOps

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "data/research/facebook/images"
OUT = ROOT / "site/img"
WIDTHS = (480, 800, 1200, 1600)

# name: (source file, crop box as fractions (left, top, right, bottom) or None)
PHOTOS = {
    "55-main-street": ("2025-10-05_fb-page_1.jpg", (0.0, 0.08, 1.0, 0.92)),
    # Home hero: the porch, the 55 oval and the building sign listing the studio.
    "entrance": ("2025-10-05_fb-page_1.jpg", (0.0, 0.245, 1.0, 0.775)),
    "82-main-door": ("2024-11-23_fb-page_6.jpg", None),
    "waiting-room": ("2024-11-23_fb-page_2.jpg", None),
    "letterboard": ("2024-11-23_fb-page_4.jpg", None),
    "open-house-cookies": ("2024-11-23_fb-page_3.jpg", None),
    "woodlands": ("2024-07-26_fb-page_3.jpg", None),
    "whitening-result": ("2025-09-14_fb-page_1.jpg", None),
    "whitening-collage": ("2026-01-12_fb-page_1.jpg", None),
}


def correct(im):
    im = ImageOps.autocontrast(im, cutoff=0.4)
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * 1.02)))
    b = b.point(lambda v: int(v * 0.985))
    im = Image.merge("RGB", (r, g, b))
    return ImageEnhance.Color(im).enhance(0.95)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (src, crop) in PHOTOS.items():
        im = ImageOps.exif_transpose(Image.open(SRC / src)).convert("RGB")
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
        im = correct(im)
        made = []
        for width in WIDTHS:
            if width > im.width and made:
                break
            width = min(width, im.width)
            v = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
            v.save(OUT / f"{name}-{width}.webp", quality=76, method=6)
            made.append(width)
        fallback = im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS) if im.width > 800 else im
        fallback.save(OUT / f"{name}.jpg", quality=78, optimize=True, progressive=True)
        print(f"{name}: {im.width}x{im.height}, webp {made}")


if __name__ == "__main__":
    main()

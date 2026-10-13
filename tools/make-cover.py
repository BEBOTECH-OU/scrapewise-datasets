#!/usr/bin/env python3
"""Build the dataset cover image for Kaggle and Hugging Face.

One idea, one diagram, real Trap: the sample funnel from products read to figures
published. Kaggle asks for 564x284; Hugging Face crops to roughly the same shape,
so both targets use the same file.

    python3 tools/make-cover.py ~/Downloads/scrapewise-cover.png
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

W, H = 564, 284
BG = "#141510"  # neutral-900
LIME = "#bdff51"  # primary-500
CREAM = "#f5f5ec"  # secondary-500
MUTED = "#727269"  # neutral-500

WOFF = Path.home() / "Documents/scraper-ui-2/assets/fonts/Trap-SemiBold.woff"
TTF = Path(__file__).resolve().parent / ".trap-semibold.ttf"

# Products read, seller profiles read, aggregate figures published. The bar widths
# are the log of each count, not the count: 197,022 next to 180 would render the
# last bar as a single pixel.
STAGES = [
    ("197,022", "products read"),
    ("55,660", "seller profiles read"),
    ("180", "figures published"),
]


def trap(size):
    if not TTF.exists():
        font = TTFont(WOFF)
        font.flavor = None  # drop the woff compression so this saves as a plain ttf
        font.save(TTF)
    return ImageFont.truetype(str(TTF), size)


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "cover.png").expanduser()

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # A lime rule down the left edge, the one brand mark on the image.
    d.rectangle([0, 0, 5, H], fill=LIME)

    # Trap has no middle dot, so the separator is a slash.
    d.text((34, 30), "SCRAPEWISE / OPEN DATA / CC BY 4.0", font=trap(11), fill=MUTED)
    d.text((34, 52), "Amazon UK", font=trap(38), fill=CREAM)
    d.text((34, 95), "marketplace snapshot", font=trap(26), fill=LIME)
    d.text((34, 130), "23-24 September 2026", font=trap(13), fill=MUTED)

    # The funnel. Widths come from the counts on a log scale so all three stages stay
    # visible; this is a shape, not a measurement, so no axis is drawn.
    import math

    top, row_h, bar_h = 168, 38, 15
    longest = math.log10(197022)
    full = W - 34 - 150
    label_font, num_font = trap(11), trap(15)

    for i, (count, label) in enumerate(STAGES):
        y = top + i * row_h
        width = int(full * math.log10(int(count.replace(",", ""))) / longest)
        d.rectangle([34, y, 34 + width, y + bar_h], fill=LIME if i == 2 else "#3f4a28")
        d.text((34 + width + 10, y + 1), count, font=num_font, fill=CREAM)
        d.text((34 + width + 10, y + 19), label, font=label_font, fill=MUTED)

    img.save(out)
    print(f"wrote {out} ({W}x{H})")


if __name__ == "__main__":
    main()

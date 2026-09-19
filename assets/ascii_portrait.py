#!/usr/bin/env python3
"""Turn a photo into the character-ramp portrait used in the README.

    pip install Pillow
    python3 ascii_portrait.py photo.png > portrait.txt

Luminance is remapped with a black/white/gamma levels pass, the background is
dropped with a feathered elliptical mask, and what's left is quantised onto a
10-step character ramp. The defaults are tuned for one specific low-key night
portrait — for a different photo, start by adjusting --black / --white.
"""

import argparse

from PIL import Image, ImageDraw, ImageFilter

RAMP = " .:-=+*#%@"


def levels(img, black, white, gamma):
    span = max(1, white - black)
    lut = [int(255 * (max(0.0, min(1.0, (i - black) / span)) ** gamma)) for i in range(256)]
    return img.point(lut)


def portrait(path, box, ellipse, cols, black, white, gamma, ramp, sharpen, feather, cutoff, aspect):
    img = Image.open(path).convert("L")
    if box:
        img = img.crop(box)
    img = img.filter(ImageFilter.UnsharpMask(radius=3, percent=sharpen, threshold=2))
    img = levels(img, black, white, gamma)

    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).ellipse(ellipse or (0, 0, img.width, img.height), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(feather))

    # characters are roughly twice as tall as they are wide
    rows = max(1, int(cols * (img.height / img.width) * aspect))
    img = img.resize((cols, rows), Image.LANCZOS)
    mask = mask.resize((cols, rows), Image.LANCZOS)

    pixels, alpha = img.load(), mask.load()
    last = len(ramp) - 1
    lines = []
    for y in range(rows):
        line = ""
        for x in range(cols):
            a = alpha[x, y] / 255.0
            if a < cutoff:
                line += " "
                continue
            value = (pixels[x, y] / 255.0) * (a ** 0.4)   # fade into the mask edge
            line += ramp[max(0, min(last, int(value * last + 0.5)))]
        lines.append(line.rstrip())
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("image")
    p.add_argument("--cols", type=int, default=54, help="output width in characters")
    p.add_argument("--box", type=int, nargs=4, metavar=("L", "T", "R", "B"),
                   default=[292, 112, 468, 392], help="crop box in the source image")
    p.add_argument("--ellipse", type=int, nargs=4, metavar=("L", "T", "R", "B"),
                   default=[0, 0, 176, 280], help="mask ellipse, in cropped coordinates")
    p.add_argument("--black", type=int, default=34, help="black point (raise it to drop the background)")
    p.add_argument("--white", type=int, default=200, help="white point (lower it to blow out highlights)")
    p.add_argument("--gamma", type=float, default=0.95)
    p.add_argument("--ramp", default=RAMP, help="dark -> light character ramp")
    p.add_argument("--sharpen", type=int, default=150, help="unsharp mask percentage")
    p.add_argument("--feather", type=int, default=9, help="mask blur radius")
    p.add_argument("--cutoff", type=float, default=0.35, help="mask alpha below which a cell is blank")
    p.add_argument("--aspect", type=float, default=0.5, help="character height:width ratio")
    a = p.parse_args()

    print(portrait(a.image, tuple(a.box), tuple(a.ellipse), a.cols, a.black, a.white,
                   a.gamma, a.ramp, a.sharpen, a.feather, a.cutoff, a.aspect))


if __name__ == "__main__":
    main()

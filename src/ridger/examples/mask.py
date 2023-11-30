from math import sin

from ridger import generate_ridge_image

from PIL import Image, ImageDraw, ImageFont


IMSIZE = (1500, 400)


def line_color(x1, y1, x2, y2):
    return (128, 255, 128, 255)


if __name__ == "__main__":
    text = "HELLO, WORLD!"
    # add 2 for padding
    character_size = IMSIZE[0] // (len(text) + 1)
    immask = Image.new("RGB", IMSIZE, (0, 0, 0))
    imd = ImageDraw.Draw(immask)
    ftf = ImageFont.load_default()
    # this is just to show how to find the right font size by pixel
    for fs in range(1, 300, 1):
        bbox = ftf.font_variant(size=fs).getbbox("X")
        if bbox[2] - bbox[0] > character_size:
            break
    ftf = ftf.font_variant(size=fs)
    imd.text(
        (character_size, character_size),
        text,
        fill=(255, 255, 255),
        font=ftf,
    )

    def height_map(x, y, mask=immask) -> tuple[int, int]:
        if mask.getpixel((x, y)) == (0, 0, 0):
            return 0
        else:
            return 8

    generate_ridge_image(
        height_map,
        line_color,
        bgcolor=(0, 0, 0, 255),
        # data_to_screen=data_to_screen,
        imsize=IMSIZE,
        line_width=1,
        line_distance=5
    ).show()

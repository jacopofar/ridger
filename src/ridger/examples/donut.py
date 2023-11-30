from math import sqrt

from ridger import generate_ridge_image

IMSIZE = (1500, 1500)


def height_map(x, y):
    dist = sqrt((x - 500) ** 2 + (y - 500) ** 2)
    # donut hole
    if dist < 100:
        return 0
    # outside the donut
    if dist > 300:
        return 0
    return 50


def line_color(x1, y1, x2, y2):
    # create a shadow effect, as if light came from the left
    if y1 == y2:
        return (200, 200, 200, 255)
    elif y1 < y2:
        return (128, 128, 128, 255)
    else:
        return (255, 255, 255, 255)


def data_to_screen(x, y) -> tuple[int, int]:
    # how long is the far away side?
    horizon_min_side = 600
    horizon_max_side = 1000
    # how long is here?
    this_horizon = (
        horizon_min_side + (horizon_max_side - horizon_min_side) * y / IMSIZE[1]
    )
    # scale x to the current hporizon keeping the center
    x = IMSIZE[0] / 2 + (x - IMSIZE[0] / 2) * this_horizon / horizon_max_side
    return x, y


if __name__ == "__main__":
    generate_ridge_image(
        height_map,
        line_color,
        bgcolor=(0, 0, 0, 255),
        data_to_screen=data_to_screen,
        imsize=IMSIZE,
    ).show()

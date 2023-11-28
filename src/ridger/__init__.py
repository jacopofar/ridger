from typing import Callable

from PIL import Image, ImageDraw

IMSIZE = (1000, 1000)
BGCOLOR = (0, 0, 0, 255)
# distance between line in data space
LINE_DISTANCE = 11
# distance between data points on the same line in data space
DATA_POINT_DISTANCE = 5


def generate_ridge_image(
    height_map: Callable[[int, int], int],
    line_color: Callable[[int, int, int, int], tuple[int, int, int, int]],
    imsize=IMSIZE,
    bgcolor=BGCOLOR,
    data_to_screen=lambda x, y: (x, y),
):
    im = Image.new("RGBA", imsize, bgcolor)

    draw = ImageDraw.Draw(im)
    for line_depth in range(LINE_DISTANCE, imsize[1], LINE_DISTANCE):
        previous_point = None, None
        for x in range(0, imsize[0], DATA_POINT_DISTANCE):
            height = height_map(x, line_depth)
            # first data point is skipped
            if previous_point[0] is not None:
                # draw the trapezoid that occludes the previous lines
                draw.polygon(
                    [
                        # previous point, base
                        data_to_screen(x - DATA_POINT_DISTANCE, line_depth),
                        # previous point, with elevation
                        data_to_screen(*previous_point),
                        # current point, with elevation
                        data_to_screen(x, line_depth - height),
                        # current point, base
                        data_to_screen(x, line_depth),
                    ],
                    fill=bgcolor,
                )
                # draw the line over the trapezoid
                draw.line(
                    (
                        data_to_screen(*previous_point),
                        data_to_screen(x, line_depth - height),
                    ),
                    fill=line_color(*previous_point, x, line_depth - height),
                    width=2,
                )
            previous_point = x, line_depth - height
    return im

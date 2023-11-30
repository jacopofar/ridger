from typing import Callable

from PIL import Image, ImageDraw

IMSIZE = (1000, 1000)


def generate_ridge_image(
    height_map: Callable[[int, int], int],
    line_color: Callable[[int, int, int, int], tuple[int, int, int, int]],
    imsize=IMSIZE,
    bgcolor=(0, 0, 0, 255),
    data_to_screen=lambda x, y: (x, y),
    line_distance=11,
    data_point_distance=5,
    line_width=2,
):
    im = Image.new("RGBA", imsize, bgcolor)

    draw = ImageDraw.Draw(im)
    for line_depth in range(line_distance, imsize[1], line_distance):
        previous_point = None, None
        for x in range(0, imsize[0], data_point_distance):
            height = height_map(x, line_depth)
            # first data point is skipped
            if previous_point[0] is not None:
                # draw the trapezoid that occludes the previous lines
                draw.polygon(
                    [
                        # previous point, base
                        data_to_screen(x - data_point_distance, line_depth),
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
                    width=line_width,
                )
            previous_point = x, line_depth - height
    return im

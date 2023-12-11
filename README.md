# ridger

Ridgeline plot (aka Joyplot) library in Python

![A ridge plot showing the words Hello World in a pseudo 3D fashion](hello_world.png)

## Usage

Have a look at the examples folder.

In short, you need to provide a function that will return the height of the chart in a given point.

Additionally, you can provide a function to specify the color and a distortion of the space (e.g. to implement perspective, see the donut example).

The image is returned as a Pillow object, use `.show()` to see it immediately or `.save(filename)` to save it as a file.
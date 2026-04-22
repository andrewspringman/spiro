# spiro

This repository contains Python scripts for generating spirograph patterns using SVG drawings.

## Python Files

### spirograph.py
Generates an SVG spirograph pattern and saves it as `spirograph4.svg`. It uses the `svgwrite` library to create a vector graphic of a spirograph curve based on mathematical formulas involving radii r1, r2, and r3. The script defines a `spirograph` function that takes parameters for the radii, canvas size, and number of points/revolutions. Example usage: `spirograph(dwg, 250, 1, 100, width=1000, height=1000, points=250)`.

### spirograph1.py
Creates a spirograph SVG file named `spirograph.svg`. Similar to the base script, it calculates points for the curve using different multipliers in the trigonometric functions. Parameters: r1=250, r2=40, r3=53, with 5000 points over 50 revolutions. The center is at the canvas center.

### spirograph2.py
Generates `spirograph2.svg` with adjusted formulas (cos(theta*3) and sin(theta/4)). Uses r1=250, r2=40, r3=53, 10000 points, 50 revolutions.

### spirograph3.py
Produces `spirograph3.svg` with a more complex formula including a scaling factor c based on theta, and an offset in the x-coordinate. Center is shifted to width/3. Parameters: r1=250, r2=1, r3=53, 20000 points, 25 revolutions.

## Usage
Run any of the scripts with Python to generate the corresponding SVG file:
```
python spirograph.py
python spirograph1.py
# etc.
```
Requires `svgwrite` library: `pip install svgwrite`.

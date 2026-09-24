# Spirograph

Generate beautiful mathematical spirograph patterns as SVG files.

A **spirograph** is a mesmerizing geometric curve created when a circle rolls inside another circle. The shape depends on the sizes of the circles and where the drawing point is located relative to the rolling circle's center.

## Mathematical Background

A spirograph is generated using parametric equations:

```
x(θ) = (r1 - r2) * cos(θ) + r3 * cos(((r1 - r2) / r2) * θ)
y(θ) = (r1 - r2) * sin(θ) - r3 * sin(((r1 - r2) / r2) * θ)
```

Where:
- **r1** = radius of the fixed (outer) circle
- **r2** = radius of the rolling (inner) circle  
- **r3** = distance from the rolling circle's center to the drawing point
- **θ** = rotation angle

## Features

- **Named presets** — Quick access to beautiful pre-tuned patterns
- **Full parameter control** — Customize any aspect of the design
- **High-quality SVG output** — Scale to any size without quality loss
- **Simple CLI interface** — Generate patterns from the command line

## Installation

```bash
git clone https://github.com/andrewspringman/spiro.git
cd spiro
python3 -m venv .venv
source .venv/bin/activate
pip install svgwrite
python spirograph.py --help
```

## Usage

### Use a Preset

```bash
python spirograph.py --preset baroque
python spirograph.py --preset intricate
python spirograph.py --preset simple
python spirograph.py --preset delicate
```

### Override Preset Parameters

Presets set defaults for r1, r2, r3, points, and revolutions. Any of these can be overridden:

```bash
# Baroque with fewer points
python spirograph.py --preset baroque --points 10

# Delicate with a different outer radius
python spirograph.py --preset delicate --r1 400

# Intricate with custom color and size
python spirograph.py --preset intricate --color "#FF6B6B" --width 2000 --height 2000
```

### Fully Custom

```bash
python spirograph.py --r1 300 --r2 7 --r3 100 --points 500 --revolutions 40 -o custom.svg
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--preset` | — | Use a named preset from `presets.json` |
| `--save` | — | Save resolved parameters as a named preset to `presets.json` |
| `--open` | — | Open the output file after generating |
| `--r1` | 250 | Radius of fixed (outer) circle |
| `--r2` | 1 | Radius of rolling (inner) circle |
| `--r3` | 100 | Distance from rolling circle center to drawing point |
| `--points` | 250 | Number of curve points to calculate (more = smoother) |
| `--revolutions` | 50 | Number of complete revolutions (more = more complex) |
| `--width` | 1000 | SVG canvas width in pixels |
| `--height` | 1000 | SVG canvas height in pixels |
| `--color` | black | Stroke color (any CSS color) |
| `--stroke-width` | 1.0 | Line width in pixels |
| `-o, --output` | spirograph.svg | Output file path |
| `-d, --directory` | ./output | Output directory |

## Saving Presets

Save any parameter combination as a named preset for reuse:

```bash
# Save a custom preset
python spirograph.py --r1 300 --r2 7 --r3 100 --points 500 --revolutions 40 --save mypattern

# Use the saved preset later
python spirograph.py --preset mypattern

# Save a modified preset under a new name
python spirograph.py --preset baroque --points 10 --save baroque_lite
```

Presets are stored in `presets.json` alongside the script. Several presets are included out of the box: `baroque`, `intricate`, `simple`, and `delicate`. Run `--help` to see all available presets and their parameters.

## License

MIT License
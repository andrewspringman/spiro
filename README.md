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

### Option 1: Clone and run directly

```bash
git clone https://github.com/andrewspringman/spiro.git
cd spiro
pip install svgwrite
python spirograph.py --help
```

### Option 2: Make it executable

```bash
chmod +x spirograph.py
./spirograph.py --preset baroque -o my_pattern.svg
```

## Usage

### Quick Start: Use a Preset

Generate one of four built-in preset patterns:

```bash
# Baroque-inspired intricate pattern
python spirograph.py --preset baroque -o baroque.svg

# Intricate design with fine details
python spirograph.py --preset intricate -o intricate.svg

# Simple, elegant pattern
python spirograph.py --preset simple -o simple.svg

# Delicate, precise design
python spirograph.py --preset delicate -o delicate.svg
```

### Advanced: Custom Parameters

```bash
# Custom radii and parameters
python spirograph.py \
  --r1 300 \
  --r2 7 \
  --r3 100 \
  --points 500 \
  --revolutions 40 \
  -o custom.svg

# Change colors and line width
python spirograph.py \
  --preset intricate \
  --color "#FF6B6B" \
  --stroke-width 2.0 \
  -o colored.svg

# Generate multiple sizes
python spirograph.py \
  --preset baroque \
  --width 2000 \
  --height 2000 \
  -o large_baroque.svg
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--preset` | — | Use a named preset (baroque, intricate, simple, delicate) |
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

## Presets Explained

### Baroque
- Parameters: r1=250, r2=1, r3=100
- Characteristic: Highly intricate, many fine details

### Intricate
- Parameters: r1=300, r2=5, r3=80
- Characteristic: Complex with balanced detail

### Simple
- Parameters: r1=200, r2=50, r3=100
- Characteristic: Bold, clear, easy to recognize

### Delicate
- Parameters: r1=280, r2=3, r3=120
- Characteristic: Fine, precise, lace-like

## License

MIT License
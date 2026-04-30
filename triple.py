import math
import svgwrite


def triple_spirograph(r1, r2, r3, r4, width=800, height=800, padding=50, points=10000, revolutions=50):
    """Generate a nested three-circle spirograph and save it as triple.svg."""
    dtheta = revolutions * 2 * math.pi / points
    angle_list = [i * dtheta for i in range(points)]

    dwg = svgwrite.Drawing('triple.svg', profile='tiny')
    dwg.viewbox(0, 0, width, height)

    cx = width / 2
    cy = height / 2

    path_data = []
    first_point_set = False

    for theta in angle_list:
        # Circle 2 rotates around the fixed Circle 1.
        x2 = (r1 - r2) * math.cos(theta)
        y2 = (r1 - r2) * math.sin(theta)

        # Circle 3 rotates around Circle 2 while the pen rotates around Circle 3.
        circle3_angle = ((r1 - r2) / r3) * theta
        x3 = x2 + r3 * math.cos(circle3_angle)
        y3 = y2 - r3 * math.sin(circle3_angle)

        pen_angle = ((r1 - r2) / r4) * theta
        x = x3 + r4 * math.cos(pen_angle)
        y = y3 - r4 * math.sin(pen_angle)

        if not first_point_set:
            path_data.append(f"M {cx + x} {cy + y}")
            first_point_set = True
        else:
            path_data.append(f"L {cx + x} {cy + y}")

    dwg.add(dwg.path(d=" ".join(path_data), fill='none', stroke='black'))
    dwg.save()


if __name__ == '__main__':
    triple_spirograph(250, 20, 240, 20, width=1000, height=1000, points=15000, revolutions=50)

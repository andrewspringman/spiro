import math
import svgwrite

def spirograph(r1, r2, r3, width=500, height=500, padding=50, points=20000, revolutions=25):
    # Calculate the angles for each point on the Spirograph curve
    dtheta = revolutions * 2 * math.pi / points
    angle_list = [i * dtheta for i in range(points)]
    
    # Initialize an SVG drawing object with specified width and height
    dwg = svgwrite.Drawing('spirograph3.svg', profile='tiny')
    dwg.viewbox(0, 0, width, height)
    
    # Calculate the center of the image
    cx = width / 3
    cy = height / 2
    
    # Create a path element to hold the Spirograph curve
    path_data = []
    first_point_set = False
    
    for theta in angle_list:
        c = theta/200
        x = (r1*c - r2*c) * math.cos(theta) + r3*c * math.cos(((r1*c - r2*c) / r3*c) * theta) + theta/2
        y = (r1*c - r2*c) * math.sin(theta) - r3*c * math.sin(((r1*c - r2*c) / r3*c) * theta)
        
        if not first_point_set:
            path_data.append(f"M {cx + x} {cy + y}")
            first_point_set = True
        else:
            path_data.append(f"L {cx + x} {cy + y}")
    
    # Add the path to the drawing
    dwg.add(dwg.path(d=" ".join(path_data), fill='none', stroke='black'))
    
    # Save the SVG file
    dwg.save()

# Example usage:
spirograph(250, 1, 53)
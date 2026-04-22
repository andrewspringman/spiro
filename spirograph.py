import math
import svgwrite

def spirograph(dwg, r1, r2, r3, width=800, height=800, padding=50, points=90, revolutions=50):
    # Calculate the angles for each point on the Spirograph curve
    dtheta = revolutions * 2 * math.pi / points
    angle_list = [i * dtheta for i in range(points)]
    
    
    # Calculate the center of the image
    cx = width / 2
    cy = height / 2
    
    # Create a path element to hold the Spirograph curve
    path_data = []
    first_point_set = False
    
    for theta in angle_list:
        c = 1
        x = (r1*c - r2*c) * math.cos(theta*2) + r3*c * math.cos(((r1*c - r2*c) / r3*c) * theta)
        y = (r1*c - r2*c) * math.sin(theta*2) - r3*c * math.sin(((r1*c - r2*c) / r3*c) * theta)
        
        if not first_point_set:
            path_data.append(f"M {cx + x} {cy + y}")
            first_point_set = True
        else:
            path_data.append(f"L {cx + x} {cy + y}")
    
    # Add the path to the drawing
    dwg.add(dwg.path(d=" ".join(path_data), fill='none', stroke='black'))

# Initialize an SVG drawing object with specified width and height
dwg = svgwrite.Drawing('spirograph4.svg', profile='tiny')
width=1000
height=1000
dwg.viewbox(0, 0, width, height)

# for points in (150, 250):    
spirograph(dwg, 250, 1, 100, width=width, height=height, points=250)

# Save the SVG file
dwg.save()

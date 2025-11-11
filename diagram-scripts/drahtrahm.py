
# ! Tod von chatty generiert und auch falsch aber !
# ? Trotzdem interessante Idee



# Import the required libraries
# matplotlib.pyplot is used for plotting (drawing) graphs and diagrams
# numpy is used here to create evenly spaced values for our field points
import matplotlib.pyplot as plt
import numpy as np

# Create a new figure and a single set of axes (the drawing area)
fig, ax = plt.subplots()

# ---- DRAW THE DRAHTRAHMEN (WIRE LOOP) ----
# Define the x and y coordinates of the corners of the rectangular loop
# The last point is repeated (0,0) so the rectangle is closed
x = [0, 2, 2, 0, 0]
y = [0, 0, 1, 1, 0]

# Plot the rectangular loop as a black line ('k' = black)
# linewidth=2 makes the wire thicker
ax.plot(x, y, 'k', linewidth=2, label='Drahtrahmen')

# ---- DRAW THE MAGNETIC FIELD (HOMOGENES MAGNETFELD) ----
# We'll represent the magnetic field by small blue arrows (vectors)
# np.linspace creates evenly spaced points between start and end values
for i in np.linspace(0.2, 1.8, 5):       # 5 positions along x-axis
    for j in np.linspace(0.2, 0.8, 3):   # 3 positions along y-axis
        # Draw a small arrow at each (i, j) location
        # Here we set dx and dy = 0 (no arrow direction), but we could modify them for vector fields
        # color='b' makes them blue, angles='xy' keeps arrows in data coordinates,
        # scale_units='xy' and scale=1 make arrows have consistent sizes
        ax.quiver(i, j, 0, 0, color='b', angles='xy', scale_units='xy', scale=1)

# Add a label "B" to indicate the direction of the magnetic field
# (You can move this text depending on your layout)
ax.text(2.1, 0.5, r'$\vec{B}$', color='b', fontsize=14)

# ---- DRAW THE CURRENT DIRECTION (STROMRICHTUNG) ----
# Draw a red arrow along the bottom side of the loop to represent current (I)
# Parameters: (x_start, y_start, dx, dy)
# head_width controls the size of the arrowhead
ax.arrow(0, 0.5, 2, 0, head_width=0.05, color='r')

# Add a label "I" for the current
ax.text(1, 0.6, r'$I$', color='r', fontsize=14)

# ---- FORMAT THE DIAGRAM ----
# Keep equal scaling on both axes (so the rectangle doesn’t look stretched)
ax.set_aspect('equal')

# Define visible limits of the diagram
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 1.5)

# Turn off the axis lines, ticks, and labels — we only want the diagram
ax.axis('off')

# Display the final diagram
plt.show()
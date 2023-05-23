import numpy as np
from mayavi import mlab

# Coordonnées des sommets du cube
vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Face inférieure
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   # Face supérieure
])

# Faces du cube (indices des sommets)
faces = np.array([
    [0, 1, 2, 3],  # Face inférieure
    [4, 5, 6, 7],  # Face supérieure
    [0, 1, 5, 4],  # Face arrière
    [1, 2, 6, 5],  # Face droite
    [2, 3, 7, 6],  # Face avant
    [3, 0, 4, 7]   # Face
])

# Split each quadrilateral into two triangles
triangles = np.vstack((faces[:, [0, 1, 2]], faces[:, [0, 2, 3]]))

# Create a figure
fig = mlab.figure()

# Plot the cube
mlab.triangular_mesh(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles, color=(0.8, 0.8, 0.8), figure=fig)

# Add axes and orientation cube
mlab.axes(figure=fig)
mlab.orientation_axes(figure=fig)

# View the plot
mlab.show()


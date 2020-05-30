
"""
Rasterizing a mesh to a volumetric datastructure
"""

import numpy as np
import pyvista as pv


__author__ = "Shervin Azadi"
__copyright__ = "Shervin Azadi"
__credits__ = "Shervin Azadi"
__license__ = "MIT"
__version__ = "0.0.2"
__maintainer__ = "Shervin Azadi"
__email__ = "shervinazadi93@gmail.com"
__status__ = "Dev"


# loading the base mesh
geo_mesh = pv.read("DATA/bunny.obj")

# loading data
values = np.genfromtxt('DATA/bunny_volume.csv',
                       delimiter=',', skip_header=7, usecols=(3))
voxel_size = np.genfromtxt('DATA/bunny_volume.csv',
                           delimiter='-', skip_header=1, max_rows=1, usecols=(1, 2, 3))
volume_shape = np.genfromtxt('DATA/bunny_volume.csv',
                             delimiter='-', skip_header=2, max_rows=1, usecols=(1, 2, 3)).astype(int)
points = np.genfromtxt('DATA/bunny_voxels.csv',
                       delimiter=',', skip_header=6, usecols=(1, 2, 3))
hits = np.genfromtxt('DATA/bunny_hitpoints.csv',
                     delimiter=',', skip_header=6, usecols=(1, 2, 3))

# reconstruct the shape of the volume
values = values.reshape(volume_shape)

# Create the spatial reference
grid = pv.UniformGrid()

# Set the grid dimensions: shape + 1 because we want to inject our values on
#   the CELL data
grid.dimensions = np.array(values.shape) + 1

# retrieve the bounding box information
mesh_bb = np.array(geo_mesh.bounds).reshape(2, 3, order='F')
mesh_bb_min = mesh_bb[0]

# Edit the spatial reference
# The bottom left corner of the data set
mesh_bb_min_rasterized = np.rint(mesh_bb_min / voxel_size) * voxel_size
grid.origin = mesh_bb_min_rasterized - voxel_size * 0.5
grid.spacing = voxel_size  # These are the cell sizes along each axis

# Add the data values to the cell data
grid.cell_arrays["values"] = values.flatten(order="F")  # Flatten the array!

# filtering the voxels
threshed = grid.threshold([0.9, 1.1])

# bounding box of the voxelation
outline = grid.outline()


# Main Plotting:

# initiating the plotter
p = pv.Plotter()
p.set_background("black")

# adding the base mesh: light blue
p.add_mesh(geo_mesh, show_edges=True, color='#abd8ff',
           opacity=0.4, label="Base Mesh")

# adding the boundingbox wireframe
p.add_mesh(outline, color="grey", label="Rasterization Domain")

# adding the hit points: blue
p.add_mesh(pv.PolyData(hits), color='#2499ff',
           point_size=12, render_points_as_spheres=True, label="Intersection Points")


# adding the voxel centeroids: red
p.add_mesh(pv.PolyData(points), color='#ff244c',
           point_size=15, render_points_as_spheres=True, label="Voxel Centroids")

# adding the voxels: light red
p.add_mesh(threshed, show_edges=True, color="#ff8fa3",
           opacity=0.3, label="Voxels")

# adding the legend
p.add_legend(bcolor=[0.1, 0.1, 0.1], border=True, size=[0.1, 0.1])

# plotting
p.show()

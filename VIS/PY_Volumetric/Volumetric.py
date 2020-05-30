import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# volume bound
s = 3

# set the sphere on the corner of array
X, Y, Z = np.mgrid[-s:s:30j, -s:s:30j, -s:s:30j]
val = np.sin(X*Y*Z) / (X*Y*Z)

# Initialize figure with 4 3D subplots
fig = make_subplots(
    rows=1, cols=1)


fig.add_trace(
    go.Volume(
        x=X[1:-1, 1:-1, 1:-1].flatten(),
        y=Y[1:-1, 1:-1, 1:-1].flatten(),
        z=Z[1:-1, 1:-1, 1:-1].flatten(),
        value=val[1:-1, 1:-1, 1:-1].flatten(),
        isomin=0,
        isomax=1,
        # colorscale='Reds',
        opacity=0.1,  # needs to be small to see through all surfaces
        surface_count=17,  # needs to be a large number for good volume rendering
        colorbar=dict(len=1, x=1),
    )
)

# set to dark mode
fig.layout.template = 'plotly_dark'

# write plot to html
html_path = "VIS/PY_Volumetric/Volumetric.html"
fig.write_html(html_path)

# show the figure
# fig.show()

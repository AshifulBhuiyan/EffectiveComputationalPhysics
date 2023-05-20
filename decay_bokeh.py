#decay_bokeh.py
import numpy as np
# import the Bokeh plotting tools
from bokeh import plotting as bp

# as in the matplotlib example, load decays.csv into a NumPy array
decaydata = np.loadtxt('./data/decays.csv',delimiter=",",skiprows=1)

# provide handles for the x and y columns
time = decaydata[:,0]
decays = decaydata[:,1]

# define some output file metadata
bp.output_file("decays.html", title="Experiment 1 Radioactivity")

# create a figure with fun Internet-friendly features (optional)
bp.figure(tools="pan,wheel_zoom,box_zoom,reset,previewsave")

# on that figure, create a line plot
bp.line(time, decays, x_axis_label="Time (s)", y_axis_label="Decays (#)",
color='#1F78B4', legend='Decays per second')

# additional customization to the figure can be specified separately
bp.curplot().title = "Decays"
bp.grid().grid_line_alpha=0.3

# open a browser
bp.show()
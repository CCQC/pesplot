#!/usr/bin/python3
"""

Potential Energy Surface Plotter

Program employs the matplotlib module of Python to plot potential energy surfaces
and output publishable quality plots.

Authors:
        Kevin Moore
        Center for Computational Quantum Chemistry (CCQC)
        Dept. of Chemistry, Univ. of Georgia, Athens, GA, United States

"""

import plotfxn 
import input_proc

# Call the series of functions which read the command line input and

input_proc.input_processor()
input_proc.section_finder()

# Call functions to run matplotlib and create pdf of potential energy surface plot.

plotfxn.format_axes()
plotfxn.generate_xcoords()
plotfxn.plt_spec_lines()
plotfxn.plt_connecting_lines()
plotfxn.create_pdf()

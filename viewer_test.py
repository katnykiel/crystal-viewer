# Import required libraries
from __future__ import annotations

import dash
from dash import html
from pymatgen.core import Lattice, Structure

import crystal_toolkit.components as ctc
from crystal_toolkit.settings import SETTINGS

# Load a sample structure to test
app = dash.Dash(assets_folder=SETTINGS.ASSETS_PATH)

structure = Structure.from_file("mxene-nlc.vasp")

# create the Crystal Toolkit component
structure_component = ctc.StructureMoleculeComponent(structure, id="hello_structure")

# add the component's layout to our app's layout
layout = html.Div([structure_component.layout()])

# as explained in "preamble" section in documentation
ctc.register_crystal_toolkit(app=app, layout=layout)
if __name__ == "__main__":
    app.run(debug=True, port=8050)

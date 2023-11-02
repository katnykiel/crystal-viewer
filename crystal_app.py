# Import required libraries
from __future__ import annotations

import dash
from dash import html
from pymatgen.core import Structure
import crystal_toolkit.components as ctc

# Taken directly from the Crystal Toolkit documentation
# https://github.com/materialsproject/crystaltoolkit

def create_crystal_toolkit_component(structure: Structure) -> dash.Dash:
    """
    Creates a Crystal Toolkit component for the given crystal structure.

    Args:
        structure : pymatgen.core.structure.Structure
        The crystal structure to display.

    Returns:
        dash.Dash :
        The Dash app containing the Crystal Toolkit component.
    """

    # create the Crystal Toolkit component
    app = dash.Dash()
    structure_component = ctc.StructureMoleculeComponent(structure)

    # add the component's layout to our app's layout
    layout = html.Div([structure_component.layout()])

    # as explained in "preamble" section in documentation
    ctc.register_crystal_toolkit(app=app, layout=layout)

    return app

# Import required libraries
from __future__ import annotations

import dash
from dash import html
from pymatgen.core import Structure
from typing import List
import crystal_toolkit.components as ctc
from dash.dependencies import Input, Output

# Taken directly from the Crystal Toolkit documentation
# https://github.com/materialsproject/crystaltoolkit


def create_crystal_toolkit_component(structures: List[Structure]) -> dash.Dash:
    """
    Creates a Crystal Toolkit component for the given crystal structure.

    Args:
        structures : List[pymatgen.core.structure.Structure]
        The crystal structures to display.

    Returns:
        dash.Dash :
        The Dash app containing the Crystal Toolkit component.
    """

    # create the Crystal Toolkit component
    app = dash.Dash(prevent_initial_callbacks=True)

    # we show the first structure by default
    structure_component = ctc.StructureMoleculeComponent(
        structures[0], id="hello_structure"
    )

    # and we create a button for user interaction
    my_button = html.Button("Swap Structure", id="change_structure_button")

    # now we have two entries in our app layout,
    # the structure component's layout and the button
    layout = html.Div([structure_component.layout(), my_button])

    # as explained in "preamble" section in documentation
    ctc.register_crystal_toolkit(app=app, layout=layout)

    # for the interactivity, we use a standard Dash callback
    @app.callback(
        Output(structure_component.id(), "data"),
        Input("change_structure_button", "n_clicks"),
    )
    def update_structure(n_clicks):
        """Toggle between hexagonal and cubic structures on button click."""
        return structures[n_clicks % len(structures)]

    return app
    


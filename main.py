from structure_loader import load_structure
from crystal_app import create_crystal_toolkit_component

# Load in a structure from structure_loader.py
structure = load_structure("mxene.in")

# Create the Crystal Toolkit component
app = create_crystal_toolkit_component(structure)
app.run(debug=True, port=8050)
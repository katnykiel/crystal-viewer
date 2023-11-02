from structure_loader import load_structure, load_structures_from_folder
from crystal_app import create_crystal_toolkit_component

# Load in a structure from structure_loader.py
structure = load_structure("mxene.in")

# Make supercell
superstructure = structure.copy()
superstructure.make_supercell([3, 3, 2])

# Create the Crystal Toolkit component
app = create_crystal_toolkit_component([structure,superstructure])
app.run(debug=True, port=8050)
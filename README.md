 # Crystal Structure Viewer

This project is a simple application for visualizing crystal structures. It uses the `pymatgen` library to load crystal structures from files and the `crystal_toolkit` library to create an interactive 3D visualization of the structure.

## Installation

First, clone this git repository.

```
git clone https://github.com/username/crystal-viewer.git
```
Before running the application, you need to install the required Python libraries. You can do this with pip:

```
pip install pymatgen crystal_toolkit dash
```

## Usage

To use the application, you need to have a file that describes the crystal structure you want to visualize. The application currently supports files in the Crystallographic Information File (CIF) format, Quantum Espresso .in format, and the POSCAR format used by VASP.

To run the application, you need to modify the `main.py` script to load your structure file. Replace `"mxene.in"` with the path to your structure file:

```python
structure = load_structure("path/to/your/structure.in")
```

Then, you can run the `main.py` script:

```bash
python main.py
```

This will start a web server and open a new browser window with the 3D visualization of your crystal structure.

## Future Work

This is a very barebones project. If there's more interest, add issues to the GitHub Issues section.
# Import required libraries
from pymatgen.core import Structure
import os

def read_qe_in(file_path):
    """
    Reads a Quantum ESPRESSO input file and returns a Structure object.

    Args:
        file_path (str): The path to the input file.

    Returns:
        Structure: The Structure object representing the atomic positions and lattice vectors
            in the input file.
    """
    # Read lines from file
    with open(file_path) as f:
        lines = f.readlines()

    # Find the line number where the atomic positions start
    for i, line in enumerate(lines):
        if "ATOMIC_POSITIONS" in line:
            start_line = i + 1
            break
    # Extract the atomic positions
    atomic_positions = []
    for line in lines[start_line:]:
        if len(line.split()) != 4:
            break
        atomic_positions.append(line.strip().split())
    # Find the line number where the lattice vectors start
    for i, line in enumerate(lines):
        if "CELL_PARAMETERS" in line:
            start_line = i + 1
            break
    # Extract the lattice vectors
    lattice_vectors = []
    for line in lines[start_line:]:
        if len(line.split()) != 3:
            break
        lattice_vectors.append(line.strip().split())
    # Create the Structure object
    species = []
    coords = []
    for pos in atomic_positions:
        species.append(pos[0])
        coords.append([float(pos[1]), float(pos[2]), float(pos[3])])
    lattice = [[float(x) for x in row] for row in lattice_vectors]
    structure = Structure(lattice, species, coords)

    return structure

def load_structure(file_path):
    """
    Load a crystal structure from a file based on its file name extension.

    Args:
        file_path (str): The path to the file containing the crystal structure.

    Returns:
        Structure: A pymatgen Structure object representing the crystal structure.

    Raises:
        ValueError: If the file extension is not supported.

    Example:
        >>> structure = load_structure('/path/to/structure.cif')
        >>> print(structure)
        Full Formula (H2 O1)
        Reduced Formula: H2O
        abc   :   3.066000   3.066000   3.066000
        angles:  60.000000  60.000000  60.000000
        Sites (3)
          #  SP           a         b         c
        ---  ----  --------  --------  --------
          0  O    0.666667  0.333333  0.666667
          1  H    0.333333  0.666667  0.333333
          2  H    0.333333  0.333333  0.333333
    """

    file_name, file_extension = os.path.splitext(file_path)
    if file_extension == ".cif":
        structure = Structure.from_file(file_path)
    # TODO: write some code to read in espresso-in files
    elif file_extension == ".in":
        structure = read_qe_in(file_path)
    elif file_name == "POSCAR" or file_extension == ".vasp":
        structure = Structure.from_file(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")
    return structure

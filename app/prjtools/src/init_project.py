"""
Written by Nima Dehghani, MIT, @neurovium
Inspired by DrWatson.jl

init_project.py

Description:
    Initializes a new Python project with a specific directory and file structure.

Usage:
>>> from prjtools import init_project
>>> init_project("MyPythonProject", authors="John Doe", force=True) 
Initialized empty Git repository in /media/nima/Kepler/SciCodes/DANDI-SargoliniMoser/MyPythonProject/.git/
Project 'MyPythonProject' has been initialized.


Output Structure:
    MyPythonProject               <- Main project directory. Initialized as a Git repository.
    │
    ├── _research                 <- WIP scripts, notes, and other alpha-state files.
    │   └── tmp                   <- Temporary data folder.
    │
    ├── data                      <- Immutable and add-only.
    │   ├── sims                  <- Data from simulations.
    │   ├── exp_pro               <- Processed experimental data.
    │   └── exp_raw               <- Raw experimental data.
    │
    ├── plots                     <- Folder for plots.
    ├── notebooks                 <- Folder for Jupyter notebooks.
    ├── papers                    <- Folder for scientific papers.
    ├── scripts                   <- Folder for various scripts.
    ├── src                       <- Source code for the project.
    │
    ├── README.md                 <- README file with project information.
    ├── .gitignore                <- .gitignore file.
    └── requirements.txt          <- File containing project dependencies.
"""

import os
import subprocess

def init_project(project_name, authors=None, force=False):
    # Check if the project directory already exists
    if os.path.exists(project_name):
        if not force:
            print(f"Project '{project_name}' already exists. Use force=True to overwrite.")
            return
        else:
            print(f"Overwriting existing project '{project_name}'.")

    # Create main project directory
    os.makedirs(project_name, exist_ok=True)
    
    # Initialize Git repository in the main project directory
    subprocess.run(['git', 'init'], cwd=project_name)
    
    # Create _research and its sub-directory
    os.makedirs(os.path.join(project_name, '_research', 'tmp'), exist_ok=True)
    
    # Create data and its sub-directories
    os.makedirs(os.path.join(project_name, 'data', 'sims'), exist_ok=True)
    os.makedirs(os.path.join(project_name, 'data', 'exp_pro'), exist_ok=True)
    os.makedirs(os.path.join(project_name, 'data', 'exp_raw'), exist_ok=True)
    
    # Create other directories
    for folder in ['plots', 'notebooks', 'papers', 'scripts', 'src']:
        os.makedirs(os.path.join(project_name, folder), exist_ok=True)
    
    # Create README.md and .gitignore
    with open(os.path.join(project_name, 'README.md'), 'w') as f:
        f.write(f"# Project README\n\nAuthors: {authors if authors else 'N/A'}")
    
    with open(os.path.join(project_name, '.gitignore'), 'w') as f:
        f.write("# Add files and folders to ignore\n_research\n")
    
    # Create a requirements.txt (Python's equivalent to Manifest.toml)
    with open(os.path.join(project_name, 'requirements.txt'), 'w') as f:
        f.write("# Add your project dependencies here")

    print(f"Project '{project_name}' has been initialized.")

# Example usage:
# init_project("MyPythonProject", authors="John Doe", force=True)
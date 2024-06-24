# MyPythonProject

Written by Nima Dehghani, MIT, @neurovium
Inspired by DrWatson.jl

## Description
`init_project.py` initializes a new Python project with a specific directory and file structure.

## Usage
```python
from GeneralTools import init_project
init_project("MyPythonProject", authors="John Doe", force=True)  # force=True overwrites existing project


## Output Structure:
MyPythonProject
│
├── _research  <- Main project directory. Initialized as a Git repository.
│   └── tmp    <- Temporary data folder.
│
├── data
│   ├── sims     <- Data from simulations.
│   ├── exp_pro  <- Processed experimental data.
│   └── exp_raw  <- Immutable and add-only.
│
├── plots        <- Folder for plots.
├── notebooks    <- Folder for Jupyter notebooks.
├── papers       <- Folder for Methods/scientific papers.
├── scripts      <- Folder for various scripts.
├── src          <- Source code for the project.
│
├── README.md   <- README file with project information.
├── .gitignore
└── requirements.txt  <- File containing project dependencies.

"""

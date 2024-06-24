"""
Written by Nima Dehghani, MIT, @neurovium
Inspired by DrWatson.jl

init_project.py

Description:
    Initializes a new Python project with a specific directory and file structure.

Usage:
    from GeneralTools import init_project
    init_project("MyPythonProject", authors="John Doe", force=True)  # force=True overwrites existing project

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

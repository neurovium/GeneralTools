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
│   └── tmp
│
├── data
│   ├── sims
│   ├── exp_pro
│   └── exp_raw
│
├── plots
├── notebooks
├── papers
├── scripts
├── src
│
├── README.md
├── .gitignore
└── requirements.txt

"""

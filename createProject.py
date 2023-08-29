import os
import subprocess

def create_project_structure(project_name, authors=None, force=False):
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
create_project_structure("MyPythonProject", authors="John Doe", force=True)

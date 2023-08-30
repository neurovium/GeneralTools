Acticvate the environment:
$Conda activate nwb

Go to the directory containing the setup.py file and run the following command:

$(nwb) nima@neurobit:/media/nima/Kepler/SciCodes/GeneralTools$ python setup.py bdist_wheel sdist

$(nwb) nima@neurobit:/media/nima/Kepler/SciCodes/GeneralTools$ pip install .

$(nwb) nima@neurobit:/media/nima/Kepler/SciCodes/GeneralTools$ pip show prjtools

It should give you this output:
Name: prjtools
Version: 0.1
Summary: A collection of general utility tools
Home-page: 
Author: Nima Dehghani, MIT @neurovium
Author-email: 
License: MIT
Location: /home/nima/anaconda3/envs/nwb/lib/python3.11/site-packages
Requires: 
Required-by:


Then use it like this:
(nwb) nima@neurobit:/media/nima/Kepler/SciCodes/GeneralTools$ python
Python 3.11.5 | packaged by conda-forge | (main, Aug 27 2023, 03:34:09) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
$>>> from prjtools import init_project
$>>> init_project("GridHypergraph-py", authors="neurovium", force=True) 
Initialized empty Git repository in /media/nima/Kepler/SciCodes/GeneralTools/GridHypergraph-py/.git/
Project 'GridHypergraph-py' has been initialized.

or
$>>> init_project("/media/nima/Kepler/SciCodes/DANDI-SargoliniMoser/GridHypergraph-py", authors="neurovium", force=True) 
Initialized empty Git repository in /media/nima/Kepler/SciCodes/DANDI-SargoliniMoser/GridHypergraph-py/.git/
Project '/media/nima/Kepler/SciCodes/DANDI-SargoliniMoser/GridHypergraph-py' has been initialized.

% <!-- 
% # In your Python interpreter, print sys.path to make sure that the site-packages directory of your nwb environment is included.
% python

% '''
% import sys
% print(sys.path)

% sys.path.append('/media/nima/Kepler/SciCodes/')
% from GeneralTools import init_project
% '''

% # To remove generaltools and scicod from the sys path, you can use the following code:

% '''
% import sys

% # Get the current sys path.
% sys_path = sys.path

% # Remove generaltools and scicod from the sys path.
% sys_path = [p for p in sys_path if not p.startswith("/media/nima/Kepler/SciCodes/GeneralTools") and not p.startswith("/media/nima/Kepler/SciCodes/scicod")]

% # Set the new sys path.
% sys.path = sys_path

% # Print the new sys path.
% print(sys.path)
% '''


% #===================================================================================================

%  step-by-step guide on how to proceed.

% Step 1: Create meta.yaml
% Create a meta.yaml file in a separate folder (not within your GeneralTools folder to keep it clean). Here's a sample meta.yaml based on your project:

% yaml
% Copy code
% package:
%   name: GeneralTools
%   version: 0.1

% source:
%   path: /path/to/your/GeneralTools

% requirements:
%   build:
%     - python
%   run:
%     - python

% about:
%   home: your_project_homepage
%   license: your_license
%   summary: 'A collection of general utility tools inspired by DrWatson.jl'

% build:
%   script: python setup.py install
% Replace /path/to/your/GeneralTools with the actual path to your GeneralTools folder.

% Step 2: Build the Conda Package
% Navigate to the directory containing your meta.yaml and run:

% bash
% Copy code
% conda build .
% This will produce a .tar.bz2 package file in the conda-bld directory. -->

Step 3: Install the Package
You can install this package locally into your Conda environment with:

bash
Copy code
conda install --use-local GeneralTools
Step 4: Test the Package
Activate the Conda environment where you installed GeneralTools and try importing it in Python.

The meta.yaml file should be in a directory separate from your GeneralTools project. You can create a new folder specifically for this build if you like.
When you run conda build ., it reads from the meta.yaml file to know where the source code is (GeneralTools in your case), but it doesn't modify that directory. All build artifacts, including the .tar.bz2 package, are stored in the conda-bld directory, which is separate from your project directory.

The folder containing the meta.yaml can be anywhere you like, as long as it is not inside your GeneralTools directory. This is to ensure that your GeneralTools directory remains clean and free of any build artifacts or additional files that you don't want in there.

For example, you could create a new folder called GeneralToolsCondaBuild in a completely different location from GeneralTools, and place the meta.yaml file there. Then you would navigate to GeneralToolsCondaBuild in the terminal to run conda build ..

This way, the GeneralTools directory remains untouched, and all the build-related activities happen in GeneralToolsCondaBuild.
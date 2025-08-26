# Python Modules
# Different ways to import Modules
# 1. Import the whole module
import math
print(math.sqrt(9))  # Note the error 
# Note that you must specify the module name when calling a function within it.

# 2. import as an alias
import math as m
print(m.sqrt(25))
# This shortens the module name, this is common with libraries like numpy, pandas, etc

# 3. Import specific functions or variables
from math import sqrt, pi
print(sqrt(36))
print(pi)    #  Shows error for pie

# 4. Import everything from the module
from math import *
print(sqrt(49))
print(pi)
# This is usually not recommended because it can cause name conflict if two modules have function with the same name

# Writing Your Own Module
# Step 1: Create a folder. Name it my_module
# Step 2: Create a file inside the folder. Name it first.py
# Step 3: Create another file inside the same folder. Name it second.py
# Step 4: Create another file still inside the same folder. Name it main.py

# Python Packages
# 1. Using pip
# This is the most common method.
# It installs packages from PyPI. It is the Python's central package repository
# pip install requests           # Install latest version
# pip install requests==2.28     # Install specific version
# pip install --upgrade reguests # Upgrade existing package
# pip uninstall requests         # Remove package

# 2. Using uv
# This is the modern, super-fast package and project manager
# Recommended method: standalone installer
# macOS/Linux
# curl -LsSf https://astral.sh/uv/install.sh | sh
# or
# window
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# After installation, verify version.
# uv --version
# uv add requests         # Install package and update project files
# uv pip install flask    # Works like pip but much faster
# uv remove requests      # Unistall
# uv venv                 # Create a virtual environment automatically
# uv run script.py        # Run scripts in the managed environment

# Other packages
# pip install ... - Standard installation from PyPI
# pip install -r requirements.txt - Batch install from file
# Virtualenv + pip - Isolated environments
# conda install ... - Data science ecosystem
# Clone + pip install . - Custom or non-PyPI packages
# .whl install - Prebuilt package install
# pip install -e  - Editable (development) install
# uv ...  - All-in-one modern manager

# Creating a virtual Environment (venv)
# python -m venv virtual_environment_name
# This will create a folder inside your working folder with the name "virtual_environment_name"
# To use it, you have have to activate it.
# 1. Click on the folder
# 2. Look for Script and open it
# 3. Look for 'activate'
# 4. Right click on it and look for copy relative path
# 5. Click on it
# 6. Finally to your terminal and select command prompt then paste you copied

# Alternative, you can use this script
# virtual_environment_name\Scripts\activate  # For Windows
# source virtual_environment_name/bin/activate # linux or macOS

# Deactivating a virtual Environment
# deactivate

# Saving and sharing Requirenment
# To freeze the installed packages into a file
# pip freeze > requirements.txt

# To install them later
# pip install -r requirements.txt
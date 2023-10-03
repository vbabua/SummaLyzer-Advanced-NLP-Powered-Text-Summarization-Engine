# Import necessary libraries
import os
from pathlib import Path
import logging

# Define function to set up the project structure
def setup_project_structure(project_name):
    
    # Configure the logging module to show log messages until INFO level 
    # in the format of the timestamp followed by the actual log message
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

    # List containing path of the directories and files that are part of the project
    list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]
    # Loop through each filepath in the list of files
    for filepath in list_of_files:

        # Convert the string filepath to a Path object
        filepath = Path(filepath)
        
        # Check if the parent directory of the filepath exists
        if not filepath.parent.exists():

            # Create the parent directory if it doesn't exist
            filepath.parent.mkdir(parents=True, exist_ok=True)

            logging.info(f"Creating directory: {filepath.parent} for the file {filepath.name}")

        # Check if the file exists or if it's empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            # If the file doesn't exists or if it's empty create it
            filepath.touch()

            logging.info(f"Creating empty file: {filepath}")

        else:
            logging.info(f"{filepath.name} already exists")

if __name__ == "__main__":

    # Call the setup_project_structure with the desired project name
    setup_project_structure(project_name="textSummarizer")


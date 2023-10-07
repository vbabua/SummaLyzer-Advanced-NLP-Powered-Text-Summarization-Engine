# Import the necessary libraries and modules
import os
import yaml

from box.exceptions import BoxValueError
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List, Union

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Union[ConfigBox, None]:
    """
    Reads a YAML file and returns its contents in a ConfigBox format.

    Args:
        path_to_yaml (Path): The filesystem path to the target YAML file.

    Returns:
        ConfigBox: A ConfigBox object containing the parsed content of the YAML file.
        None: Returns None if there's an error during the operation.

    Raises:
        ValueError: Exception raised if the YAML file is found to be empty.
    """
    try:
        # Open the YAML file for reading
        with open(path_to_yaml) as yaml_file:
            # Use yaml.safe_load to parse the YAML file's content
            content = yaml.safe_load(yaml_file)
            
            # If the parsed content is empty, raise an exception
            if not content:
                raise BoxValueError
            
            # Log a successful file loading operation
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)  # Convert the content to ConfigBox and return
    
    # Handle the specific case where the YAML file is empty
    except BoxValueError:
        logger.error(f"YAML file: {path_to_yaml} is empty.")
        raise ValueError("YAML file is empty")
    
    # Handle other generic exceptions
    except Exception as e:
        logger.error(f"Error reading YAML file: {path_to_yaml}. Error: {e}")
        raise e  # Re-raise the caught exception after logging


@ensure_annotations
def create_directories(path_to_directories: List[Path], verbose: bool = True) -> None:
    """
    Create directories based on a list of specified paths.

    Args:
        path_to_directories (List[Path]): List of directory paths to be created.
        verbose (bool, optional): If True, logs each directory creation operation. Defaults to True.
    """
    for path in path_to_directories:
        # Use pathlib's mkdir method to create the directory
        # The parents=True argument ensures that parent directories are also created if they don't exist
        # The exist_ok=True argument ensures that no error is raised if the directory already exists
        Path(path).mkdir(parents=True, exist_ok=True)
        
        # If verbose is True, log the directory creation
        if verbose:
            logger.info(f"Created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a specified file in kilobytes (KB).

    Args:
        path (Path): The filesystem path to the target file.

    Returns:
        str: A string representing the file size in KB.
    """
    # Get file metadata and retrieve the file size in bytes and then convert it into kilobytes
    size_in_kb = round(path.stat().st_size / 1024)
    return f"~ {size_in_kb} KB"
    
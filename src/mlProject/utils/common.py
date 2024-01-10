import os
import yaml
import json
import joblib
from box import ConfigBox
from pathlib import Path
from ensure import ensure_annotations
from mlProject import logger

from typing import Any
from box.exceptions import BoxValueError



# Function to read a YAML file and return its content as a ConfigBox object
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: If there is an exception while reading the file.

    Returns:
        ConfigBox: ConfigBox containing the YAML content.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

# Function to create directories given a list of paths
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories based on the provided list of paths.

    Args:
        path_to_directories (list): List of paths for directories to be created.
        verbose (bool, optional): If True, logs the creation of each directory.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

# Function to save data as JSON to a specified file path
@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data as JSON to a specified file path.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")

# Function to load JSON data from a specified file path
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads JSON data from a specified file path.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

# Function to save binary data to a specified file path using joblib
@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary data to a specified file path using joblib.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

# Function to load binary data from a specified file path using joblib
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a specified file path using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

# Function to get the size of a file in kilobytes
@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

"""Validation utilities for clinerules file management."""

import os
from typing import List, Optional
from src.utils.logging_config import setup_logger
from .config import CLINERULES_DIR, DIRECTORY_STRUCTURE

logger = setup_logger(__name__)


def validate_directory_structure() -> Optional[str]:
    """
    Validate that the required directory structure exists.

    Returns:
        Error message if validation fails, None if successful
    """
    if not os.path.exists(CLINERULES_DIR):
        return f"Error: Clinerules directory not found: {CLINERULES_DIR}"

    # Check all required subdirectories
    for parent, subdirs in DIRECTORY_STRUCTURE.items():
        parent_path = os.path.join(os.getcwd(), parent)
        if not os.path.exists(parent_path):
            return f"Error: Directory not found: {parent_path}"

        for subdir in subdirs:
            subdir_path = os.path.join(parent_path, subdir)
            if not os.path.exists(subdir_path):
                return f"Error: Directory not found: {subdir_path}"

    return None


def format_directory_structure() -> List[str]:
    """
    Format the expected directory structure for display.

    Returns:
        List of lines showing the directory structure
    """
    lines = []
    lines.append("Expected directory structure:")
    lines.append("clinerules/")
    for subdir in DIRECTORY_STRUCTURE["clinerules"]:
        lines.append(f"  ├── {subdir}/")
    return lines


def validate_files_exist(files: List[str]) -> bool:
    """
    Validate that all files in the list exist.

    Args:
        files: List of file paths to validate

    Returns:
        True if all files exist, False otherwise
    """
    for file in files:
        if not os.path.exists(file):
            logger.error(f"File not found: {file}")
            return False
    return True

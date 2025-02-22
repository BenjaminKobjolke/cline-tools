"""Core functionality for managing clinerules files."""

from .config import CLINERULES_DIR, OUTPUT_DIR
from .validator import validate_directory_structure
from .file_selector import FileSelector
from .output_handler import OutputHandler

__all__ = [
    'CLINERULES_DIR',
    'OUTPUT_DIR',
    'validate_directory_structure',
    'FileSelector',
    'OutputHandler',
]

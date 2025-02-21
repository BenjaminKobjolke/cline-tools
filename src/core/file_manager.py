import os
import glob
from typing import List, Optional
from src.utils.logging_config import setup_logger

logger = setup_logger(__name__)


class FileManager:
    """Handles file operations for the clinerules system."""

    @staticmethod
    def list_files(pattern: str) -> List[str]:
        """
        List files matching the given pattern.

        Args:
            pattern: Glob pattern to match files

        Returns:
            List of normalized file paths matching the pattern
        """
        files = sorted(glob.glob(pattern))
        return [os.path.normpath(f) for f in files]

    @staticmethod
    def read_file(file_path: str) -> Optional[str]:
        """
        Read content from a file.

        Args:
            file_path: Path to the file to read

        Returns:
            File content as string or None if file cannot be read
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            logger.error(f"Could not find file: {file_path}")
            return None
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
            return None

    @staticmethod
    def write_file(file_path: str, content: str) -> bool:
        """
        Write content to a file.

        Args:
            file_path: Path to the file to write
            content: Content to write to the file

        Returns:
            True if write was successful, False otherwise
        """
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            logger.error(f"Error writing to file {file_path}: {e}")
            return False

    @staticmethod
    def ensure_directory(directory: str) -> bool:
        """
        Ensure a directory exists, create if it doesn't.

        Args:
            directory: Directory path to ensure exists

        Returns:
            True if directory exists or was created, False on error
        """
        try:
            os.makedirs(directory, exist_ok=True)
            return True
        except Exception as e:
            logger.error(f"Error creating directory {directory}: {e}")
            return False

    @staticmethod
    def merge_files(files: List[str]) -> Optional[str]:
        """
        Merge content of multiple files.

        Args:
            files: List of file paths to merge

        Returns:
            Merged content of all files or None if error occurs
        """
        try:
            content = []
            for file in files:
                file_content = FileManager.read_file(file)
                if file_content is not None:
                    content.append(file_content.strip())
                else:
                    return None
            return "\n\n".join(content)
        except Exception as e:
            logger.error(f"Error merging files: {e}")
            return None

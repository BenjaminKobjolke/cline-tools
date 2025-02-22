"""Output handling functionality for clinerules files."""

import os
from typing import List, Optional
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager
from .config import OUTPUT_DIR, OUTPUT_FILE

logger = setup_logger(__name__)


class OutputHandler:
    """Handles output file creation and management."""

    def __init__(self):
        """Initialize OutputHandler with required components."""
        self.file_manager = FileManager()

    def ensure_output_directory(self) -> bool:
        """
        Ensure output directory exists.

        Returns:
            True if directory exists or was created, False on error
        """
        try:
            if not os.path.exists(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)
            return True
        except Exception as e:
            logger.error(f"Error creating output directory: {e}")
            return False

    def merge_files(self, files: List[str]) -> Optional[str]:
        """
        Merge content from multiple files.

        Args:
            files: List of file paths to merge

        Returns:
            Merged content or None if error occurs
        """
        if not files:
            logger.error("No files provided for merging")
            return None

        try:
            content = []
            for file in files:
                file_content = self.file_manager.read_file(file)
                if file_content is not None:
                    content.append(file_content.strip())
                else:
                    return None
            return "\n\n".join(content)
        except Exception as e:
            logger.error(f"Error merging files: {e}")
            return None

    def create_output_file(self, content: str) -> bool:
        """
        Create output file with provided content.

        Args:
            content: Content to write to file

        Returns:
            True if file was created successfully, False otherwise
        """
        if not self.ensure_output_directory():
            return False

        return self.file_manager.write_file(OUTPUT_FILE, content)

    def process_files(self, files: List[str]) -> bool:
        """
        Process files and create output file.

        Args:
            files: List of file paths to process

        Returns:
            True if processing was successful, False otherwise
        """
        if not files:
            logger.error("No files selected for processing")
            return False

        merged_content = self.merge_files(files)
        if merged_content is None:
            return False

        if not self.create_output_file(merged_content):
            return False

        logger.info(f"Files merged successfully into {OUTPUT_FILE}")
        logger.info("Merged files:")
        for file in files:
            logger.info(f"- {os.path.basename(file)}")

        return True

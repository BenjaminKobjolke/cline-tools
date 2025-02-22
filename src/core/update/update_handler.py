"""Update handling functionality for clinerules files."""

import os
from typing import Optional, Tuple
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager
from src.core.block_extractor import BlockExtractor
from src.core.rules.file_selector import FileSelector
from src.utils.input_handler import InputHandler

logger = setup_logger(__name__)


class UpdateHandler:
    """Handles update operations for clinerules files."""

    def __init__(self):
        """Initialize UpdateHandler with required components."""
        self.file_manager = FileManager()
        self.block_extractor = BlockExtractor()
        self.file_selector = FileSelector()
        self.input_handler = InputHandler()

    def validate_files(self, external_file: str) -> bool:
        """
        Validate that required files and directories exist.

        Args:
            external_file: Path to external rules file

        Returns:
            True if validation passes, False otherwise
        """
        # Check if external file exists
        if not os.path.exists(external_file):
            logger.error(f"External file not found: {external_file}")
            return False

        # Get local files
        general_files, system_files, project_files, language_files = self.file_selector.get_files_by_category()
        if not any([general_files, system_files, project_files, language_files]):
            logger.error("No local files found")
            return False

        return True

    def select_local_file(self) -> Optional[str]:
        """
        Display and select a local file.

        Returns:
            Selected file path or None if no selection made
        """
        # Get files by category
        general_files, system_files, project_files, language_files = self.file_selector.get_files_by_category()

        # Display files by category
        self.file_selector.display_files_by_category(
            general_files, system_files, project_files, language_files
        )

        # Get user selection
        all_files = general_files + system_files + project_files + language_files
        if not all_files:
            logger.error("No files found")
            return None

        return self.input_handler.get_valid_selection(
            all_files, "\nSelect file: "
        )

    def extract_block(self, content: str, block_type: str, file_path: str) -> Optional[str]:
        """
        Extract block from content.

        Args:
            content: File content to extract from
            block_type: Type of block to extract
            file_path: Path to file being processed

        Returns:
            Extracted block or None if extraction fails
        """
        block = self.block_extractor.extract_block(content, block_type, file_path)
        if block is None:
            logger.error(f"Could not extract block from file: {file_path}")
            return None
        return block

    def replace_block(
        self, content: str, new_block: str, block_type: str, file_path: str
    ) -> Optional[str]:
        """
        Replace block in content.

        Args:
            content: Original content
            new_block: New block content
            block_type: Type of block to replace
            file_path: Path to file being processed

        Returns:
            Updated content or None if replacement fails
        """
        updated_content = self.block_extractor.replace_block(
            content, new_block, block_type, file_path
        )
        if updated_content is None:
            logger.error(f"Could not replace block in file: {file_path}")
            return None
        return updated_content

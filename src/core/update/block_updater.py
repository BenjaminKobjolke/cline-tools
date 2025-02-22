"""Block update functionality for clinerules files."""

import os
from typing import Optional, Tuple
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager
from src.core.block_extractor import BlockExtractor
from .update_handler import UpdateHandler

logger = setup_logger(__name__)


class BlockUpdater:
    """Handles block update operations for clinerules files."""

    def __init__(self):
        """Initialize BlockUpdater with required components."""
        self.file_manager = FileManager()
        self.block_extractor = BlockExtractor()
        self.update_handler = UpdateHandler()

    def update_local_with_external(self, external_file: str, local_file: str) -> bool:
        """
        Update local file with block from external file.

        Args:
            external_file: Path to external rules file
            local_file: Path to local file to update

        Returns:
            True if update was successful, False otherwise
        """
        try:
            # Read file contents
            external_content = self.file_manager.read_file(external_file)
            if external_content is None:
                logger.error(f"Error reading external file: {external_file}")
                return False

            # Determine block type
            block_type = self.block_extractor.determine_block_type(local_file)
            if not block_type:
                logger.error(f"Could not determine block type from path: {local_file}")
                return False

            # Extract block from external file
            block = self.update_handler.extract_block(
                external_content, block_type, local_file
            )
            if block is None:
                return False

            # Write block to local file
            if not self.file_manager.write_file(local_file, block):
                logger.error(f"Error writing to local file: {local_file}")
                return False

            logger.info(f"Successfully updated {os.path.basename(local_file)}")
            return True

        except Exception as e:
            logger.error(f"Error updating local file: {e}")
            return False

    def update_external_with_local(self, external_file: str, local_file: str) -> bool:
        """
        Update external file with block from local file.

        Args:
            external_file: Path to external rules file
            local_file: Path to local file to use

        Returns:
            True if update was successful, False otherwise
        """
        try:
            # Read file contents
            local_content = self.file_manager.read_file(local_file)
            external_content = self.file_manager.read_file(external_file)
            if local_content is None or external_content is None:
                logger.error("Error reading files")
                return False

            # Determine block type
            block_type = self.block_extractor.determine_block_type(local_file)
            if not block_type:
                logger.error(f"Could not determine block type from path: {local_file}")
                return False

            # Replace block in external file
            updated_content = self.update_handler.replace_block(
                external_content, local_content, block_type, local_file
            )
            if updated_content is None:
                return False

            # Write updated content back to external file
            if not self.file_manager.write_file(external_file, updated_content):
                logger.error(f"Error writing to external file: {external_file}")
                return False

            logger.info(f"Successfully updated block in {os.path.basename(external_file)}")
            logger.info(f"Using content from {os.path.basename(local_file)}")
            return True

        except Exception as e:
            logger.error(f"Error updating external file: {e}")
            return False

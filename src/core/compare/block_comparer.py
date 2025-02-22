"""Block comparison functionality for clinerules files."""

import os
from typing import Optional, Tuple
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager
from src.core.block_extractor import BlockExtractor

logger = setup_logger(__name__)


class BlockComparer:
    """Handles comparison of clinerules blocks."""

    def __init__(self):
        """Initialize BlockComparer with required components."""
        self.file_manager = FileManager()
        self.block_extractor = BlockExtractor()

    def extract_blocks(
        self, external_file: str, local_file: str
    ) -> Optional[Tuple[str, str, str]]:
        """
        Extract blocks from external and local files.

        Args:
            external_file: Path to external rules file
            local_file: Path to local rules file

        Returns:
            Tuple of (external_block, local_block, block_type) or None if extraction fails
        """
        try:
            # Read file contents
            external_content = self.file_manager.read_file(external_file)
            local_content = self.file_manager.read_file(local_file)

            if external_content is None or local_content is None:
                logger.error("Error reading files")
                return None

            # Determine block type
            block_type = self.block_extractor.determine_block_type(local_file)
            if not block_type:
                logger.error(f"Could not determine block type from path: {local_file}")
                return None

            # Extract blocks
            external_block = self.block_extractor.extract_block(
                external_content, block_type, local_file
            )
            local_block = self.block_extractor.extract_block(
                local_content, block_type, local_file
            )

            if external_block is None or local_block is None:
                logger.error("Could not extract blocks for comparison")
                return None

            return external_block, local_block, block_type

        except Exception as e:
            logger.error(f"Error extracting blocks: {e}")
            return None

    def are_blocks_identical(self, external_block: str, local_block: str) -> bool:
        """
        Check if blocks are identical.

        Args:
            external_block: Content from external file
            local_block: Content from local file

        Returns:
            True if blocks are identical, False otherwise
        """
        return external_block.strip() == local_block.strip()

    def validate_files(self, external_file: str, local_file: str) -> bool:
        """
        Validate that both files exist.

        Args:
            external_file: Path to external rules file
            local_file: Path to local rules file

        Returns:
            True if both files exist, False otherwise
        """
        if not os.path.exists(external_file):
            logger.error(f"External file not found: {external_file}")
            return False

        if not os.path.exists(local_file):
            logger.error(f"Local file not found: {local_file}")
            return False

        return True

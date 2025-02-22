import os
import re
from typing import Optional, Tuple
from src.utils.logging_config import setup_logger

logger = setup_logger(__name__)


class BlockExtractor:
    """Handles extraction of blocks from clinerules files."""

    BLOCK_TYPES = {
        "LANGUAGE": r"clinerules_language_(\w+)\.md",
        "SYSTEM": "SYSTEM",
        "PROJECT": "PROJECT",
        "GENERAL": "GENERAL",
    }

    @staticmethod
    def determine_block_type(file_path: str) -> Optional[str]:
        """
        Determine block type based on file path.

        Args:
            file_path: Path to the file

        Returns:
            Block type (GENERAL, LANGUAGE, SYSTEM, or PROJECT) or None if unknown
        """
        path_parts = file_path.lower().split(os.sep)
        if "clinerules" in path_parts:
            clinerules_index = path_parts.index("clinerules")
            if len(path_parts) > clinerules_index + 1:
                category = path_parts[clinerules_index + 1]
                if category == "general":
                    return "GENERAL"
                elif category == "languages":
                    return "LANGUAGE"
                elif category == "system":
                    return "SYSTEM"
                elif category == "project":
                    return "PROJECT"
        return None

    @classmethod
    def get_start_pattern(cls, block_type: str, filename: str) -> Optional[str]:
        """
        Get the start pattern for a block type.

        Args:
            block_type: Type of block (GENERAL, LANGUAGE, SYSTEM, or PROJECT)
            filename: Name of file being processed

        Returns:
            Start pattern string or None if pattern cannot be determined
        """
        if block_type == "LANGUAGE":
            match = re.search(cls.BLOCK_TYPES["LANGUAGE"], filename)
            if match:
                language = match.group(1).upper()
                return f"### BEGIN LANGUAGE {language}"
            return None
        elif block_type in cls.BLOCK_TYPES:
            if block_type == "GENERAL":
                return "### BEGIN GENERAL RULES"
            return f"### BEGIN {block_type}"
        return None

    @classmethod
    def extract_block(
        cls, content: str, block_type: str, filename: str
    ) -> Optional[str]:
        """
        Extract block from content based on type.

        Args:
            content: File content to extract from
            block_type: Type of block to extract (GENERAL, LANGUAGE, SYSTEM, or PROJECT)
            filename: Name of file being processed

        Returns:
            Extracted block content or None if block cannot be found
        """
        start_pattern = cls.get_start_pattern(block_type, filename)
        if not start_pattern:
            logger.warning(f"Could not determine start pattern for {filename}")
            return None

        # Find the start of the block
        start_match = content.find(start_pattern)
        if start_match == -1:
            logger.warning(
                f"Could not find start pattern '{start_pattern}' in {filename}"
            )
            return None

        # Get content from start pattern
        block_content = content[start_match:]

        # Find next BEGIN marker if it exists
        next_begin = re.search(r"### BEGIN", block_content[len(start_pattern) :])
        if next_begin:
            # Cut off at next BEGIN
            block_content = block_content[
                : len(start_pattern) + next_begin.start()
            ].strip()

        return block_content.strip()

    @classmethod
    def find_block_bounds(
        cls, content: str, block_type: str, filename: str
    ) -> Optional[Tuple[int, int]]:
        """
        Find the start and end positions of a block in content.

        Args:
            content: Content to search in
            block_type: Type of block to find
            filename: Name of file being processed

        Returns:
            Tuple of (start_pos, end_pos) or None if block not found
        """
        start_pattern = cls.get_start_pattern(block_type, filename)
        if not start_pattern:
            return None

        # Find the start of the block
        start_match = content.find(start_pattern)
        if start_match == -1:
            return None

        # Get content from start pattern
        remaining = content[start_match:]

        # Find next BEGIN marker if it exists
        next_begin = re.search(r"### BEGIN", remaining[len(start_pattern) :])
        if next_begin:
            end_pos = start_match + len(start_pattern) + next_begin.start()
        else:
            end_pos = len(content)

        return (start_match, end_pos)

    @classmethod
    def replace_block(
        cls, content: str, new_block: str, block_type: str, filename: str
    ) -> Optional[str]:
        """
        Replace a block in content with new block content.

        Args:
            content: Original content
            new_block: New block content to insert
            block_type: Type of block to replace
            filename: Name of file being processed

        Returns:
            Updated content with block replaced or None if block not found
        """
        bounds = cls.find_block_bounds(content, block_type, filename)
        if not bounds:
            return None

        start_pos, end_pos = bounds
        return content[:start_pos] + new_block + content[end_pos:]

    @classmethod
    def compare_blocks(
        cls, external_content: str, local_content: str, block_type: str, filename: str
    ) -> bool:
        """
        Compare two blocks of content.

        Args:
            external_content: Content from external file
            local_content: Content from local file
            block_type: Type of block to compare
            filename: Name of file being processed

        Returns:
            True if blocks are identical, False otherwise
        """
        external_block = cls.extract_block(external_content, block_type, filename)
        local_block = cls.extract_block(local_content, block_type, filename)

        if external_block is None or local_block is None:
            logger.error("Could not extract blocks for comparison")
            return False

        return external_block == local_block

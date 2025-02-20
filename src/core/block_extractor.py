import re
from typing import Optional
from src.utils.logging_config import setup_logger

logger = setup_logger(__name__)

class BlockExtractor:
    """Handles extraction of blocks from clinerules files."""

    BLOCK_TYPES = {
        'LANGUAGE': r'clinerules_language_(\w+)\.md',
        'SYSTEM': 'SYSTEM',
        'PROJECT': 'PROJECT'
    }

    @staticmethod
    def determine_block_type(file_path: str) -> Optional[str]:
        """
        Determine block type based on file path.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Block type (LANGUAGE, SYSTEM, or PROJECT) or None if unknown
        """
        path_lower = file_path.lower()
        if 'languages' in path_lower:
            return 'LANGUAGE'
        elif 'system' in path_lower:
            return 'SYSTEM'
        elif 'project' in path_lower:
            return 'PROJECT'
        return None

    @classmethod
    def get_start_pattern(cls, block_type: str, filename: str) -> Optional[str]:
        """
        Get the start pattern for a block type.
        
        Args:
            block_type: Type of block (LANGUAGE, SYSTEM, or PROJECT)
            filename: Name of file being processed
            
        Returns:
            Start pattern string or None if pattern cannot be determined
        """
        if block_type == 'LANGUAGE':
            match = re.search(cls.BLOCK_TYPES['LANGUAGE'], filename)
            if match:
                language = match.group(1).upper()
                return f"### BEGIN LANGUAGE {language}"
            return None
        elif block_type in cls.BLOCK_TYPES:
            return f"### BEGIN {block_type}"
        return None

    @classmethod
    def extract_block(cls, content: str, block_type: str, filename: str) -> Optional[str]:
        """
        Extract block from content based on type.
        
        Args:
            content: File content to extract from
            block_type: Type of block to extract (LANGUAGE, SYSTEM, or PROJECT)
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
            logger.warning(f"Could not find start pattern '{start_pattern}' in {filename}")
            return None

        # Get content from start pattern
        block_content = content[start_match:]
        
        # Find next BEGIN marker if it exists
        next_begin = re.search(r'### BEGIN', block_content[len(start_pattern):])
        if next_begin:
            # Cut off at next BEGIN
            block_content = block_content[:len(start_pattern) + next_begin.start()].strip()
        
        return block_content.strip()

    @classmethod
    def compare_blocks(cls, external_content: str, local_content: str, 
                      block_type: str, filename: str) -> bool:
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

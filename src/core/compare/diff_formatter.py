"""Diff formatting functionality for clinerules files."""

import os
import tempfile
import subprocess
from typing import Optional, Tuple
from src.utils.logging_config import setup_logger
from src.core.diff_handler import DiffHandler

logger = setup_logger(__name__)


class DiffFormatter:
    """Handles formatting and display of file differences."""

    def __init__(self):
        """Initialize DiffFormatter with required components."""
        self.diff_handler = DiffHandler()

    def create_temp_files(
        self, external_block: str, local_block: str, block_type: str
    ) -> Tuple[str, str]:
        """
        Create temporary files for diff comparison.

        Args:
            external_block: Content from external file
            local_block: Content from local file
            block_type: Type of block being compared

        Returns:
            Tuple of (external_temp_path, local_temp_path)
        """
        # Create temp files with meaningful names
        ext_fd, ext_path = tempfile.mkstemp(prefix=f"external_{block_type}_", suffix=".md")
        loc_fd, loc_path = tempfile.mkstemp(prefix=f"local_{block_type}_", suffix=".md")

        try:
            with os.fdopen(ext_fd, 'w') as ext_file:
                ext_file.write(external_block)
            with os.fdopen(loc_fd, 'w') as loc_file:
                loc_file.write(local_block)
        except Exception as e:
            logger.error(f"Error writing temp files: {e}")
            os.unlink(ext_path)
            os.unlink(loc_path)
            raise

        return ext_path, loc_path

    def cleanup_temp_files(self, *file_paths: str) -> None:
        """
        Clean up temporary files.

        Args:
            file_paths: Paths to files to delete
        """
        for path in file_paths:
            try:
                os.unlink(path)
            except Exception as e:
                logger.error(f"Error deleting temp file {path}: {e}")

    def show_diff(
        self, external_block: str, local_block: str, block_type: str, use_git_diff: bool
    ) -> bool:
        """
        Show differences between blocks using selected diff tool.

        Args:
            external_block: Content from external file
            local_block: Content from local file
            block_type: Type of block being compared
            use_git_diff: Whether to use git diff instead of VS Code

        Returns:
            True if diff was displayed successfully, False otherwise
        """
        try:
            # Create temp files
            ext_path, loc_path = self.create_temp_files(
                external_block, local_block, block_type
            )

            # Show diff using selected tool
            success = self.diff_handler.compare_with_diff_tool(
                external_block, local_block, block_type, use_git_diff
            )

            # Cleanup
            self.cleanup_temp_files(ext_path, loc_path)

            return success

        except Exception as e:
            logger.error(f"Error showing diff: {e}")
            return False

    def format_block_info(self, block_type: str, file_path: str) -> str:
        """
        Format block information for display.

        Args:
            block_type: Type of block
            file_path: Path to file containing block

        Returns:
            Formatted block information string
        """
        return (
            f"\nBlock Type: {block_type}\n"
            f"File: {os.path.basename(file_path)}\n"
            f"Path: {file_path}\n"
        )

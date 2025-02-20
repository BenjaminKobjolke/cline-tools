import os
import subprocess
from typing import Optional, Tuple
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager

logger = setup_logger(__name__)

class DiffHandler:
    """Handles diff operations between files."""

    def __init__(self):
        """Initialize DiffHandler with a temporary directory."""
        self.tmp_dir = 'tmp'
        FileManager.ensure_directory(self.tmp_dir)

    def create_temp_files(self, external_block: str, local_block: str, 
                         block_type: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Create temporary files for diff comparison.
        
        Args:
            external_block: Content from external file
            local_block: Content from local file
            block_type: Type of block being compared
            
        Returns:
            Tuple of (external_tmp_path, local_tmp_path) or (None, None) on error
        """
        try:
            external_tmp = os.path.join(self.tmp_dir, f'external_{block_type.lower()}_block.md')
            local_tmp = os.path.join(self.tmp_dir, f'local_{block_type.lower()}_block.md')

            if not FileManager.write_file(external_tmp, external_block):
                return None, None
            if not FileManager.write_file(local_tmp, local_block):
                return None, None

            return external_tmp, local_tmp
        except Exception as e:
            logger.error(f"Error creating temporary files: {e}")
            return None, None

    def run_git_diff(self, external_tmp: str, local_tmp: str) -> bool:
        """
        Run git diff command between two files.
        
        Args:
            external_tmp: Path to external temporary file
            local_tmp: Path to local temporary file
            
        Returns:
            True if diff command executed successfully, False otherwise
        """
        try:
            diff_command = [
                'git', 'diff', '--no-index',
                '--color=always',
                '--word-diff=color',
                external_tmp, local_tmp
            ]
            subprocess.run(diff_command)
            return True
        except subprocess.CalledProcessError:
            # git diff returns non-zero exit code if files are different
            return True
        except Exception as e:
            logger.error(f"Error running git diff: {e}")
            return False

    def run_vscode_diff(self, external_tmp: str, local_tmp: str) -> bool:
        """
        Run VS Code diff command between two files.
        
        Args:
            external_tmp: Path to external temporary file
            local_tmp: Path to local temporary file
            
        Returns:
            True if diff command executed successfully, False otherwise
        """
        try:
            diff_command = f'code --diff "{external_tmp}" "{local_tmp}"'
            subprocess.run(diff_command, shell=True)
            return True
        except Exception as e:
            logger.error(f"Error running VS Code diff: {e}")
            return False

    def compare_with_diff_tool(self, external_block: str, local_block: str, 
                             block_type: str, use_git_diff: bool = True) -> bool:
        """
        Compare blocks using selected diff tool.
        
        Args:
            external_block: Content from external file
            local_block: Content from local file
            block_type: Type of block being compared
            use_git_diff: Whether to use git diff (True) or VS Code diff (False)
            
        Returns:
            True if diff operation was successful, False otherwise
        """
        # Create temporary files
        tmp_files = self.create_temp_files(external_block, local_block, block_type)
        if tmp_files == (None, None):
            return False

        external_tmp, local_tmp = tmp_files

        # Run diff command
        if use_git_diff:
            return self.run_git_diff(external_tmp, local_tmp)
        else:
            return self.run_vscode_diff(external_tmp, local_tmp)

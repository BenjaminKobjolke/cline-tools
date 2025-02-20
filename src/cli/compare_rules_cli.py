import os
import argparse
from typing import Optional, List
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager
from src.core.block_extractor import BlockExtractor
from src.core.diff_handler import DiffHandler
from src.utils.input_handler import InputHandler

logger = setup_logger(__name__)

class CompareRulesCLI:
    """CLI interface for comparing clinerules files."""

    def __init__(self):
        """Initialize CompareRulesCLI with required components."""
        self.file_manager = FileManager()
        self.block_extractor = BlockExtractor()
        self.diff_handler = DiffHandler()
        self.input_handler = InputHandler()

    def get_files_by_category(self) -> tuple[List[str], List[str], List[str]]:
        """
        Get files organized by category.
        
        Returns:
            Tuple of (system_files, project_files, language_files)
        """
        current_dir = os.getcwd()
        system_files = self.file_manager.list_files(
            os.path.join(current_dir, 'system', 'clinerules_*')
        )
        project_files = self.file_manager.list_files(
            os.path.join(current_dir, 'project', 'clinerules_*')
        )
        language_files = self.file_manager.list_files(
            os.path.join(current_dir, 'languages', 'clinerules_*')
        )
        return system_files, project_files, language_files

    def display_and_select_file(self, system_files: List[str], 
                              project_files: List[str], 
                              language_files: List[str]) -> Optional[str]:
        """
        Display files and get user selection.
        
        Args:
            system_files: List of system rule files
            project_files: List of project rule files
            language_files: List of language rule files
            
        Returns:
            Selected file path or None if no selection made
        """
        all_files = []
        current_number = 1

        # Display system files
        if system_files:
            current_number = self.input_handler.display_files_with_numbers(
                system_files, "System", current_number
            )
            all_files.extend(system_files)

        # Display project files
        if project_files:
            current_number = self.input_handler.display_files_with_numbers(
                project_files, "Project", current_number
            )
            all_files.extend(project_files)

        # Display language files
        if language_files:
            current_number = self.input_handler.display_files_with_numbers(
                language_files, "Language", current_number
            )
            all_files.extend(language_files)

        if not all_files:
            logger.error("\nNo files found to compare")
            logger.error("Make sure you're running the script from the correct directory")
            logger.error(f"Current directory: {os.getcwd()}")
            return None

        return self.input_handler.get_valid_selection(all_files, "\nSelect file number to compare: ")

    def compare_rules_files(self, external_file: str) -> bool:
        """
        Compare rules files and show differences.
        
        Args:
            external_file: Path to external rules file to compare against
            
        Returns:
            True if comparison was successful, False otherwise
        """
        try:
            # Check if external file exists
            if not os.path.exists(external_file):
                logger.error(f"Error: File not found: {external_file}")
                return False

            # Get and display files by category
            system_files, project_files, language_files = self.get_files_by_category()
            local_file = self.display_and_select_file(system_files, project_files, language_files)
            
            if not local_file:
                return False

            # Read file contents
            external_content = self.file_manager.read_file(external_file)
            local_content = self.file_manager.read_file(local_file)
            
            if external_content is None or local_content is None:
                return False

            # Determine block type
            block_type = self.block_extractor.determine_block_type(local_file)
            if not block_type:
                logger.error(f"Could not determine block type from path: {local_file}")
                return False

            # Extract blocks
            external_block = self.block_extractor.extract_block(
                external_content, block_type, local_file
            )
            local_block = self.block_extractor.extract_block(
                local_content, block_type, local_file
            )

            if external_block is None or local_block is None:
                logger.error("Could not extract blocks for comparison")
                return False

            # Check if blocks are identical
            if external_block == local_block:
                print("\nBlocks are identical")
                return True

            # Get diff tool choice and compare
            use_git_diff = self.input_handler.get_diff_tool_choice()
            return self.diff_handler.compare_with_diff_tool(
                external_block, local_block, block_type, use_git_diff
            )

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return False

def main() -> None:
    """Main entry point for compare_rules CLI."""
    parser = argparse.ArgumentParser(description='Compare clinerules blocks between files')
    parser.add_argument('external_file', help='Path to external clinerules file')
    args = parser.parse_args()

    cli = CompareRulesCLI()
    if not cli.compare_rules_files(args.external_file):
        logger.error("Failed to compare rules files")

if __name__ == '__main__':
    main()

"""CLI interface for comparing clinerules files."""

import argparse
from typing import Optional
from src.utils.logging_config import setup_logger
from src.utils.input_handler import InputHandler
from src.core.rules.file_selector import FileSelector
from src.core.compare.block_comparer import BlockComparer
from src.core.compare.diff_formatter import DiffFormatter

logger = setup_logger(__name__)


class CompareRulesCLI:
    """CLI interface for comparing clinerules files."""

    def __init__(self):
        """Initialize CompareRulesCLI with required components."""
        self.file_selector = FileSelector()
        self.block_comparer = BlockComparer()
        self.diff_formatter = DiffFormatter()
        self.input_handler = InputHandler()

    def compare_rules_files(self, external_file: str) -> bool:
        """
        Compare rules files and show differences.

        Args:
            external_file: Path to external rules file to compare against

        Returns:
            True if comparison was successful, False otherwise
        """
        try:
            # Get files by category
            general_files, system_files, project_files, language_files = self.file_selector.get_files_by_category()

            # Display files by category
            self.file_selector.display_files_by_category(
                general_files, system_files, project_files, language_files
            )

            # Get user selection
            all_files = general_files + system_files + project_files + language_files
            if not all_files:
                print("\nNo files found to compare")
                return False

            local_file = self.input_handler.get_valid_selection(
                all_files, "\nSelect file number to compare: "
            )
            if not local_file:
                return False

            # Validate files
            if not self.block_comparer.validate_files(external_file, local_file):
                return False

            # Extract blocks for comparison
            result = self.block_comparer.extract_blocks(external_file, local_file)
            if result is None:
                return False

            external_block, local_block, block_type = result

            # Check if blocks are identical
            if self.block_comparer.are_blocks_identical(external_block, local_block):
                print("\nBlocks are identical")
                return True

            # Show block information
            print(self.diff_formatter.format_block_info(block_type, local_file))

            # Get diff tool choice and show diff
            use_git_diff = self.input_handler.get_diff_tool_choice()
            return self.diff_formatter.show_diff(
                external_block, local_block, block_type, use_git_diff
            )

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return False


def main() -> None:
    """Main entry point for compare_rules CLI."""
    parser = argparse.ArgumentParser(
        description="Compare clinerules blocks between files"
    )
    parser.add_argument("external_file", help="Path to external clinerules file")
    args = parser.parse_args()

    cli = CompareRulesCLI()
    if not cli.compare_rules_files(args.external_file):
        print("Failed to compare rules files")


if __name__ == "__main__":
    main()

"""CLI interface for creating clinerules files."""

from typing import Optional
from src.utils.logging_config import setup_logger
from src.core.rules.validator import validate_directory_structure, format_directory_structure
from src.core.rules.file_selector import FileSelector
from src.core.rules.output_handler import OutputHandler

logger = setup_logger(__name__)


class CreateRulesCLI:
    """CLI interface for creating clinerules files."""

    def __init__(self):
        """Initialize CreateRulesCLI with required components."""
        self.file_selector = FileSelector()
        self.output_handler = OutputHandler()

    def create_rules_file(self) -> bool:
        """
        Create a new clinerules file from selected components.

        Returns:
            True if file was created successfully, False otherwise
        """
        try:
            # Validate directory structure
            error_msg = validate_directory_structure()
            if error_msg:
                print(error_msg)
                print()
                print("\n".join(format_directory_structure()))
                return False

            # Select files from all categories
            selected_files = self.file_selector.select_all_files()

            # Check if any files were selected
            if not selected_files:
                print("\nError: No sections were selected. At least one section is required.")
                return False

            # Process files and create output
            return self.output_handler.process_files(selected_files)

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return False


def main() -> None:
    """Main entry point for create_rules CLI."""
    cli = CreateRulesCLI()
    if not cli.create_rules_file():
        print("Failed to create rules file")


if __name__ == "__main__":
    main()

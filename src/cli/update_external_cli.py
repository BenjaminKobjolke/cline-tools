import os
import argparse
from typing import Optional, List
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager
from src.core.block_extractor import BlockExtractor
from src.utils.input_handler import InputHandler

logger = setup_logger(__name__)


class UpdateExternalCLI:
    """CLI interface for updating external clinerules files with local content."""

    def __init__(self):
        """Initialize UpdateExternalCLI with required components."""
        self.file_manager = FileManager()
        self.block_extractor = BlockExtractor()
        self.input_handler = InputHandler()
        self.clinerules_dir = os.path.join(os.getcwd(), "clinerules")

    def get_local_files(self) -> List[str]:
        """
        Get all local clinerules files.

        Returns:
            List of file paths
        """
        all_files = []

        # Get files from each directory
        general_files = self.file_manager.list_files(
            os.path.join(self.clinerules_dir, "general", "clinerules_*")
        )
        system_files = self.file_manager.list_files(
            os.path.join(self.clinerules_dir, "system", "clinerules_*")
        )
        project_files = self.file_manager.list_files(
            os.path.join(self.clinerules_dir, "project", "clinerules_*")
        )
        language_files = self.file_manager.list_files(
            os.path.join(self.clinerules_dir, "languages", "clinerules_*")
        )

        # Display files with continuous numbering
        current_number = 1

        if general_files:
            current_number = self.input_handler.display_files_with_numbers(
                general_files, "General", current_number
            )
            all_files.extend(general_files)

        if system_files:
            current_number = self.input_handler.display_files_with_numbers(
                system_files, "System", current_number
            )
            all_files.extend(system_files)

        if project_files:
            current_number = self.input_handler.display_files_with_numbers(
                project_files, "Project", current_number
            )
            all_files.extend(project_files)

        if language_files:
            current_number = self.input_handler.display_files_with_numbers(
                language_files, "Language", current_number
            )
            all_files.extend(language_files)

        return all_files

    def update_external_file(self, external_file: str) -> bool:
        """
        Update external file with content from local file.

        Args:
            external_file: Path to external clinerules file

        Returns:
            True if update was successful, False otherwise
        """
        try:
            # Check if external file exists
            if not os.path.exists(external_file):
                print(f"Error: External file not found: {external_file}")
                return False

            # Check if clinerules directory exists
            if not os.path.exists(self.clinerules_dir):
                print(f"Error: Clinerules directory not found: {self.clinerules_dir}")
                print("\nExpected directory structure:")
                print("clinerules/")
                print("  ├── general/")
                print("  ├── system/")
                print("  ├── project/")
                print("  └── languages/")
                return False

            # Get and display local files
            local_files = self.get_local_files()
            if not local_files:
                print("No local files found")
                return False

            # Get user selection
            local_file = self.input_handler.get_valid_selection(
                local_files, "\nSelect file to use: "
            )
            if not local_file:
                return False

            # Read file contents
            local_content = self.file_manager.read_file(local_file)
            external_content = self.file_manager.read_file(external_file)
            if local_content is None or external_content is None:
                print("Error reading files")
                return False

            # Determine block type
            block_type = self.block_extractor.determine_block_type(local_file)
            if not block_type:
                print(f"Could not determine block type from path: {local_file}")
                return False

            # Replace block in external file
            updated_content = self.block_extractor.replace_block(
                external_content, local_content, block_type, local_file
            )
            if updated_content is None:
                print("Could not find matching block in external file")
                return False

            # Write updated content back to external file
            if not self.file_manager.write_file(external_file, updated_content):
                print(f"Error writing to external file: {external_file}")
                return False

            print(f"\nSuccessfully updated block in {os.path.basename(external_file)}")
            print(f"Using content from {os.path.basename(local_file)}")
            return True

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return False


def main() -> None:
    """Main entry point for update_external CLI."""
    parser = argparse.ArgumentParser(
        description="Update external clinerules file with content from local file"
    )
    parser.add_argument("external_file", help="Path to external clinerules file")
    args = parser.parse_args()

    cli = UpdateExternalCLI()
    if not cli.update_external_file(args.external_file):
        print("Failed to update external file")


if __name__ == "__main__":
    main()

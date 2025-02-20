import os
import argparse
from typing import Optional, List
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager
from src.core.block_extractor import BlockExtractor
from src.utils.input_handler import InputHandler

logger = setup_logger(__name__)

class UpdateLocalCLI:
    """CLI interface for updating local clinerules files with external content."""

    def __init__(self):
        """Initialize UpdateLocalCLI with required components."""
        self.file_manager = FileManager()
        self.block_extractor = BlockExtractor()
        self.input_handler = InputHandler()
        self.clinerules_dir = os.path.join(os.getcwd(), 'clinerules')

    def get_local_files(self) -> List[str]:
        """
        Get all local clinerules files.
        
        Returns:
            List of file paths
        """
        all_files = []
        
        # Get files from each directory
        system_files = self.file_manager.list_files(
            os.path.join(self.clinerules_dir, 'system', 'clinerules_*')
        )
        project_files = self.file_manager.list_files(
            os.path.join(self.clinerules_dir, 'project', 'clinerules_*')
        )
        language_files = self.file_manager.list_files(
            os.path.join(self.clinerules_dir, 'languages', 'clinerules_*')
        )

        # Display files with continuous numbering
        current_number = 1
        
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

    def update_local_file(self, external_file: str) -> bool:
        """
        Update a local file with content from external file.
        
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
                print("  ├── system/")
                print("  ├── project/")
                print("  └── languages/")
                return False

            # Get and display local files
            local_files = self.get_local_files()
            if not local_files:
                print("No local files found to update")
                return False

            # Get user selection
            local_file = self.input_handler.get_valid_selection(
                local_files,
                "\nSelect file to update: "
            )
            if not local_file:
                return False

            # Read file contents
            external_content = self.file_manager.read_file(external_file)
            if external_content is None:
                print(f"Error reading external file: {external_file}")
                return False

            # Determine block type and extract block
            block_type = self.block_extractor.determine_block_type(local_file)
            if not block_type:
                print(f"Could not determine block type from path: {local_file}")
                return False

            # Extract block from external file
            block = self.block_extractor.extract_block(
                external_content, block_type, local_file
            )
            if block is None:
                print(f"Could not find matching block in external file")
                return False

            # Write block to local file
            if not self.file_manager.write_file(local_file, block):
                print(f"Error writing to local file: {local_file}")
                return False

            print(f"\nSuccessfully updated {os.path.basename(local_file)}")
            return True

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return False

def main() -> None:
    """Main entry point for update_local CLI."""
    parser = argparse.ArgumentParser(
        description='Update local clinerules file with content from external file'
    )
    parser.add_argument('external_file', help='Path to external clinerules file')
    args = parser.parse_args()

    cli = UpdateLocalCLI()
    if not cli.update_local_file(args.external_file):
        print("Failed to update local file")

if __name__ == '__main__':
    main()

import os
import glob
from typing import List, Optional
from src.utils.logging_config import setup_logger
from src.core.file_manager import FileManager
from src.utils.input_handler import InputHandler

logger = setup_logger(__name__)

class CreateRulesCLI:
    """CLI interface for creating clinerules files."""

    def __init__(self):
        """Initialize CreateRulesCLI with required components."""
        self.file_manager = FileManager()
        self.input_handler = InputHandler()

    def select_system_file(self) -> Optional[str]:
        """
        Select a system rules file.
        
        Returns:
            Selected system file path or None if no selection made
        """
        system_files = self.file_manager.list_files(os.path.join('system', 'clinerules*.md'))
        if not system_files:
            print("No system files found")
            return None

        self.input_handler.display_files_with_numbers(system_files, "System")
        return self.input_handler.get_valid_selection(system_files, "\nSelect system file number: ")

    def select_project_file(self) -> Optional[str]:
        """
        Select a project rules file.
        
        Returns:
            Selected project file path or None if no selection made
        """
        project_files = self.file_manager.list_files(os.path.join('project', 'clinerules*.md'))
        if not project_files:
            print("No project files found")
            return None

        self.input_handler.display_files_with_numbers(project_files, "Project")
        return self.input_handler.get_valid_selection(project_files, "\nSelect project file number: ")

    def select_language_files(self) -> List[str]:
        """
        Select multiple language rules files.
        
        Returns:
            List of selected language file paths
        """
        language_files = self.file_manager.list_files(os.path.join('languages', 'clinerules*.md'))
        if not language_files:
            print("No language files found")
            return []

        selected: List[str] = []
        while True:
            remaining_files = [f for f in language_files if f not in selected]
            if not remaining_files:
                break

            self.input_handler.display_selected_files(selected, remaining_files)
            choice = self.input_handler.get_valid_selection(
                remaining_files,
                "\nSelect a language number (press Enter to finish): ",
                allow_empty=True
            )
            
            if choice is None:
                break
            selected.append(choice)
            print(f"Added {os.path.basename(choice)}")

        return selected

    def create_rules_file(self) -> bool:
        """
        Create a new .clinerules file from selected components.
        
        Returns:
            True if file was created successfully, False otherwise
        """
        try:
            # Select system file
            system_file = self.select_system_file()
            if not system_file:
                return False

            # Select project file
            project_file = self.select_project_file()
            if not project_file:
                return False

            # Select language files
            language_files = self.select_language_files()

            # Merge all selected files
            all_files = [system_file, project_file] + language_files
            merged_content = self.file_manager.merge_files(all_files)
            
            if merged_content is None:
                return False

            # Write merged content
            if not self.file_manager.write_file('.clinerules', merged_content):
                return False

            print("\nFiles merged successfully into .clinerules")
            print("Merged files:")
            for file in all_files:
                print(f"- {os.path.basename(file)}")

            return True

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return False

def main() -> None:
    """Main entry point for create_rules CLI."""
    cli = CreateRulesCLI()
    if not cli.create_rules_file():
        logger.error("Failed to create rules file")

if __name__ == '__main__':
    main()

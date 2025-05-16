"""File selection functionality for clinerules files."""

import os
from typing import List, Optional, Tuple
from src.utils.logging_config import setup_logger
from src.utils.input_handler import InputHandler
from src.core.file_manager import FileManager
from .config import (
    GENERAL_PATTERN,
    SYSTEM_PATTERN,
    PROJECT_PATTERN,
    LANGUAGE_PATTERN,
    CLINE_PATTERN,
)

logger = setup_logger(__name__)


class FileSelector:
    """Handles selection of clinerules files."""

    def __init__(self):
        """Initialize FileSelector with required components."""
        self.file_manager = FileManager()
        self.input_handler = InputHandler()

    def get_files_by_category(self) -> Tuple[List[str], List[str], List[str], List[str]]:
        """
        Get files organized by category.

        Returns:
            Tuple of (general_files, system_files, project_files, language_files)
        """
        general_files = self.file_manager.list_files(GENERAL_PATTERN)
        system_files = self.file_manager.list_files(SYSTEM_PATTERN)
        project_files = self.file_manager.list_files(PROJECT_PATTERN)
        language_files = self.file_manager.list_files(LANGUAGE_PATTERN)
        cline_files = self.file_manager.list_files(CLINE_PATTERN)
        return general_files, system_files, project_files, language_files, cline_files

    def display_files_by_category(
        self,
        general_files: List[str],
        system_files: List[str],
        project_files: List[str],
        language_files: List[str],
        cline_files: List[str],
    ) -> None:
        """
        Display files organized by category.

        Args:
            general_files: List of general rule files
            system_files: List of system rule files
            project_files: List of project rule files
            language_files: List of language rule files
        """
        current_number = 1
        if cline_files:
            current_number = self.input_handler.display_files_with_numbers(
                cline_files, "Cline", current_number
            )
        if general_files:
            current_number = self.input_handler.display_files_with_numbers(
                general_files, "General", current_number
            )
        if system_files:
            current_number = self.input_handler.display_files_with_numbers(
                system_files, "System", current_number
            )
        if project_files:
            current_number = self.input_handler.display_files_with_numbers(
                project_files, "Project", current_number
            )
        if language_files:
            current_number = self.input_handler.display_files_with_numbers(
                language_files, "Language", current_number
            )

    def select_general_file(self) -> Optional[str]:
        """
        Select a general rules file.

        Returns:
            Selected general file path or None if no selection made
        """
        general_files = self.file_manager.list_files(GENERAL_PATTERN)
        if not general_files:
            logger.info("No general files found")
            return None

        self.input_handler.display_files_with_numbers(general_files, "General")
        return self.input_handler.get_valid_selection(
            general_files, "\nSelect general file number (press Enter to skip): ",
            allow_empty=True
        )

    def select_system_file(self) -> Optional[str]:
        """
        Select a system rules file.

        Returns:
            Selected system file path or None if no selection made
        """
        system_files = self.file_manager.list_files(SYSTEM_PATTERN)
        if not system_files:
            logger.info("No system files found")
            return None

        self.input_handler.display_files_with_numbers(system_files, "System")
        return self.input_handler.get_valid_selection(
            system_files, "\nSelect system file number (press Enter to skip): ",
            allow_empty=True
        )

    def select_project_file(self) -> Optional[str]:
        """
        Select a project rules file.

        Returns:
            Selected project file path or None if no selection made
        """
        project_files = self.file_manager.list_files(PROJECT_PATTERN)
        if not project_files:
            logger.info("No project files found")
            return None

        self.input_handler.display_files_with_numbers(project_files, "Project")
        return self.input_handler.get_valid_selection(
            project_files, "\nSelect project file number (press Enter to skip): ",
            allow_empty=True
        )

    def select_language_files(self) -> List[str]:
        """
        Select multiple language rules files.

        Returns:
            List of selected language file paths
        """
        language_files = self.file_manager.list_files(LANGUAGE_PATTERN)
        if not language_files:
            logger.info("No language files found")
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
                allow_empty=True,
            )

            if choice is None:
                break
            selected.append(choice)
            logger.info(f"Added {os.path.basename(choice)}")

        return selected

    def select_cline_file(self) -> Optional[str]:
        """
        Select a cline rules file.

        Returns:
            Selected cline file path or None if no selection made
        """
        cline_files = self.file_manager.list_files(CLINE_PATTERN)
        if not cline_files:
            logger.info("No cline files found")
            return None

        self.input_handler.display_files_with_numbers(cline_files, "Cline")
        return self.input_handler.get_valid_selection(
            cline_files, "\nSelect cline file number (press Enter to skip): ",
            allow_empty=True
        )

    def select_all_files(self) -> List[str]:
        """
        Select files from all categories.

        Returns:
            List of all selected file paths
        """
        all_files = []

        # Select files from each section
        cline_file = self.select_cline_file()
        general_file = self.select_general_file()
        system_file = self.select_system_file()
        project_file = self.select_project_file()
        language_files = self.select_language_files()

        # Collect only selected files
        if cline_file:
            all_files.append(cline_file)
        if general_file:
            all_files.append(general_file)
        if system_file:
            all_files.append(system_file)
        if project_file:
            all_files.append(project_file)
        all_files.extend(language_files)

        return all_files

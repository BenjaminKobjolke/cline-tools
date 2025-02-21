import os
from typing import List, Optional
from src.utils.logging_config import setup_logger

logger = setup_logger(__name__)


class InputHandler:
    """Handles user input operations."""

    @staticmethod
    def get_valid_selection(
        files: List[str], prompt: str, allow_empty: bool = False
    ) -> Optional[str]:
        """
        Get valid selection from user.

        Args:
            files: List of files to choose from
            prompt: Prompt message for user input
            allow_empty: Whether to allow empty input (defaults to False)

        Returns:
            Selected file path or None if empty input is allowed and provided

        Raises:
            ValueError: If input is not a valid number
        """
        while True:
            try:
                choice = input(prompt).strip()
                if allow_empty and not choice:
                    return None

                num = int(choice)
                if 1 <= num <= len(files):
                    selected = files[num - 1]
                    logger.debug(f"Selected file: {selected}")
                    return selected
                print(f"Please enter a number between 1 and {len(files)}")
            except ValueError:
                print("Please enter a valid number")

    @staticmethod
    def get_diff_tool_choice() -> bool:
        """
        Get user's choice of diff tool.

        Returns:
            True for git diff, False for VS Code diff
        """
        print("\nSelect diff tool:")
        print("1. git diff (colored inline diff)")
        print("2. VS Code (side-by-side diff)")

        while True:
            choice = input("Enter choice (1 or 2): ").strip()
            if choice == "1":
                return True
            elif choice == "2":
                return False
            print("Please enter 1 or 2")

    @staticmethod
    def display_files_with_numbers(
        files: List[str], category: str, start_num: int = 1
    ) -> int:
        """
        Display files with numbers for selection.

        Args:
            files: List of files to display
            category: Category name for the files
            start_num: Starting number for file list

        Returns:
            Next number in sequence
        """
        if files:
            print(f"\n{category} files:")
            for i, file in enumerate(files, start_num):
                print(f"{i}. {os.path.basename(file)}")
            return start_num + len(files)
        return start_num

    @staticmethod
    def display_selected_files(selected: List[str], remaining: List[str]) -> None:
        """
        Display selected and remaining files.

        Args:
            selected: List of selected files
            remaining: List of remaining files
        """
        print("\nCurrently selected files:")
        for file in selected:
            print(f"- {os.path.basename(file)}")

        if remaining:
            print("\nRemaining files:")
            for i, file in enumerate(remaining, 1):
                print(f"{i}. {os.path.basename(file)}")
        else:
            print("\nAll files have been selected.")

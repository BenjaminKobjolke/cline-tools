"""CLI interface for updating local clinerules files with external content."""

import argparse
from src.utils.logging_config import setup_logger
from src.core.update.update_handler import UpdateHandler
from src.core.update.block_updater import BlockUpdater

logger = setup_logger(__name__)


class UpdateLocalCLI:
    """CLI interface for updating local clinerules files with external content."""

    def __init__(self):
        """Initialize UpdateLocalCLI with required components."""
        self.update_handler = UpdateHandler()
        self.block_updater = BlockUpdater()

    def update_local_file(self, external_file: str) -> bool:
        """
        Update a local file with content from external file.

        Args:
            external_file: Path to external clinerules file

        Returns:
            True if update was successful, False otherwise
        """
        try:
            # Validate files
            if not self.update_handler.validate_files(external_file):
                return False

            # Select local file to update
            local_file = self.update_handler.select_local_file()
            if not local_file:
                return False

            # Update local file with external content
            return self.block_updater.update_local_with_external(external_file, local_file)

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return False


def main() -> None:
    """Main entry point for update_local CLI."""
    parser = argparse.ArgumentParser(
        description="Update local clinerules file with content from external file"
    )
    parser.add_argument("external_file", help="Path to external clinerules file")
    args = parser.parse_args()

    cli = UpdateLocalCLI()
    if not cli.update_local_file(args.external_file):
        print("Failed to update local file")


if __name__ == "__main__":
    main()

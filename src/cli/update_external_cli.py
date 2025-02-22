"""CLI interface for updating external clinerules files with local content."""

import argparse
from src.utils.logging_config import setup_logger
from src.core.update.update_handler import UpdateHandler
from src.core.update.block_updater import BlockUpdater

logger = setup_logger(__name__)


class UpdateExternalCLI:
    """CLI interface for updating external clinerules files with local content."""

    def __init__(self):
        """Initialize UpdateExternalCLI with required components."""
        self.update_handler = UpdateHandler()
        self.block_updater = BlockUpdater()

    def update_external_file(self, external_file: str) -> bool:
        """
        Update external file with content from local file.

        Args:
            external_file: Path to external clinerules file

        Returns:
            True if update was successful, False otherwise
        """
        try:
            # Validate files
            if not self.update_handler.validate_files(external_file):
                return False

            # Select local file to use
            local_file = self.update_handler.select_local_file()
            if not local_file:
                return False

            # Update external file with local content
            return self.block_updater.update_external_with_local(external_file, local_file)

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

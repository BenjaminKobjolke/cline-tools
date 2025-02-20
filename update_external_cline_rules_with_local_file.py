#!/usr/bin/env python3
"""
Entry point script for updating external clinerules files with content from local file.
This script provides a command-line interface for selecting a local file and updating
the corresponding block in an external clinerules file.
"""

from src.cli.update_external_cli import main

if __name__ == '__main__':
    main()

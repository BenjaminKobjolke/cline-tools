#!/usr/bin/env python3
"""
Entry point script for updating local clinerules files with content from external file.
This script provides a command-line interface for selecting a local file and updating it
with the corresponding block from an external clinerules file.
"""

from src.cli.update_local_cli import main

if __name__ == '__main__':
    main()

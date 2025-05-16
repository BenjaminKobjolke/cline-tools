"""Configuration for clinerules file management."""

import os
from typing import Dict, List

# Directory paths
CLINERULES_DIR = os.path.join(os.getcwd(), "clinerules")
OUTPUT_DIR = os.path.join(os.getcwd(), "output")

# File patterns
GENERAL_PATTERN = os.path.join(CLINERULES_DIR, "general", "clinerules*.md")
SYSTEM_PATTERN = os.path.join(CLINERULES_DIR, "system", "clinerules*.md")
PROJECT_PATTERN = os.path.join(CLINERULES_DIR, "project", "clinerules*.md")
LANGUAGE_PATTERN = os.path.join(CLINERULES_DIR, "languages", "clinerules*.md")
CLINE_PATTERN = os.path.join(CLINERULES_DIR, "cline", "clinerules*.md")

# Output file
OUTPUT_FILE = os.path.join(OUTPUT_DIR, ".clinerules")

# Directory structure for validation
DIRECTORY_STRUCTURE: Dict[str, List[str]] = {
    "clinerules": [
        "general",
        "system",
        "project",
        "languages",
        "cline",
    ]
}

# File categories
CATEGORIES = {
    "general": "General rules that apply to all projects",
    "system": "System-specific rule files",
    "project": "Project-specific rule files",
    "languages": "Language-specific rule files",
    "cline": "Cline-specific rule files",
}

# Cline Tools

This repository contains rule files and tools for use with the [Cline VS Code plugin](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev), an extension that enables direct interaction with AI assistants within Visual Studio Code. For more information about Cline, visit the [official GitHub repository](https://github.com/cline/cline).

## Available Rule Files

The repository currently includes the following rule files:

- `.clinerules_autohotkey_v1` - Comprehensive rules for AutoHotkey v1 development, including proper object access syntax, variable usage in commands, string concatenation guidelines, and window command best practices.
- `.clinerules_flutter` - Detailed Flutter development guidelines covering project structure, coding conventions, state management, environment configuration, and best practices for logging and error handling.
- `.clinerules_python` - Python development rules focusing on virtual environment setup, coding standards (PEP 8), project structure, dependency management, and logging best practices.

## Purpose

These rule files enhance Cline's capabilities by providing comprehensive language-specific context and guidelines. Each rule file contains detailed instructions about:

- Project structure and organization
- Language-specific syntax and conventions
- Best practices for error handling and logging
- Environment setup and dependency management
- Automation scripts and development workflows

When used with the Cline VS Code plugin, these rules help AI assistants better understand your codebase and provide more accurate, contextually relevant assistance for different programming languages and frameworks.

## Directory Structure

The repository uses the following structure for organizing rule files:

```
clinerules/
  ├── general/     - General rules that apply to all projects
  ├── system/      - System-specific rule files
  ├── project/     - Project-specific rule files
  └── languages/   - Language-specific rule files

output/
  └── .clinerules  - Generated rules file
```

## Available Tools

The repository includes several Python tools for managing clinerules files:

1. **Create Rules** (`create_rules.py`):

   - Combines selected general, system, project, and language rules into a single rules file
   - Interactive selection of components to include (any section can be skipped)
   - Creates output/.clinerules file
   - Requires at least one section to be selected

2. **Compare Rules** (`compare_rules.py`):

   - Compares blocks between local and external clinerules files
   - Supports both git diff and VS Code diff views

3. **Update Local Rules** (`update_local_cline_rules_with_external_file.py`):

   - Updates a selected local rule file with content from an external .clinerules file
   - Extracts matching block based on file type and name

4. **Update External Rules** (`update_external_cline_rules_with_local_file.py`):
   - Updates a block in an external .clinerules file with content from a local rule file
   - Preserves other blocks in the external file

## Usage

1. Clone this repository
2. Run `install.bat` to set up the Python environment and dependencies
3. Run `run.bat` to access the tools menu
4. Select the desired operation:
   - Create a new rules file (outputs to output/.clinerules)
   - Compare local and external rules
   - Update local rules from external file
   - Update external file from local rules
5. For use with Cline VS Code plugin:
   - Copy output/.clinerules to your project

## Contributing

Feel free to contribute additional rule files or improvements to existing ones by submitting a pull request.

## License

This project is open source and available under the MIT License.

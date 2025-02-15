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

## Usage

1. Clone this repository
2. Copy the desired rule file to your project directory
3. Rename the rule file to `.clinerules` (e.g., rename `.clinerules_python` to `.clinerules` in your Python project)
4. The Cline VS Code plugin will automatically detect and use these rules when providing assistance for your project

## Contributing

Feel free to contribute additional rule files or improvements to existing ones by submitting a pull request.

## License

This project is open source and available under the MIT License.

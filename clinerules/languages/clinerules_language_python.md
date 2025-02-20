### BEGIN LANGUAGE PYTHON

# Coding Standards

- You split large code blocks into managble files and classes.
- Group related classes/functions into separate files under modules.
- Follow PEP 8 style guidelines
- Use docstrings and type hints
- Auto-format code with black
- Use flake8 for linting
- Modular Design

# Virtual Environments

- Create venv for dependency isolation. But only if the directory doesnt exist yet.
- Maintain requirements.txt. Update it after adding new libraries (e.g., pip freeze > requirements.txt). 
- Use latest stable versions of packages

# Logging Best Practices

- Use Python's logging module
- Avoid print statements
- Handle exceptions with proper error messages
- Use appropriate log levels (INFO, WARNING, ERROR)

# Entry Points

- Use main.py for argument parsing and flow
- Use if **name** == "**main**" pattern
- Import modules as needed

# Dependencies

- Maintain requirements.txt file
- Update after adding new libraries (pip freeze > requirements.txt)
- Use latest stable versions for new features and fixes

# Error Handling

- Always use logging class, not print statements
- Handle errors gracefully with clear messages or fallback procedures
- Implement fallback procedures when needed

# Configuration

- Store settings in settings.ini at the project root. Parse these using Python’s configparser.

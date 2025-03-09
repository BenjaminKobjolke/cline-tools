@echo off
REM Format code with black
echo.
echo Formatting code with black...
black src create_rules.py compare_rules.py

REM Run flake8
echo.
echo Running flake8 linter...
flake8 src create_rules.py compare_rules.py

pause
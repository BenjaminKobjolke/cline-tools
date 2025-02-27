@echo off
echo Creating virtual environment...

call python -m venv venv

echo Installing dependencies...
REM Activate virtual environment
call %~dp0\venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Format code with black
echo.
echo Formatting code with black...
black src create_rules.py compare_rules.py

REM Run flake8
echo.
echo Running flake8 linter...
flake8 src create_rules.py compare_rules.py

echo.
echo Installation complete.
echo You can now use 'run.bat' to execute the tools.

REM Deactivate virtual environment
deactivate

pause

@echo off
echo Cline Tools Runner
echo.
echo 1. Create Rules (create_rules.py)
echo 2. Compare Rules (compare_rules.py)
echo.

REM Activate virtual environment
call %~dp0\venv\Scripts\activate.bat

set /p choice="Enter your choice (1 or 2): "

if "%choice%"=="1" (
    python create_rules.py
) else if "%choice%"=="2" (
    set /p external_file="Enter path to external clinerules file: "
    python compare_rules.py "%external_file%"
) else (
    echo Invalid choice. Please enter 1 or 2.
)

REM Deactivate virtual environment
deactivate

pause

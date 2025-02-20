@echo off
echo Cline Tools Runner
echo.
echo 1. Create Rules (create_rules.py)
echo 2. Compare Rules (compare_rules.py)
echo 3. Update Local File from External (update_local_cline_rules_with_external_file.py)
echo 4. Update External File from Local (update_external_cline_rules_with_local_file.py)
echo.

REM Activate virtual environment
call %~dp0\venv\Scripts\activate.bat

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    python create_rules.py
) else if "%choice%"=="2" (
    set /p external_file="Enter path to external clinerules file: "
    python compare_rules.py "%external_file%"
) else if "%choice%"=="3" (
    set /p external_file="Enter path to external clinerules file: "
    python update_local_cline_rules_with_external_file.py "%external_file%"
) else if "%choice%"=="4" (
    set /p external_file="Enter path to external clinerules file: "
    python update_external_cline_rules_with_local_file.py "%external_file%"
) else (
    echo Invalid choice. Please enter a number between 1 and 4.
)

REM Deactivate virtual environment
deactivate

pause

### BEGIN SYSTEM

# System Environment

OS: Windows
Shell: Windows PowerShell

# Shell Limitations

## PowerShell does not support && to combine commands

For example this will not work:
python -m venv venv && .venv\Scripts\activate

Therefore execute commands separately.
For example create the directories one by one.

## How to delete files and folders

"del" command does not work in powershell.
use "Remove-Item"

## How to create multiple folders

Example: mkdir src\core\rules; mkdir src\core\compare


# Helper Scripts

Provide .bat files for automation:
install.bat:
@echo off
echo Installing dependencies...
pause

run.bat:
@echo off
echo Running application...
pause

activate_environment.bat (for python)
@echo off
%~dp0\venv\Scripts\activate.bat

Use windows "call" before executing applications in the bat files.
Like "call python" or "call pip"

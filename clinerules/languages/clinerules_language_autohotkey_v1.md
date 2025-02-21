### BEGIN LANGUAGE AUTOHOTKEY

# Object Access

- Use bracket notation for object properties, not dot notation
- CORRECT: obj["property"]
- WRONG: obj.property

# Object Creation

- Use Object() to create new objects, not {}
- CORRECT: myObj := Object()
- WRONG: myObj := {}

# Arrays

- Use [] for arrays (this is supported)
- CORRECT: myArray := []

# Variables in Commands

- When using variables in AutoHotkey commands, wrap them in %%
- Don't use % for expressions
- CORRECT: WinGet, WindowId,, ahk_exe %targetExe%
- WRONG: WinGet, WindowId,, % targetExe

# String Concatenation

- For commands that need concatenated strings, store in variable first
- CORRECT:
  targetExe := processName ".exe"
  WinGet, WindowId,, ahk_exe %targetExe%

# Window Commands

- WinExist and similar commands don't use % for variables
- CORRECT: if WinExist(targetTitle)
- WRONG: if WinExist(%targetTitle%)

# Error Prevention

- Don't use % in WinExist/WinActivate parameters
- Always store concatenated strings in variables before using in commands
- Use bracket notation for all object property access
- Remember to use %% for variables in command parameters

# GUI Commands

- When using named GUIs, be consistent with the name prefix
- CORRECT:
  ```autohotkey
  Gui, main:Add, Text, h100 w100, Text
  Gui, main:Show, w200 h100
  ```
- WRONG (inconsistent naming):
  ```autohotkey
  Gui, main:Add, Text, h100 w100, Text
  Gui, Show, w200 h100  ; missing main: prefix
  ```
- For temporary GUIs (like alerts), use no prefix consistently
- Options like h100, w200 should not have spaces between letter and number

# Function Definitions

- Opening brace goes on a new line
- CORRECT:
  ```autohotkey
  MyFunction()
  {
      code here
  }
  ```
- WRONG:
  ```autohotkey
  MyFunction() {
      code here
  }
  ```

# Include Files

- Include order matters - files with dependencies must be included after their dependencies
- Global variables should be included first
- Function definitions should be included before they're used
- Hotkey definitions should be included last
- CORRECT order:
  ```autohotkey
  #Include global.ahk
  #Include functions.ahk
  #Include gui.ahk
  #Include hotkeys.ahk
  ```

# Code Organization

- Split large files into logical modules
- Keep related functionality together
- Use descriptive file names that indicate purpose
- Common splits:
  - global.ahk: Global variables
  - gui.ahk: GUI related functions
  - hotkeys.ahk: Hotkey definitions
  - config.ahk: Configuration handling
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

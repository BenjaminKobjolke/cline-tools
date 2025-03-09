### BEGIN LANGUAGE ARDUINO C

# **Coding Standards**

- Split large code blocks into manageable `.h` and `.cpp` files.
- Group related functions into classes or libraries.
- Follow the **Arduino Style Guide** for naming conventions and formatting.
- Use `const` and `constexpr` for immutable values.
- Prefer `enum` instead of plain integers for states or modes.
- Use meaningful variable names and avoid magic numbers.

# **Code Structure**

- Create separate `.h` files for function declarations and `.cpp` files for definitions.
- Place global constants and macros in a dedicated `config.h` file.
- Avoid long `loop()` and `setup()` functions. Split logic into helper functions.
- Use namespaces or class encapsulation for complex projects.

# **Memory Management**

- Prefer stack allocation whenever possible.
- Avoid dynamic memory allocation (`malloc`/`new`) unless absolutely necessary.
- Use `PROGMEM` for large constant data to save SRAM.
- Monitor free memory using `freeMemory()` during debugging.

# **Error Handling**

- Always check the return value of critical functions (e.g., `Serial.begin()`).
- Implement fail-safe procedures in case of errors.
- Use watchdog timers to reset the system in case of deadlocks.

# **Logging & Debugging**

- Use `Serial.println()` for debugging, but disable it for production.
- Implement conditional debug macros (e.g., `#define DEBUG 1`) to toggle logs.
- Ensure `Serial.begin()` matches the baud rate of the serial monitor.

# **Hardware Interaction**

- Debounce buttons using software or hardware methods.
- Avoid blocking code with `delay()`. Use `millis()` for non-blocking timing.
- Always initialize sensors, displays, and other peripherals in `setup()`.

# **Power Efficiency**

- Use sleep modes (`LowPower.h`) for battery-powered projects.
- Disable unused peripherals (e.g., `ADC`, `I2C`) to save power.
- Reduce clock speed if high performance is not required.

# **Libraries & Dependencies**

- Prefer official Arduino libraries or well-maintained open-source ones.
- Avoid redundant libraries; check compatibility with your board.
- Keep libraries updated but ensure compatibility with existing code.

# **Safety & Reliability**

- Implement watchdog timers to recover from unexpected crashes.
- Check array bounds and avoid buffer overflows.
- Use CRC or checksums when communicating over unreliable channels.

# **Configuration**

- Store user-defined settings in EEPROM, SPIFFS, or SD card.
- Use `#define` or `const` for compile-time settings.
- Provide clear documentation for configurable parameters.

# **Documentation & Style**

- Use Doxygen-style comments for functions and classes.
- Document pin connections and module configurations in code comments.
- Maintain a `README.md` file for project structure and setup instructions.
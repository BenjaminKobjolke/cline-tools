### BEGIN LANGUAGE PHP

# Coding Standards

- Split large code blocks into manageable files and classes.
- Group related classes/functions into separate files under namespaces.
- Follow PSR-12 coding standards.
- Use PHPDoc for documentation and type hints.
- Auto-format code with PHP-CS-Fixer.
- Use PHPStan or Psalm for static analysis.
- Modular Design.
- Never use plain associative arrays for structured data between functions and classes. Create a class or DTO (Data Transfer Object) for that.

# Virtual Environments

- Use Composer for dependency management.
- Ensure `vendor` directory exists before running `composer install`.
- Maintain `composer.json` and `composer.lock`. Update dependencies with `composer update`.
- Use the latest stable versions of packages.

# Logging Best Practices

- Use Monolog for logging.
- Avoid `echo` or `var_dump` for debugging in production.
- Handle exceptions with meaningful error messages.
- Use appropriate log levels (INFO, WARNING, ERROR).

# Entry Points

- Use `index.php` or `bootstrap.php` for application initialization.
- Use front controllers for handling requests in web applications.
- Autoload classes using Composer (`composer dump-autoload`).

# Dependencies

- Maintain `composer.json` and `composer.lock` files.
- Update dependencies regularly (`composer update`).
- Use the latest stable versions to leverage new features and security fixes.

# Error Handling

- Use a centralized error handler.
- Log errors using Monolog instead of displaying them.
- Handle exceptions gracefully with clear messages or fallback mechanisms.
- Implement fallback procedures when necessary.

# Configuration

- Store settings in `.env` files and use `vlucas/phpdotenv` for parsing.
- Do not hardcode configuration values in the codebase.
- Use environment variables for sensitive data like API keys and database credentials.

### END LANGUAGE PHP
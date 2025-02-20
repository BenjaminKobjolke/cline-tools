### BEGIN LANGUAGE FLUTTER

# Coding Standards

- Follow Flutter's Dart Style Guide
- Format code using dart format
- Use doc comments (///) for documentation
- Follow SOLID principles

# Project Organization

- Group related widgets into separate files
- Keep business logic separate from UI
- Use proper state management (Provider, Riverpod, or Bloc)

Example structure:
lib/
main.dart
screens/
widgets/
services/

# Dependencies

- Use pubspec.yaml to manage dependencies
- Run flutter pub get after adding dependencies
- Prefer latest stable versions

# Environment Setup

- Store settings in lib/config.dart or .env files
- Parse .env files using flutter_dotenv
- Keep sensitive data out of version control

# Development & Execution

- Use flutter run for debug mode
- Specify platform with -d flag
- Use Flutter's built-in environment

# Logging & Error Handling

- Use dart:developer or logger package instead of print()
- Implement try-catch for critical operations
- Display user-friendly error messages
- Log errors with proper context

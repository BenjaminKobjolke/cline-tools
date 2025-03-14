### BEGIN LANGUAGE RUST

# Coding Standards

- Split large codebases into manageable modules and crates.
- Organize related functionality into separate modules.
- Follow Rust’s official style guide (rustfmt).
- Use clear, descriptive function and variable names.
- Write doc comments (`///`) for public functions, structs, and modules.
- Prefer `struct`s and `enum`s over generic tuples for passing structured data.
- Avoid unnecessary `unsafe` code unless required for performance or FFI.
- Always use `clippy` to lint code and enforce best practices.

# Dependency Management

- Use `cargo` for dependency management.
- Keep `Cargo.toml` updated with only necessary dependencies.
- Run `cargo update` periodically to fetch the latest stable versions.
- Use `cargo audit` to check for security vulnerabilities.

# Logging Best Practices

- Use the `log` crate for logging.
- Avoid `println!` for debugging; use logging macros (`info!`, `warn!`, `error!`).
- Ensure log levels are appropriate for debugging vs. production use.

# Error Handling

- Use `Result<T, E>` for recoverable errors.
- Use `?` operator for propagating errors when appropriate.
- Use `panic!` only for unrecoverable conditions.
- Prefer `thiserror` or `anyhow` crates for error handling.

# Entry Points

- Use `main.rs` or `lib.rs` as the root of the application.
- Keep `main.rs` minimal, delegating logic to other modules.
- Structure command-line applications using `clap` or similar crates.

# Configuration

- Use `.env` files for secrets and environment variables (`dotenv` crate).
- Store structured configurations in `config.toml` and parse with `serde`.
- Avoid hardcoding values; use constants or configuration files.

# Performance & Safety

- Use `cargo bench` for performance benchmarking.
- Avoid unnecessary memory allocations; prefer `&str` over `String` where applicable.
- Optimize hot code paths with `#[inline(always)]` where needed.
- Use idiomatic Rust (avoid manual memory management unless required).

# Build & Formatting

- Use `cargo fmt` to maintain consistent code formatting.
- Use `cargo clippy` to enforce best practices.
- Automate builds and tests with `cargo check` and `cargo test`.

import logging
import sys
from typing import Optional


def setup_logger(name: str, level: Optional[int] = logging.INFO) -> logging.Logger:
    """
    Set up a logger with consistent formatting and handling.

    Args:
        name: The name of the logger
        level: The logging level (defaults to INFO)

    Returns:
        A configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler if none exists
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

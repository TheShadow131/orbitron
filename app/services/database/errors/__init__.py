"""
Database errors package.

This package contains custom exception classes related to database service.
These exceptions are used to handle various error scenarios.
"""

from .base import DBServiceError
from .connection import (
    DBConnectionAlreadyExistsError,
    DBConnectionError,
    DBConnectionNotFoundError,
    DBConnectionUnhealthyError,
)

__all__ = [
    "DBServiceError",
    "DBConnectionError",
    "DBConnectionAlreadyExistsError",
    "DBConnectionNotFoundError",
    "DBConnectionUnhealthyError",
]

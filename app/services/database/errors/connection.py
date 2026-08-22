"""
Database connection error module.

This module defines custom exceptions related to database connection errors.
These exceptions are used to handle various error scenarios that may occur
when working with database connections in the application.
"""

from .base import DBServiceError


class DBConnectionError(DBServiceError):
    """Exception raised for database connection errors."""


class DBConnectionAlreadyExistsError(DBServiceError):
    """Exception raised when trying to create a connection that already exists."""


class DBConnectionNotFoundError(DBServiceError):
    """Exception raised when trying to access a connection that does not exist."""


class DBConnectionUnhealthyError(DBServiceError):
    """Exception raised when a database connection health check fails."""

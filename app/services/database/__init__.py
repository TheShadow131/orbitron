"""
Database service package.

This package provides a database service to interact with various database connections.
It includes the `DatabaseService` class, which manages database connections and
operations, as well as custom exception classes for handling database-related errors.
"""

from .errors import DBServiceError
from .main import DatabaseService
from .models import BaseModel

__all__ = ["DatabaseService", "DBServiceError", "BaseModel"]

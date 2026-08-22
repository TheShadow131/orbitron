"""
Database service module.

This module provides the `DatabaseService` class, which manages database connections and
operations. It allows you to create, set up, check, and delete database connections, as
well as perform health checks and execute queries using asynchronous sessions.
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from logging import getLogger

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from .errors import (
    DBConnectionAlreadyExistsError,
    DBConnectionNotFoundError,
    DBConnectionUnhealthyError,
)
from .models import BaseModel


class DatabaseService:
    """
    Database service class for managing database operations.

    This class provides methods to create, set up, check, and delete database
    connections, as well as perform health checks and execute queries using
    asynchronous sessions. It maintains a dictionary of connections, where
    each connection is represented by its name.
    """

    _instance = None

    # Internal methods:
    def __new__(cls) -> "DatabaseService":
        """
        Create a singleton instance of the DatabaseService class.

        :return: The singleton instance of the DatabaseService class.
        :rtype: DatabaseService
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        """Initialize the database service."""
        if hasattr(self, "_connections"):
            return

        self._logger = getLogger(__package__)
        self._connections: dict[str, dict] = {}

    # Private methods:

    # Public methods:
    def create_connection(self, name: str, connection_url: str) -> None:
        """
        Create a new database connection.

        :param name: The name of the connection.
        :type name: str
        :raises DBConnectionAlreadyExistsError: If the connection already exists.
        """
        if self.check_connection(name):
            raise DBConnectionAlreadyExistsError(f"Connection '{name}' already exists.")

        _engine = create_async_engine(connection_url, echo=False)
        _sessionmaker = async_sessionmaker(_engine, expire_on_commit=False)

        self._connections[name] = {
            "engine": _engine,
            "sessionmaker": _sessionmaker,
        }
        self._logger.debug(f"Created connection '{name}'.")

    async def setup_connection(self, name: str) -> None:
        """
        Set up a database connection.

        :param name: The name of the connection.
        :type name: str
        :raises DBConnectionNotFoundError: If the connection does not exist.
        :raises DBConnectionUnhealthyError: If the setup fails due to a database error.
        """
        if not self.check_connection(name):
            raise DBConnectionNotFoundError(f"Connection '{name}' does not exist.")

        async with self._connections[name]["engine"].begin() as connection:
            try:
                await connection.run_sync(BaseModel.metadata.create_all)
                self._logger.info(f"Setup completed for connection '{name}'.")

            except SQLAlchemyError as error:
                self._logger.error(f"Setup failed for connection '{name}': {error}")
                raise DBConnectionUnhealthyError(
                    f"Setup failed for connection '{name}': {error}"
                ) from error

    def check_connection(self, name: str) -> bool:
        """
        Check if a database connection exists.

        :param name: The name of the connection.
        :type name: str
        :return: True if the connection exists, False otherwise.
        :rtype: bool
        """
        return name in self._connections

    async def check_connection_health(self, name: str) -> bool:
        """
        Check the health of a database connection.

        :param name: The name of the connection.
        :type name: str
        :return: True if the connection is healthy, False otherwise.
        :rtype: bool
        :raises DBConnectionNotFoundError: If the connection does not exist.
        """
        if not self.check_connection(name):
            raise DBConnectionNotFoundError(f"Connection '{name}' does not exist.")

        async with self.get_session(name) as session:
            try:
                result = await session.execute(text("SELECT 1"))
                return result.scalar() == 1

            except SQLAlchemyError as error:
                self._logger.error(
                    f"Health check failed for connection '{name}': {error}"
                )
                return False

    async def delete_connection(self, name: str) -> None:
        """
        Delete an existing database connection.

        :param name: The name of the connection.
        :type name: str
        :raises DBConnectionNotFoundError: If the connection does not exist.
        """
        if not self.check_connection(name):
            raise DBConnectionNotFoundError(f"Connection '{name}' does not exist.")

        _engine = self._connections[name]["engine"]
        await _engine.dispose()

        del self._connections[name]
        self._logger.debug(f"Deleted connection '{name}'.")

    async def delete_all_connections(self) -> None:
        """Delete all existing database connections."""
        for name in list(self._connections.keys()):
            await self.delete_connection(name)

    @asynccontextmanager
    async def get_session(self, name: str) -> AsyncGenerator[AsyncSession]:
        """
        Get a database session for executing queries.

        :param name: The name of the connection.
        :type name: str
        :return: An asynchronous context manager that yields a database session.
        :rtype: AsyncSession
        :raises DBConnectionNotFoundError: If the connection does not exist.
        """
        if not self.check_connection(name):
            raise DBConnectionNotFoundError(f"Connection '{name}' does not exist.")

        _sessionmaker = self._connections[name]["sessionmaker"]
        async with _sessionmaker() as session:
            yield session

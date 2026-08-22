"""
Database base model module.

This module defines the `BaseModel` class, which serves as the base class for all
database models in the application.
"""

from datetime import datetime

from sqlalchemy import BigInteger, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """
    Database base model for all database models.

    This class provides common attributes and functionality for all database models,
    including an auto-incrementing primary key, created_at and updated_at timestamps,
    and automatic handling of these timestamps during database operations.
    """

    # Attributes:
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

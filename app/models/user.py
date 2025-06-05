"""User model definition.

This module defines the User model for the database.
"""

from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """User model for database storage.

    Attributes:
        id: Primary key
        email: User's email address (unique)
        hashed_password: Hashed password
        is_active: Whether the user is active
        is_superuser: Whether the user is a superuser
        created_at: Timestamp of user creation
        updated_at: Timestamp of last update
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

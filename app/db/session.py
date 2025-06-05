"""Database session configuration.

This module sets up the SQLModel database session and engine.
"""

from typing import Generator
from sqlmodel import Session, SQLModel, create_engine
from app.core.config import get_settings

settings = get_settings()

# Create database URL - using system user credentials
DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}/{settings.POSTGRES_DB}"

# Create engine with echo for debugging
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables() -> None:
    """Create database tables based on SQLModel metadata.

    This function should be called when the application starts.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get database session.

    Yields:
        Session: Database session.
    """
    with Session(engine) as session:
        yield session

"""Authentication router.

This module contains the authentication endpoints.
"""

from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from app.api.dependencies import authenticate_user, get_current_active_user
from app.core.config import get_settings
from app.core.security import create_access_token, get_password_hash
from app.db.session import get_session
from app.models.user import User
from app.schemas.user import User as UserSchema
from app.schemas.user import UserCreate

router = APIRouter()
settings = get_settings()


@router.post("/login", response_model=dict)
async def login(
    db: Session = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """Login endpoint.

    Args:
        db: Database session
        form_data: OAuth2 password request form

    Returns:
        dict: Access token and token type

    Raises:
        HTTPException: If authentication fails
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=user.id, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=UserSchema)
async def register(
    *,
    db: Session = Depends(get_session),
    user_in: UserCreate,
) -> Any:
    """Register new user.

    Args:
        db: Database session
        user_in: User creation data

    Returns:
        User: Created user

    Raises:
        HTTPException: If user with email already exists
    """
    user = db.exec(select(User).where(User.email == user_in.email)).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/me", response_model=UserSchema)
async def read_users_me(
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """Get current user.

    Args:
        current_user: Current active user

    Returns:
        User: Current user
    """
    return current_user

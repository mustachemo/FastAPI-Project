"""Main FastAPI application module.

This module initializes the FastAPI application and includes all routers and middleware.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import auth, ml_model
from app.core.config import get_settings
from app.db.session import create_db_and_tables

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A production-ready FastAPI application for serving machine learning models",
    version=settings.VERSION,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])

app.include_router(ml_model.router, prefix=f"{settings.API_V1_STR}/ml", tags=["ml"])


@app.on_event("startup")
async def on_startup():
    """Initialize database on startup."""
    create_db_and_tables()


@app.get("/")
async def root():
    """Root endpoint that returns a welcome message.

    Returns:
        dict: A welcome message and API information.
    """
    return {
        "message": "Welcome to FastAPI ML Service",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring.

    Returns:
        dict: Health status of the application.
    """
    return {"status": "healthy"}

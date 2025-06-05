"""Main FastAPI application module.

This module initializes the FastAPI application and includes all routers and middleware.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI ML Service",
    description="A production-ready FastAPI application for serving machine learning models",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

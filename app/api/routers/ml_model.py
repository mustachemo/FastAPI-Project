"""ML model router.

This module contains the ML model endpoints for predictions and model management.
"""

from typing import Any
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlmodel import Session

from app.api.dependencies import get_current_active_user
from app.db.session import get_session
from app.models.user import User
from app.schemas.ml import (
    BatchPredictionRequest,
    BatchPredictionResponse,
    ModelInput,
    ModelOutput,
    ModelStatus,
)
from app.services.ml_service import ml_service

router = APIRouter()


@router.post("/predict", response_model=ModelOutput)
async def predict(
    *,
    input_data: ModelInput,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """Make a prediction using the ML model.

    Args:
        input_data: Model input data
        current_user: Current authenticated user

    Returns:
        ModelOutput: Model prediction
    """
    return ml_service.predict(input_data)


@router.post("/batch-predict", response_model=BatchPredictionResponse)
async def batch_predict(
    *,
    request: BatchPredictionRequest,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """Make batch predictions using the ML model.

    Args:
        request: Batch prediction request
        db: Database session
        current_user: Current authenticated user

    Returns:
        BatchPredictionResponse: Batch predictions and processing time
    """
    return ml_service.batch_predict(request, db)


@router.get("/status", response_model=ModelStatus)
async def get_model_status(
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """Get current model status.

    Args:
        current_user: Current authenticated user

    Returns:
        ModelStatus: Current model status and metrics
    """
    return ml_service.get_status()


@router.post("/update")
async def update_model(
    *,
    model_file: UploadFile = File(...),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """Update the ML model with a new version.

    Args:
        model_file: New model file
        current_user: Current authenticated user

    Returns:
        dict: Update status

    Raises:
        HTTPException: If user is not a superuser or update fails
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="Not enough permissions to update the model"
        )

    # Save the uploaded file temporarily
    try:
        contents = await model_file.read()
        temp_path = f"temp_{model_file.filename}"
        with open(temp_path, "wb") as f:
            f.write(contents)

        # Update the model
        ml_service.update_model(temp_path)

        return {"status": "success", "message": "Model updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update model: {str(e)}")

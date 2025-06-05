"""ML model schemas.

This module defines Pydantic models for ML model input/output.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class ModelInput(BaseModel):
    """Base schema for model input.

    Attributes:
        data: Input data for the model
        parameters: Optional parameters for model inference
    """

    data: Dict[str, Any] = Field(..., description="Input data for the model")
    parameters: Optional[Dict[str, Any]] = Field(
        default=None, description="Optional parameters for model inference"
    )


class ModelOutput(BaseModel):
    """Base schema for model output.

    Attributes:
        prediction: Model prediction
        confidence: Optional confidence score
        metadata: Optional metadata about the prediction
    """

    prediction: Any = Field(..., description="Model prediction")
    confidence: Optional[float] = Field(
        default=None, description="Confidence score of the prediction", ge=0.0, le=1.0
    )
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional metadata about the prediction"
    )


class ModelStatus(BaseModel):
    """Schema for model status.

    Attributes:
        model_name: Name of the model
        version: Model version
        status: Current status of the model
        last_updated: Timestamp of last update
        metrics: Optional performance metrics
    """

    model_name: str = Field(..., description="Name of the model")
    version: str = Field(..., description="Model version")
    status: str = Field(..., description="Current status of the model")
    last_updated: str = Field(..., description="Timestamp of last update")
    metrics: Optional[Dict[str, float]] = Field(
        default=None, description="Optional performance metrics"
    )


class BatchPredictionRequest(BaseModel):
    """Schema for batch prediction request.

    Attributes:
        inputs: List of model inputs
        batch_size: Optional batch size for processing
    """

    inputs: List[ModelInput] = Field(..., description="List of model inputs")
    batch_size: Optional[int] = Field(
        default=None, description="Optional batch size for processing", gt=0
    )


class BatchPredictionResponse(BaseModel):
    """Schema for batch prediction response.

    Attributes:
        predictions: List of model outputs
        processing_time: Total processing time in seconds
    """

    predictions: List[ModelOutput] = Field(..., description="List of model outputs")
    processing_time: float = Field(..., description="Total processing time in seconds")

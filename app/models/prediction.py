"""Prediction model for storing ML model predictions.

This module defines the database model for storing prediction results.
"""

from datetime import datetime
from typing import Any, Dict, Optional
from sqlmodel import Field, SQLModel


class Prediction(SQLModel, table=True):
    """Model for storing ML model predictions.

    Attributes:
        id: Primary key
        input_data: Input data used for prediction
        output_data: Model prediction output
        model_version: Version of the model used
        created_at: Timestamp of prediction
        processing_time: Time taken for prediction in seconds
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    input_data: Dict[str, Any] = Field(
        ..., description="Input data used for prediction"
    )
    output_data: Dict[str, Any] = Field(..., description="Model prediction output")
    model_version: str = Field(..., description="Version of the model used")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    processing_time: Optional[float] = Field(
        default=None, description="Time taken for prediction in seconds"
    )

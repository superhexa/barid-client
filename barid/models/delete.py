from pydantic import BaseModel, Field, model_validator
from typing import Optional, Union

class DeleteSuccess(BaseModel):
    message: str
    deleted_count: Optional[int] = Field(default=None, ge=0)

class DeleteError(BaseModel):
    name: str
    message: str

class DeleteResult(BaseModel):
    success: bool
    result: Optional[DeleteSuccess] = None
    error: Optional[DeleteError] = None

    @model_validator(mode='before')
    def validate_fields(cls, values):
        if values.get("success") is True and not values.get("result"):
            raise ValueError("Success response must have 'result'")
        if values.get("success") is False and not values.get("error"):
            raise ValueError("Error response must have 'error'")
        return values

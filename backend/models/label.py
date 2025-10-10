from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Label(Document):
    """Label document model for MongoDB."""
    name: str = Field(..., min_length=1, max_length=50)
    color: str = Field(..., pattern="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")  # Hex color code
    user_id: str = Field(..., index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name = "labels"
        indexes = ["user_id"]
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Work",
                "color": "#3B82F6",
                "user_id": "user_id_here"
            }
        }


class LabelCreate(BaseModel):
    """Schema for creating a new label."""
    name: str = Field(..., min_length=1, max_length=50)
    color: str = Field(..., pattern="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")


class LabelUpdate(BaseModel):
    """Schema for updating a label."""
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    color: Optional[str] = Field(None, pattern="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")


class LabelResponse(BaseModel):
    """Schema for label response."""
    id: str
    name: str
    color: str
    user_id: str
    created_at: datetime
    
    class Config:
        from_attributes = True

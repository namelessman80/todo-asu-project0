from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class PriorityLevel(str, Enum):
    """Priority level enum for tasks."""
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Task(Document):
    """Task document model for MongoDB."""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    priority: PriorityLevel = PriorityLevel.MEDIUM
    deadline: datetime
    completed: bool = False
    labels: List[str] = []  # List of label IDs
    user_id: str = Field(..., index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name = "tasks"
        indexes = ["user_id", "completed", "deadline"]
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Complete project",
                "description": "Finish the TODO app",
                "priority": "High",
                "deadline": "2024-12-31T23:59:59",
                "completed": False,
                "labels": [],
                "user_id": "user_id_here"
            }
        }


class TaskCreate(BaseModel):
    """Schema for creating a new task."""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    priority: PriorityLevel = PriorityLevel.MEDIUM
    deadline: datetime
    completed: bool = False
    labels: List[str] = []


class TaskUpdate(BaseModel):
    """Schema for updating a task."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    priority: Optional[PriorityLevel] = None
    deadline: Optional[datetime] = None
    completed: Optional[bool] = None
    labels: Optional[List[str]] = None


class TaskResponse(BaseModel):
    """Schema for task response."""
    id: str
    title: str
    description: Optional[str] = None
    priority: str
    deadline: datetime
    completed: bool
    labels: List[str]
    user_id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

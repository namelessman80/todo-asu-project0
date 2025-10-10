from beanie import Document
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class User(Document):
    """User document model for MongoDB."""
    email: EmailStr = Field(..., unique=True)
    full_name: Optional[str] = Field(None, min_length=1, max_length=100)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name = "users"
        indexes = ["email"]
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "full_name": "John Doe",
                "hashed_password": "hashed_password_here",
                "created_at": "2024-01-01T00:00:00"
            }
        }


class UserCreate(BaseModel):
    """Schema for creating a new user."""
    email: EmailStr
    full_name: Optional[str] = Field(None, min_length=1, max_length=100)
    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """Schema for updating user profile."""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, min_length=1, max_length=100)


class UserResponse(BaseModel):
    """Schema for user response."""
    id: str
    email: str
    full_name: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserInDB(BaseModel):
    """Schema for user in database (used internally)."""
    id: str
    email: str
    full_name: Optional[str]
    hashed_password: str
    created_at: datetime
    
    class Config:
        from_attributes = True

from datetime import timedelta, datetime
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User, UserCreate, UserResponse
from models.label import Label
from models.token import Token
from auth import (
    get_password_hash,
    authenticate_user,
    create_access_token,
    get_user_by_email,
)
from config import settings

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate):
    """Register a new user."""
    # Check if user already exists
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user using Beanie
    new_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=get_password_hash(user.password),
        created_at=datetime.utcnow()
    )
    await new_user.insert()
    
    # Create default labels for new user
    default_labels = [
        Label(name="Work", color="#3B82F6", user_id=str(new_user.id), created_at=datetime.utcnow()),
        Label(name="Personal", color="#10B981", user_id=str(new_user.id), created_at=datetime.utcnow()),
        Label(name="Urgent", color="#EF4444", user_id=str(new_user.id), created_at=datetime.utcnow()),
    ]
    for label in default_labels:
        await label.insert()
    
    return UserResponse(
        id=str(new_user.id),
        email=new_user.email,
        full_name=new_user.full_name,
        created_at=new_user.created_at
    )


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login with email and password."""
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/logout")
async def logout():
    """Logout (token invalidation handled on client side)."""
    return {"message": "Successfully logged out"}

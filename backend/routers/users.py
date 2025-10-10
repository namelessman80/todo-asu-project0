from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User, UserResponse, UserInDB, UserUpdate
from auth import get_current_user
from beanie import PydanticObjectId

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: UserInDB = Depends(get_current_user)):
    """Get current user information."""
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        created_at=current_user.created_at
    )


@router.put("/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    current_user: UserInDB = Depends(get_current_user)
):
    """Update current user profile."""
    # Get the user document from database
    user = await User.get(PydanticObjectId(current_user.id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check if email is being updated and if it's already taken
    if user_update.email is not None and user_update.email != user.email:
        existing_user = await User.find_one(User.email == user_update.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already taken"
            )
        user.email = user_update.email
    
    # Update full name if provided
    if user_update.full_name is not None:
        user.full_name = user_update.full_name
    
    # Save the updated user
    await user.save()
    
    return UserResponse(
        id=str(user.id),
        email=user.email,
        full_name=user.full_name,
        created_at=user.created_at
    )

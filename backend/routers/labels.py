from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.label import Label, LabelCreate, LabelUpdate, LabelResponse
from models.user import UserInDB
from auth import get_current_user
from beanie import PydanticObjectId
from datetime import datetime

router = APIRouter(prefix="/labels", tags=["labels"])


@router.post("", response_model=LabelResponse, status_code=status.HTTP_201_CREATED)
async def create_label(
    label: LabelCreate,
    current_user: UserInDB = Depends(get_current_user)
):
    """Create a new label."""
    # Check if label with same name already exists for this user
    existing_label = await Label.find_one(
        Label.name == label.name,
        Label.user_id == current_user.id
    )
    if existing_label:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Label with this name already exists"
        )
    
    new_label = Label(
        name=label.name,
        color=label.color,
        user_id=current_user.id,
        created_at=datetime.utcnow()
    )
    await new_label.insert()
    
    return LabelResponse(
        id=str(new_label.id),
        name=new_label.name,
        color=new_label.color,
        user_id=new_label.user_id,
        created_at=new_label.created_at
    )


@router.get("", response_model=List[LabelResponse])
async def get_labels(current_user: UserInDB = Depends(get_current_user)):
    """Get all labels for the current user."""
    labels = await Label.find(Label.user_id == current_user.id).sort("+created_at").to_list()
    
    return [
        LabelResponse(
            id=str(label.id),
            name=label.name,
            color=label.color,
            user_id=label.user_id,
            created_at=label.created_at
        )
        for label in labels
    ]


@router.get("/{label_id}", response_model=LabelResponse)
async def get_label(
    label_id: str,
    current_user: UserInDB = Depends(get_current_user)
):
    """Get a specific label by ID."""
    try:
        label = await Label.get(PydanticObjectId(label_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid label ID"
        )
    
    if not label or label.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Label not found"
        )
    
    return LabelResponse(
        id=str(label.id),
        name=label.name,
        color=label.color,
        user_id=label.user_id,
        created_at=label.created_at
    )


@router.put("/{label_id}", response_model=LabelResponse)
async def update_label(
    label_id: str,
    label_update: LabelUpdate,
    current_user: UserInDB = Depends(get_current_user)
):
    """Update a label."""
    # Get label from database
    try:
        label = await Label.get(PydanticObjectId(label_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid label ID"
        )
    
    if not label or label.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Label not found"
        )
    
    # Check if new name conflicts with existing label
    if label_update.name is not None and label_update.name != label.name:
        existing_label = await Label.find_one(
            Label.name == label_update.name,
            Label.user_id == current_user.id
        )
        if existing_label:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Label with this name already exists"
            )
        label.name = label_update.name
    
    # Update color if provided
    if label_update.color is not None:
        label.color = label_update.color
    
    await label.save()
    
    return LabelResponse(
        id=str(label.id),
        name=label.name,
        color=label.color,
        user_id=label.user_id,
        created_at=label.created_at
    )


@router.delete("/{label_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_label(
    label_id: str,
    current_user: UserInDB = Depends(get_current_user)
):
    """Delete a label."""
    try:
        label = await Label.get(PydanticObjectId(label_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid label ID"
        )
    
    if not label or label.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Label not found"
        )
    
    await label.delete()
    return None

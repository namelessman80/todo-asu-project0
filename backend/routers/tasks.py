from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from models.task import Task, TaskCreate, TaskUpdate, TaskResponse
from models.user import UserInDB
from auth import get_current_user
from beanie import PydanticObjectId
from datetime import datetime

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate,
    current_user: UserInDB = Depends(get_current_user)
):
    """Create a new task."""
    new_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        deadline=task.deadline,
        completed=task.completed,
        labels=task.labels,
        user_id=current_user.id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    await new_task.insert()
    
    return TaskResponse(
        id=str(new_task.id),
        title=new_task.title,
        description=new_task.description,
        priority=new_task.priority.value,
        deadline=new_task.deadline,
        completed=new_task.completed,
        labels=new_task.labels,
        user_id=new_task.user_id,
        created_at=new_task.created_at,
        updated_at=new_task.updated_at
    )


@router.get("", response_model=List[TaskResponse])
async def get_tasks(
    label: Optional[str] = Query(None, description="Filter by label ID"),
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    current_user: UserInDB = Depends(get_current_user)
):
    """Get all tasks for the current user with optional filtering."""
    # Build query
    query = {"user_id": current_user.id}
    if label:
        query["labels"] = label
    if completed is not None:
        query["completed"] = completed
    
    # Use Beanie to find tasks
    tasks = await Task.find(query).sort("-created_at").to_list()
    
    return [
        TaskResponse(
            id=str(task.id),
            title=task.title,
            description=task.description,
            priority=task.priority.value,
            deadline=task.deadline,
            completed=task.completed,
            labels=task.labels,
            user_id=task.user_id,
            created_at=task.created_at,
            updated_at=task.updated_at
        )
        for task in tasks
    ]


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: str,
    current_user: UserInDB = Depends(get_current_user)
):
    """Get a specific task by ID."""
    try:
        task = await Task.get(PydanticObjectId(task_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid task ID"
        )
    
    if not task or task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return TaskResponse(
        id=str(task.id),
        title=task.title,
        description=task.description,
        priority=task.priority.value,
        deadline=task.deadline,
        completed=task.completed,
        labels=task.labels,
        user_id=task.user_id,
        created_at=task.created_at,
        updated_at=task.updated_at
    )


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: str,
    task_update: TaskUpdate,
    current_user: UserInDB = Depends(get_current_user)
):
    """Update a task."""
    # Get task from database
    try:
        task = await Task.get(PydanticObjectId(task_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid task ID"
        )
    
    if not task or task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Update fields if provided
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.priority is not None:
        task.priority = task_update.priority
    if task_update.deadline is not None:
        task.deadline = task_update.deadline
    if task_update.completed is not None:
        task.completed = task_update.completed
    if task_update.labels is not None:
        task.labels = task_update.labels
    
    task.updated_at = datetime.utcnow()
    await task.save()
    
    return TaskResponse(
        id=str(task.id),
        title=task.title,
        description=task.description,
        priority=task.priority.value,
        deadline=task.deadline,
        completed=task.completed,
        labels=task.labels,
        user_id=task.user_id,
        created_at=task.created_at,
        updated_at=task.updated_at
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: str,
    current_user: UserInDB = Depends(get_current_user)
):
    """Delete a task."""
    try:
        task = await Task.get(PydanticObjectId(task_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid task ID"
        )
    
    if not task or task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    await task.delete()
    return None

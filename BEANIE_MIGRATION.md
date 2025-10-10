# Beanie ODM Migration Guide

This document explains the migration from direct Motor usage to Beanie ODM (Object Document Mapper) for MongoDB operations.

## What is Beanie?

Beanie is an asynchronous Python ODM (Object Document Mapper) for MongoDB built on top of Motor and Pydantic. It provides:

- **Type Safety**: Full Pydantic integration for data validation
- **Clean API**: Pythonic interface for MongoDB operations
- **Async/Await**: Built on Motor for non-blocking operations
- **Automatic Indexing**: Define indexes in your models
- **Query Builder**: Intuitive query syntax

## Changes Made

### 1. Dependencies (`requirements.txt`)

**Before:**
```txt
pymongo==4.6.0
motor==3.3.2
```

**After:**
```txt
beanie==1.23.6
motor==3.3.2
```

Note: Beanie includes Motor as a dependency, so Motor is still used under the hood.

### 2. Database Connection (`database.py`)

**Before:**
```python
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING, IndexModel

client = None
database = None

async def connect_to_mongo():
    global client, database
    client = AsyncIOMotorClient(settings.mongodb_url)
    database = client[settings.database_name]
    
    # Manual index creation
    await database.users.create_index([("email", ASCENDING)], unique=True)
    await database.tasks.create_index([("user_id", ASCENDING)])
    await database.labels.create_index([("user_id", ASCENDING)])
```

**After:**
```python
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.user import User
from models.task import Task
from models.label import Label

client = None

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(settings.mongodb_url)
    database = client[settings.database_name]
    
    # Initialize Beanie with document models
    await init_beanie(
        database=database,
        document_models=[User, Task, Label]
    )
```

### 3. Models

**Before (Pydantic BaseModel):**
```python
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    # ...
```

**After (Beanie Document):**
```python
from beanie import Document
from pydantic import Field

class Task(Document):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    user_id: str = Field(..., index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name = "tasks"  # Collection name
        indexes = ["user_id", "completed", "deadline"]
```

### 4. CRUD Operations

#### Create

**Before:**
```python
task_dict = task.model_dump()
task_dict["user_id"] = current_user.id
result = await db.tasks.insert_one(task_dict)
task_dict["id"] = str(result.inserted_id)
```

**After:**
```python
new_task = Task(
    title=task.title,
    description=task.description,
    user_id=current_user.id
)
await new_task.insert()
# Access ID with: str(new_task.id)
```

#### Read (Find One)

**Before:**
```python
user = await db.users.find_one({"email": email})
if user:
    user["id"] = str(user["_id"])
    return UserInDB(**user)
```

**After:**
```python
user = await User.find_one(User.email == email)
if user:
    return UserInDB(
        id=str(user.id),
        email=user.email,
        # ...
    )
```

#### Read (Find Many)

**Before:**
```python
tasks = []
async for task in db.tasks.find({"user_id": user_id}).sort("created_at", -1):
    task["id"] = str(task["_id"])
    tasks.append(TaskResponse(**task))
```

**After:**
```python
tasks = await Task.find({"user_id": user_id}).sort("-created_at").to_list()
# Or using query builder:
tasks = await Task.find(Task.user_id == user_id).sort("-created_at").to_list()
```

#### Update

**Before:**
```python
await db.tasks.update_one(
    {"_id": ObjectId(task_id)},
    {"$set": update_data}
)
updated_task = await db.tasks.find_one({"_id": ObjectId(task_id)})
```

**After:**
```python
task = await Task.get(PydanticObjectId(task_id))
task.title = new_title
task.updated_at = datetime.utcnow()
await task.save()
```

#### Delete

**Before:**
```python
result = await db.tasks.delete_one({"_id": ObjectId(task_id)})
if result.deleted_count == 0:
    raise HTTPException(...)
```

**After:**
```python
task = await Task.get(PydanticObjectId(task_id))
if not task:
    raise HTTPException(...)
await task.delete()
```

## Benefits of Beanie

### 1. Type Safety
```python
# Beanie uses Pydantic models, so you get full type checking
task = await Task.get(task_id)
task.title = "New Title"  # IDE autocomplete works!
# task.invalid_field = "value"  # This would be caught by type checker
```

### 2. Clean Query Syntax
```python
# Before (dict-based queries)
await db.tasks.find({"user_id": user_id, "completed": False})

# After (type-safe queries)
await Task.find(Task.user_id == user_id, Task.completed == False).to_list()
```

### 3. Automatic Index Management
```python
class Task(Document):
    user_id: str = Field(..., index=True)  # Simple index
    
    class Settings:
        indexes = ["user_id", "completed"]  # Multiple indexes
```

### 4. Built-in Validation
```python
class Label(Document):
    name: str = Field(..., min_length=1, max_length=50)
    color: str = Field(..., pattern="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
```

## MongoDB Design Decisions

Following the MongoDB embedding vs. referencing guidelines from `todo-specs.md`:

### Users → Tasks (Reference)
- **Decision**: Reference (store `user_id` in tasks)
- **Reason**: 
  - High cardinality: Users can have many tasks
  - Tasks can exist independently
  - Tasks and users are queried separately

### Tasks → Labels (Reference)
- **Decision**: Reference (store label IDs in task's `labels` array)
- **Reason**:
  - Many-to-many relationship
  - Labels can be reused across tasks
  - Labels need to be managed independently
  - Prevents data duplication

### Embedded vs Referenced Summary

| Relationship | Type | Reason |
|--------------|------|--------|
| User → Tasks | Reference | High cardinality, independent existence |
| User → Labels | Reference | Independent management, reusability |
| Task → Labels | Reference | Many-to-many, prevents duplication |

## Migration Checklist

- [x] Add Beanie to `requirements.txt`
- [x] Update `database.py` to use `init_beanie()`
- [x] Convert all models to Beanie Documents
- [x] Update all CRUD operations in routers
- [x] Update authentication helpers
- [x] Update environment templates with MongoDB Atlas connection
- [x] Update documentation (README, SETUP_GUIDE)

## Testing After Migration

1. **Verify Database Connection**:
   ```bash
   # Start backend and check logs
   python main.py
   # Should see: "Connected to MongoDB database: todo_app"
   ```

2. **Test API Endpoints**:
   - Visit http://localhost:8000/docs
   - Test signup, login, and CRUD operations

3. **Check Indexes**:
   - Use MongoDB Compass or mongosh
   - Verify indexes are created on collections

## Resources

- [Beanie Documentation](https://roman-right.github.io/beanie/)
- [MongoDB Embedding vs Referencing](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design)
- [FastAPI with Beanie Tutorial](https://roman-right.github.io/beanie/tutorial/fastapi/)
- [Project Specifications](./todo-specs.md)


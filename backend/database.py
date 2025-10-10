from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from config import settings
from models.user import User
from models.task import Task
from models.label import Label
import sys

client = None


async def connect_to_mongo():
    """Initialize MongoDB connection and Beanie ODM."""
    global client
    try:
        print(f"Connecting to MongoDB...")
        print(f"Database: {settings.database_name}")
        
        # Create client with timeout settings
        client = AsyncIOMotorClient(
            settings.mongodb_url,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=10000
        )
        
        # Test the connection
        await client.admin.command('ping')
        print("✓ MongoDB connection successful!")
        
        database = client[settings.database_name]
        
        # Initialize Beanie with the document models
        print("Initializing Beanie ODM...")
        await init_beanie(
            database=database,
            document_models=[User, Task, Label]
        )
        
        print(f"✓ Connected to MongoDB database: {settings.database_name}")
        print(f"✓ Beanie ODM initialized with models: User, Task, Label")
        
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {str(e)}")
        print(f"Connection URL: {settings.mongodb_url[:50]}...")
        sys.exit(1)


async def close_mongo_connection():
    """Close database connection."""
    global client
    if client:
        client.close()
        print("Closed MongoDB connection!")

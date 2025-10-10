# TODO Application - Full Stack Project

A modern, full-stack TODO application built with FastAPI (backend), Next.js (frontend), and MongoDB (database). This application features user authentication, task management with labels, and a beautiful, responsive UI built with Tailwind CSS.

## 🚀 Features

### Required Features (MVP)
- ✅ **User Authentication**: Secure signup, login, and logout functionality with JWT tokens
- ✅ **Task Management**: Complete CRUD operations for tasks
  - Create tasks with title, description, priority (High/Medium/Low), and deadline
  - View all tasks with filtering capabilities
  - Update task details and mark as complete
  - Delete tasks
- ✅ **Labeling System**: Create and manage labels to categorize tasks
  - Predefined labels (Work, Personal, Urgent) created on signup
  - Assign multiple labels to tasks
  - Filter tasks by labels
- ✅ **Data Persistence**: All data stored in MongoDB

### Stretch Goals (Bonus Features)
- ✅ **Task Filtering**: Filter tasks by label and completion status
- ✅ **User Profile Management**: View user information (expandable to edit profile)
- ✅ **Responsive Design**: Fully responsive UI that works on all screen sizes
- ✅ **Comprehensive Error Handling**: Clear error messages with toast notifications

## 🛠️ Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **MongoDB**: NoSQL database for data persistence
- **Beanie**: Async MongoDB ODM (Object Document Mapper) built on top of Motor
- **Motor**: Async MongoDB driver
- **PyJWT**: JSON Web Token implementation
- **Passlib**: Password hashing library
- **Python 3.8+**

### Frontend
- **Next.js 15**: React framework with App Router
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework
- **Axios**: HTTP client for API requests
- **React Hot Toast**: Toast notifications
- **date-fns**: Date formatting library

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.12** (recommended) or Python 3.8+
- **Node.js 18 or higher**
- **npm** or **yarn** package manager
- ✅ **No MongoDB installation needed!** (Uses MongoDB Atlas cloud database)

## 🔧 Setup Instructions

### Quick Start Summary

```bash
# Backend setup
cd backend
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install --upgrade certifi  # Fix SSL for MongoDB Atlas
cp env.template .env
python main.py

# Frontend setup (in new terminal)
cd frontend
npm install
echo "NEXT_PUBLIC_API_URL=http://localhost:8000/api" > .env.local
npm run dev
```

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd todo-asu-project0
```

### 2. Backend Setup

#### Create Python Virtual Environment

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3.12 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the `backend` directory by copying `env.template`:

```bash
# Make sure you're in the backend directory
cd backend
cp env.template .env
```

The default configuration uses **MongoDB Atlas** (cloud database provided by instructor):

```env
MONGODB_URL=mongodb+srv://db_user1:XM4Q2jcOShpjAUHG@cluster0.faxo8fl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
DATABASE_NAME=todo_app
SECRET_KEY=your-secret-key-change-this-in-production-09876543210
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Important:** 
- ✅ **No local MongoDB installation needed!** The project uses MongoDB Atlas (cloud)
- The MongoDB Atlas connection is provided by the instructor (cluster0.faxo8fl.mongodb.net)
- Change the `SECRET_KEY` to a secure random string in production

#### Fix SSL Certificates (macOS with Python 3.12)

If you're using Python 3.12 on macOS, you need to install SSL certificates:

```bash
# Option 1: Run the certificate installer (if available)
/Applications/Python\ 3.12/Install\ Certificates.command

# Option 2: Or manually upgrade certifi in your venv
cd backend
source venv/bin/activate
pip install --upgrade certifi
```

**Note**: This is required for MongoDB Atlas connection to work with Python 3.12 on macOS.

#### Optional: Local MongoDB (Not Required)

The project uses MongoDB Atlas by default. Only set up local MongoDB if you need offline development:

```bash
# Using Docker (easiest):
docker run -d -p 27017:27017 --name mongodb mongo:latest

# Then update .env:
MONGODB_URL=mongodb://localhost:27017
```

#### Run the Backend

```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
source venv/bin/activate

# Start the backend server
python main.py
```

You should see output like this:
```
Connecting to MongoDB...
Database: todo_app
✓ MongoDB connection successful!
Initializing Beanie ODM...
✓ Connected to MongoDB database: todo_app
✓ Beanie ODM initialized with models: User, Task, Label
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

The backend API will be available at: `http://localhost:8000`  
API documentation (Swagger UI): `http://localhost:8000/docs`

**Alternative**: Use uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Troubleshooting**:
- If you get "Address already in use": `lsof -ti:8000 | xargs kill -9`
- If SSL errors persist: `pip install --upgrade certifi`

### 3. Frontend Setup

Open a new terminal window/tab:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create environment file
# Create a file named .env.local with:
echo "NEXT_PUBLIC_API_URL=http://localhost:8000/api" > .env.local

# Start the development server
npm run dev
```

The frontend will be available at: `http://localhost:3000`

## 🎯 Usage

### Getting Started

1. **Sign Up**: Navigate to `http://localhost:3000` and click "Sign up"
   - Enter your email, password, and optionally your full name
   - Three default labels (Work, Personal, Urgent) will be created automatically

2. **Login**: Use your credentials to log in

3. **Create Tasks**: 
   - Click "Create Task" button
   - Fill in task details (title, description, priority, deadline)
   - Assign labels to categorize your task
   - Click "Create Task" to save

4. **Manage Tasks**:
   - Check the checkbox to mark tasks as complete
   - Click the edit icon to modify task details
   - Click the delete icon to remove tasks
   - Use filters to view tasks by status or label

5. **Filter Tasks**:
   - Filter by completion status (All, Pending, Completed)
   - Filter by label (All Labels, Work, Personal, Urgent, etc.)

## 📁 Project Structure

```
todo-asu-project0/
├── backend/
│   ├── models/              # Beanie Document models
│   │   ├── __init__.py
│   │   ├── user.py          # User models (Beanie Document)
│   │   ├── task.py          # Task models (Beanie Document)
│   │   ├── label.py         # Label models (Beanie Document)
│   │   └── token.py         # Token models
│   ├── routers/             # API endpoints
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication endpoints
│   │   ├── users.py         # User endpoints
│   │   ├── tasks.py         # Task CRUD endpoints
│   │   └── labels.py        # Label CRUD endpoints
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration settings
│   ├── database.py          # MongoDB connection
│   ├── auth.py              # Authentication utilities
│   └── requirements.txt     # Python dependencies
│
├── frontend/
│   ├── app/                 # Next.js app directory
│   │   ├── dashboard/       # Dashboard page
│   │   ├── login/           # Login page
│   │   ├── signup/          # Signup page
│   │   ├── layout.tsx       # Root layout
│   │   ├── page.tsx         # Home page
│   │   └── globals.css      # Global styles
│   ├── components/          # React components
│   │   ├── TaskCard.tsx     # Task card component
│   │   └── TaskModal.tsx    # Task create/edit modal
│   ├── lib/                 # Utilities
│   │   ├── api.ts           # API client
│   │   └── auth-context.tsx # Authentication context
│   ├── types/               # TypeScript types
│   │   └── index.ts         # Type definitions
│   └── package.json         # Node dependencies
│
└── README.md                # This file
```

## 🗄️ Database Schema

### Users Collection
```javascript
{
  "_id": ObjectId,
  "email": String (unique),
  "full_name": String (optional),
  "hashed_password": String,
  "created_at": DateTime
}
```

### Tasks Collection
```javascript
{
  "_id": ObjectId,
  "title": String,
  "description": String (optional),
  "priority": String ("High" | "Medium" | "Low"),
  "deadline": DateTime,
  "completed": Boolean,
  "labels": Array<String>,
  "user_id": String,
  "created_at": DateTime,
  "updated_at": DateTime
}
```

### Labels Collection
```javascript
{
  "_id": ObjectId,
  "name": String,
  "color": String,
  "user_id": String,
  "created_at": DateTime
}
```

## 🔒 Security Features

- Password hashing using bcrypt
- JWT token-based authentication
- Protected API endpoints requiring authentication
- CORS configuration for frontend-backend communication
- Input validation using Pydantic models

## 🌐 API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user

### Users
- `GET /api/users/me` - Get current user info
- `PUT /api/users/me` - Update user profile

### Tasks
- `GET /api/tasks` - Get all tasks (with optional filters)
- `POST /api/tasks` - Create new task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

### Labels
- `GET /api/labels` - Get all labels
- `POST /api/labels` - Create new label
- `GET /api/labels/{id}` - Get specific label
- `PUT /api/labels/{id}` - Update label
- `DELETE /api/labels/{id}` - Delete label

## 🧪 Testing the Application

1. **Backend API Testing**: Visit `http://localhost:8000/docs` for interactive API documentation
2. **Frontend Testing**: Navigate through the UI to test all features
3. **Health Check**: `GET http://localhost:8000/health` or `curl http://localhost:8000/health`

## 🔧 Common Issues & Solutions

### Backend won't start - "Address already in use"
```bash
# Kill the process using port 8000
lsof -ti:8000 | xargs kill -9
# Then start again
cd backend && source venv/bin/activate && python main.py
```

### SSL Certificate Error (MongoDB Atlas)
```bash
# This happens on macOS with Python 3.12
cd backend
source venv/bin/activate
pip install --upgrade certifi
```

### "No module named 'beanie'" or import errors
```bash
# Make sure venv is activated and dependencies are installed
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### Backend starts but stuck at "Waiting for application startup"
```bash
# Check if .env file exists
ls backend/.env

# If not, create it:
cd backend
cp env.template .env
```

### Can't connect to mongosh
This is expected! You don't need local MongoDB. The backend connects to MongoDB Atlas automatically. If you want to explore the database, use:
```bash
mongosh "mongodb+srv://db_user1:XM4Q2jcOShpjAUHG@cluster0.faxo8fl.mongodb.net/"
```

## 📝 Development Notes

- The backend uses async/await with Beanie ODM for non-blocking MongoDB operations
- Beanie provides a clean, Pythonic interface for MongoDB documents
- MongoDB embedding/referencing guidelines followed per project specifications
- Frontend uses React Server Components and Client Components appropriately
- Task filtering is implemented as a stretch goal feature
- Error handling with user-friendly toast notifications
- Responsive design tested on mobile, tablet, and desktop screens

## 🚧 Future Enhancements

- Task sorting (by date, priority, etc.)
- Task search functionality
- Recurring tasks
- Task reminders/notifications
- Collaborative tasks (sharing with other users)
- Dark mode support
- Export tasks to CSV/PDF
- Task categories/projects

## 🤝 Contributing

This is a student project for ASU's full-stack development course. For any questions or issues, please contact the repository owner.

## 📄 License

This project is created for educational purposes as part of ASU's coursework.

## 👨‍💻 Author

Created as Project 0 for ASU Full-Stack Development Course
Deadline: October 13, 2025

## 🙏 Acknowledgments

- FastAPI documentation and community
- Next.js documentation and examples
- Tailwind CSS for the amazing utility-first CSS framework
- MongoDB for flexible document storage

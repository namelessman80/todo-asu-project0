# Quick Start Guide - TODO App

## 🚀 Get Running in 5 Minutes

### Prerequisites
- Python 3.12 installed
- Node.js 18+ installed
- Internet connection (for MongoDB Atlas)

### Step 1: Backend Setup (2 minutes)

```bash
# Navigate to backend
cd backend

# Create and activate virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Fix SSL certificates for MongoDB Atlas (macOS only)
pip install --upgrade certifi

# Create .env file
cp env.template .env

# Start backend
python main.py
```

**Expected Output:**
```
Connecting to MongoDB...
Database: todo_app
✓ MongoDB connection successful!
✓ Connected to MongoDB database: todo_app
✓ Beanie ODM initialized with models: User, Task, Label
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ Backend ready at: http://localhost:8000

### Step 2: Frontend Setup (2 minutes)

Open a **new terminal** window:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Create environment file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000/api" > .env.local

# Start frontend
npm run dev
```

✅ Frontend ready at: http://localhost:3000

### Step 3: Use the App (1 minute)

1. Open http://localhost:3000
2. Click "Sign up" to create an account
3. Start creating tasks!

## 🔧 Common Issues

### "Address already in use" (Port 8000)
```bash
lsof -ti:8000 | xargs kill -9
```

### SSL Certificate Error
```bash
cd backend
source venv/bin/activate
pip install --upgrade certifi
```

### Can't find .env file
```bash
cd backend
cp env.template .env
```

### Wrong directory error
Make sure you're in the correct directory:
- Backend commands: Run from `backend/` directory
- Frontend commands: Run from `frontend/` directory

## 📊 Verify Everything Works

### Check Backend Health
```bash
curl http://localhost:8000/health
# Should return: {"status":"healthy"}
```

### Check API Docs
Visit: http://localhost:8000/docs

### Check Frontend
Visit: http://localhost:3000

## 🎯 What You Get

- ✅ MongoDB Atlas (cloud database) - Already configured
- ✅ FastAPI backend with authentication
- ✅ Next.js frontend with beautiful UI
- ✅ Create, read, update, delete tasks
- ✅ Label system for organization
- ✅ Filter tasks by status and labels
- ✅ Responsive design

## 💡 Pro Tips

1. **Keep both terminals open** - One for backend, one for frontend
2. **Backend must start first** - Frontend needs API to be running
3. **No local MongoDB needed** - Everything uses MongoDB Atlas
4. **API docs are interactive** - Test endpoints at /docs

## 📚 Need More Help?

- Full documentation: [README.md](./README.md)
- Setup guide: [SETUP_GUIDE.md](./SETUP_GUIDE.md)
- Connection issues: [CONNECTION_FIXED.md](./CONNECTION_FIXED.md)

---

**That's it! You're ready to code.** 🎉


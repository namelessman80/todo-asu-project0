# Quick Setup Guide

This guide will help you get the TODO application up and running quickly.

## Quick Start (3 Steps)

### Step 1: Start MongoDB

**Option A: Using Docker (Recommended)**
```bash
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

**Option B: Using Local MongoDB**
```bash
# macOS (with Homebrew)
brew services start mongodb-community

# Linux
sudo systemctl start mongod
```

**Option C: Using MongoDB Atlas (Cloud) - Default for this project**
1. The project uses MongoDB Atlas provided by the instructor
2. Connection details are in `backend/env.template`
3. Copy `env.template` to `.env`: `cp env.template .env`
4. MongoDB Atlas cluster: cluster0.faxo8fl.mongodb.net

### Step 2: Start Backend

Open a terminal:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Or use the provided script:
```bash
cd backend
./run.sh  # On Windows: use Git Bash or WSL
```

The backend will start at: http://localhost:8000
API docs available at: http://localhost:8000/docs

### Step 3: Start Frontend

Open a new terminal:
```bash
cd frontend
npm install
echo "NEXT_PUBLIC_API_URL=http://localhost:8000/api" > .env.local
npm run dev
```

Or use the provided script:
```bash
cd frontend
./run.sh  # On Windows: use Git Bash or WSL
```

The frontend will start at: http://localhost:3000

## Testing the Application

1. Open http://localhost:3000 in your browser
2. Click "Sign up" to create a new account
3. After signup, you'll be automatically logged in
4. Start creating tasks!

## Default Labels

When you sign up, three labels are automatically created:
- **Work** (Blue)
- **Personal** (Green)
- **Urgent** (Red)

## Troubleshooting

### MongoDB Connection Error
- Ensure MongoDB is running: `docker ps` or `brew services list`
- Check the connection string in `backend/.env`
- Default: `mongodb://localhost:27017`

### Backend Port Already in Use
- Kill the process using port 8000:
  ```bash
  # macOS/Linux
  lsof -ti:8000 | xargs kill -9
  
  # Windows
  netstat -ano | findstr :8000
  taskkill /PID <PID> /F
  ```

### Frontend Port Already in Use
- Kill the process using port 3000 or run on different port:
  ```bash
  npm run dev -- -p 3001
  ```

### Import Errors in Python
- Make sure virtual environment is activated:
  ```bash
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate     # Windows
  ```
- Reinstall dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Module Not Found in Frontend
- Clear Next.js cache and reinstall:
  ```bash
  rm -rf .next node_modules package-lock.json
  npm install
  npm run dev
  ```

## Environment Variables

### Backend (.env)

**Default (MongoDB Atlas - provided by instructor):**
```env
MONGODB_URL=mongodb+srv://db_user1:XM4Q2jcOShpjAUHG@cluster0.faxo8fl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
DATABASE_NAME=todo_app
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**For Local MongoDB:**
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=todo_app
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## Useful Commands

### Backend
```bash
# Start with auto-reload
uvicorn main:app --reload

# Check Python version
python --version

# List installed packages
pip list
```

### Frontend
```bash
# Start development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Check Node version
node --version
```

### MongoDB
```bash
# Start MongoDB (Docker)
docker start mongodb

# Stop MongoDB (Docker)
docker stop mongodb

# Connect to MongoDB shell
mongosh

# View databases
mongosh --eval "show dbs"
```

## API Testing

Use the interactive API docs at http://localhost:8000/docs to test endpoints:

1. Create a user via `/api/auth/signup`
2. Login via `/api/auth/login` to get a token
3. Click "Authorize" button and paste your token
4. Test other endpoints

Or use curl:
```bash
# Signup
curl -X POST http://localhost:8000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123"
```

## Development Tips

1. **Hot Reload**: Both backend and frontend support hot reload during development
2. **API Docs**: Use Swagger UI at `/docs` for testing API endpoints
3. **Console Logs**: Check browser console and terminal for debugging
4. **Database GUI**: Use MongoDB Compass to view database contents
5. **Port Conflicts**: If ports are in use, change them in the respective config files

## Production Deployment

For production deployment:
1. Change `SECRET_KEY` in backend `.env`
2. Update `MONGODB_URL` to production database
3. Update `NEXT_PUBLIC_API_URL` to production API URL
4. Build frontend: `npm run build`
5. Use production WSGI server for backend (e.g., Gunicorn)
6. Consider using Docker for containerization

## Need Help?

- Check the main README.md for detailed information
- Review the API documentation at http://localhost:8000/docs
- Check MongoDB connection at http://localhost:8000/health







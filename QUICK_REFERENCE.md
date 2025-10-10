# Quick Reference Card

## 🚀 Starting the Application

### Option 1: Using Shell Scripts (Easiest)
```bash
# Terminal 1 - Backend
cd backend && ./run.sh

# Terminal 2 - Frontend
cd frontend && ./run.sh
```

### Option 2: Using Docker Compose + Manual Start
```bash
# Start MongoDB
docker-compose up -d

# Terminal 1 - Backend
cd backend
source venv/bin/activate
python main.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

### Option 3: Manual Setup
```bash
# Start MongoDB
docker run -d -p 27017:27017 --name mongodb mongo

# Terminal 1 - Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

# Terminal 2 - Frontend
cd frontend
npm install
npm run dev
```

## 🔗 Important URLs

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:3000 | Main application |
| Backend API | http://localhost:8000 | REST API |
| API Docs | http://localhost:8000/docs | Swagger UI |
| Health Check | http://localhost:8000/health | Server status |

## 📝 Common Commands

### Backend
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install/Update dependencies
pip install -r requirements.txt

# Run backend
python main.py

# Run with uvicorn directly
uvicorn main:app --reload --port 8000

# Deactivate virtual environment
deactivate
```

### Frontend
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Clean cache
rm -rf .next node_modules
npm install
```

### MongoDB
```bash
# Start (Docker)
docker start mongodb

# Stop (Docker)
docker stop mongodb

# Remove (Docker)
docker rm mongodb

# Connect to shell
mongosh

# Connect to specific database
mongosh mongodb://localhost:27017/todo_app

# Using Docker Compose
docker-compose up -d     # Start
docker-compose down      # Stop
docker-compose ps        # Status
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000 (backend)
lsof -ti:8000
kill -9 $(lsof -ti:8000)

# Find process using port 3000 (frontend)
lsof -ti:3000
kill -9 $(lsof -ti:3000)
```

### MongoDB Connection Issues
```bash
# Check if MongoDB is running
docker ps | grep mongo

# Restart MongoDB
docker restart mongodb

# View MongoDB logs
docker logs mongodb
```

### Python Import Errors
```bash
# Ensure venv is activated (should see (venv) in prompt)
source venv/bin/activate

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

### Frontend Module Not Found
```bash
# Clear and reinstall
rm -rf node_modules package-lock.json .next
npm install
npm run dev
```

## 🧪 Testing

### Test Backend API
```bash
# Health check
curl http://localhost:8000/health

# Signup
curl -X POST http://localhost:8000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123"
```

### Or use the Swagger UI
1. Go to http://localhost:8000/docs
2. Click on an endpoint
3. Click "Try it out"
4. Fill in parameters
5. Click "Execute"

## 📦 Project Structure Quick Look

```
todo-asu-project0/
├── backend/
│   ├── models/       # Data models
│   ├── routers/      # API endpoints
│   ├── main.py       # App entry
│   └── config.py     # Settings
├── frontend/
│   ├── app/          # Pages
│   ├── components/   # UI components
│   ├── lib/          # Utilities
│   └── types/        # TypeScript types
└── README.md         # Full documentation
```

## 🔑 Environment Files

### Backend `.env`
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=todo_app
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend `.env.local`
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## 🎯 Default User Flow

1. Visit http://localhost:3000
2. Click "Sign up"
3. Enter email and password
4. Auto-login after signup
5. Three default labels created (Work, Personal, Urgent)
6. Click "Create Task" to add tasks
7. Manage tasks from dashboard

## 📊 Dashboard Features

- **Stats**: Total, Pending, Completed, Overdue tasks
- **Filters**: By status and label
- **Task Actions**: Complete, Edit, Delete
- **Task Details**: Title, Description, Priority, Deadline, Labels

## 🎨 Task Priority Levels

- **High**: Red badge
- **Medium**: Yellow badge
- **Low**: Green badge

## 🏷️ Default Labels

| Label | Color | Purpose |
|-------|-------|---------|
| Work | Blue | Work-related tasks |
| Personal | Green | Personal tasks |
| Urgent | Red | High-priority items |

## 💾 Data Persistence

All data is stored in MongoDB:
- Users in `users` collection
- Tasks in `tasks` collection  
- Labels in `labels` collection

## 🔒 Authentication

- JWT tokens stored in localStorage
- Tokens expire in 30 minutes (configurable)
- Passwords hashed with bcrypt
- Protected routes redirect to login

## 📱 Responsive Breakpoints

- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## 🚨 Common Errors & Solutions

| Error | Solution |
|-------|----------|
| "MongoDB connection failed" | Start MongoDB server |
| "Port 8000 already in use" | Kill process or change port |
| "Module not found" | Check venv is activated |
| "Network Error" | Ensure backend is running |
| "401 Unauthorized" | Login again (token expired) |

## 📞 Getting Help

1. Check README.md for detailed docs
2. Check SETUP_GUIDE.md for setup help
3. Check API docs at /docs
4. Check browser console for errors
5. Check terminal logs for errors

## ⚡ Pro Tips

- Use `Ctrl+C` to stop servers
- Keep both terminals open while developing
- Check `/docs` for API testing
- Use MongoDB Compass for database GUI
- Clear browser cache if seeing old data
- Use browser DevTools for debugging

## 🎬 For Demo Video

Show these features:
1. Signup/Login
2. Create multiple tasks
3. Edit a task
4. Complete a task
5. Delete a task
6. Filter by label
7. Filter by status
8. Show responsive design
9. Show error handling
10. Logout

---

**Need more help?** See README.md or SETUP_GUIDE.md







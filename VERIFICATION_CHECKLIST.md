# Project Verification Checklist

Use this checklist to verify that everything is working correctly before submission.

## Pre-Flight Setup Checklist

### Backend Setup
- [ ] MongoDB is running (Docker, local, or Atlas)
- [ ] Virtual environment created: `python3 -m venv venv`
- [ ] Virtual environment activated: `source venv/bin/activate`
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Environment file created (copy from `env.template` to `.env`)
- [ ] Backend starts without errors: `python main.py`
- [ ] API docs accessible at: http://localhost:8000/docs
- [ ] Health check passes: http://localhost:8000/health

### Frontend Setup
- [ ] Node.js installed (v18+)
- [ ] Dependencies installed: `npm install`
- [ ] Environment file created (`.env.local` with API URL)
- [ ] Frontend starts without errors: `npm run dev`
- [ ] Frontend accessible at: http://localhost:3000
- [ ] No console errors in browser

## Feature Verification

### User Authentication
- [ ] Can access signup page at `/signup`
- [ ] Can create new account with valid email/password
- [ ] Password validation works (min 6 characters)
- [ ] Email validation works
- [ ] Duplicate email shows error
- [ ] After signup, user is auto-logged in
- [ ] Can logout successfully
- [ ] Can login with existing credentials
- [ ] Invalid credentials show error
- [ ] Token is stored in localStorage
- [ ] Protected routes redirect to login when not authenticated

### Task Management
- [ ] Can access dashboard after login
- [ ] Dashboard shows user statistics (Total, Pending, Completed, Overdue)
- [ ] Can click "Create Task" button
- [ ] Task creation modal opens
- [ ] Can create task with:
  - [ ] Title (required)
  - [ ] Description (optional)
  - [ ] Priority (High/Medium/Low)
  - [ ] Deadline (date/time picker)
  - [ ] Labels (multiple selection)
- [ ] New task appears in task list
- [ ] Can mark task as complete (checkbox)
- [ ] Completed tasks show visual indication
- [ ] Can edit existing task
- [ ] Task updates reflect immediately
- [ ] Can delete task with confirmation
- [ ] Task removal is immediate

### Labeling System
- [ ] Three default labels created on signup (Work, Personal, Urgent)
- [ ] Labels show in task creation modal
- [ ] Can select multiple labels for a task
- [ ] Labels display on task cards with correct styling
- [ ] Can filter tasks by label using dropdown
- [ ] Label filter works correctly

### Filtering & Search
- [ ] Can filter by status (All, Pending, Completed)
- [ ] Status filter works correctly
- [ ] Can combine status and label filters
- [ ] Filters update task list immediately
- [ ] "No tasks" message shows when filtered list is empty

### UI/UX
- [ ] Login page loads and looks good
- [ ] Signup page loads and looks good
- [ ] Dashboard is well-designed and intuitive
- [ ] Task cards are visually appealing
- [ ] Modal is properly styled
- [ ] Buttons have hover states
- [ ] Loading states show for async operations
- [ ] Toast notifications appear for actions
- [ ] Success messages are green
- [ ] Error messages are red
- [ ] Forms validate input
- [ ] Required fields are marked

### Responsive Design
- [ ] Test on desktop (1920x1080)
- [ ] Test on laptop (1366x768)
- [ ] Test on tablet (768x1024)
- [ ] Test on mobile (375x667)
- [ ] All elements scale appropriately
- [ ] No horizontal scrolling
- [ ] Touch targets are adequate on mobile
- [ ] Text is readable on all screen sizes

### Error Handling
- [ ] Network errors show user-friendly messages
- [ ] Invalid form data shows validation errors
- [ ] 404 errors are handled
- [ ] Authentication errors redirect to login
- [ ] Server errors show helpful messages
- [ ] Failed operations don't crash the app

## API Endpoint Verification

Test these using the Swagger UI at http://localhost:8000/docs

### Auth Endpoints
- [ ] POST `/api/auth/signup` - Creates new user
- [ ] POST `/api/auth/login` - Returns JWT token
- [ ] POST `/api/auth/logout` - Returns success message

### User Endpoints
- [ ] GET `/api/users/me` - Returns current user (requires auth)
- [ ] PUT `/api/users/me` - Updates user profile (requires auth)

### Task Endpoints
- [ ] GET `/api/tasks` - Returns user's tasks (requires auth)
- [ ] GET `/api/tasks?label=Work` - Filters by label
- [ ] GET `/api/tasks?completed=true` - Filters by completion
- [ ] POST `/api/tasks` - Creates new task (requires auth)
- [ ] GET `/api/tasks/{id}` - Returns specific task (requires auth)
- [ ] PUT `/api/tasks/{id}` - Updates task (requires auth)
- [ ] DELETE `/api/tasks/{id}` - Deletes task (requires auth)

### Label Endpoints
- [ ] GET `/api/labels` - Returns user's labels (requires auth)
- [ ] POST `/api/labels` - Creates new label (requires auth)
- [ ] GET `/api/labels/{id}` - Returns specific label (requires auth)
- [ ] PUT `/api/labels/{id}` - Updates label (requires auth)
- [ ] DELETE `/api/labels/{id}` - Deletes label (requires auth)

## Database Verification

Use MongoDB Compass or mongosh to verify:

- [ ] Database `todo_app` exists
- [ ] Collection `users` has documents
- [ ] User passwords are hashed (not plain text)
- [ ] Collection `tasks` has documents
- [ ] Tasks have all required fields
- [ ] Collection `labels` has documents
- [ ] Indexes are created:
  - [ ] users.email (unique)
  - [ ] tasks.user_id
  - [ ] labels.user_id

## Security Verification

- [ ] Passwords are hashed in database
- [ ] JWT tokens expire after configured time
- [ ] Cannot access other users' tasks
- [ ] Cannot access other users' labels
- [ ] Protected endpoints require authentication
- [ ] Invalid tokens are rejected
- [ ] CORS is configured correctly

## Code Quality Verification

### Backend
- [ ] No syntax errors
- [ ] All imports work
- [ ] No unused imports
- [ ] Consistent code style
- [ ] Functions have clear purpose
- [ ] Models are properly defined
- [ ] Error handling is present

### Frontend
- [ ] No TypeScript errors
- [ ] No console errors
- [ ] No unused variables
- [ ] Consistent code style
- [ ] Components are reusable
- [ ] Types are properly defined
- [ ] No memory leaks (check DevTools)

## Documentation Verification

- [ ] README.md is complete
- [ ] README has project description
- [ ] README has setup instructions
- [ ] README has technology list
- [ ] README has features list
- [ ] README has API documentation
- [ ] README has database schema
- [ ] README has project structure
- [ ] SETUP_GUIDE.md is clear and helpful
- [ ] PROJECT_SUMMARY.md covers all aspects
- [ ] Code comments explain complex logic

## Submission Checklist

- [ ] GitHub repository is public
- [ ] All code is committed
- [ ] Commit messages are descriptive
- [ ] .gitignore excludes sensitive files
- [ ] No `.env` files in repository
- [ ] README is the first thing visible
- [ ] Repository URL is submitted
- [ ] Demo video is recorded (if required)
- [ ] Demo video shows all features
- [ ] Demo video is uploaded to YouTube (unlisted)
- [ ] Video link is submitted

## Final Testing Workflow

1. **Fresh Start Test**
   - [ ] Stop all servers
   - [ ] Delete MongoDB data
   - [ ] Delete `venv` and `node_modules`
   - [ ] Follow setup instructions from scratch
   - [ ] Verify everything works

2. **User Journey Test**
   - [ ] Sign up as new user
   - [ ] Verify default labels exist
   - [ ] Create 5 different tasks
   - [ ] Edit 2 tasks
   - [ ] Complete 2 tasks
   - [ ] Delete 1 task
   - [ ] Filter by label
   - [ ] Filter by status
   - [ ] Logout
   - [ ] Login again
   - [ ] Verify data persists

3. **Error Scenario Test**
   - [ ] Try invalid email format
   - [ ] Try short password
   - [ ] Try duplicate email
   - [ ] Try wrong password
   - [ ] Try accessing dashboard without login
   - [ ] Try creating task with missing title
   - [ ] Verify all show appropriate errors

## Performance Check

- [ ] Backend responds quickly (<100ms for most requests)
- [ ] Frontend loads quickly (<2s initial load)
- [ ] No lag when typing in forms
- [ ] Task list updates smoothly
- [ ] No janky animations
- [ ] MongoDB queries are efficient

## Browser Compatibility

Test in multiple browsers:
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari (if on macOS)

## Ready for Submission?

If all checkboxes are checked, your project is ready for submission! 🎉

### Final Steps:
1. Commit all changes
2. Push to GitHub
3. Verify repository is public
4. Submit repository URL
5. Record and submit demo video (if required)
6. Prepare for code review

Good luck! 🚀







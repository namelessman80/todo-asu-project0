Project Overview (Deadline: 10/13/2025)
Students will build a full-stack TODO application with user authentication, tasks, and labels. The backend will be a RESTful API built with Python's FastAPI with Beanie for ODM, and the frontend will be a Next.js application. The application will use MongoDB for data persistence. This project is designed to provide hands-on experience with modern web development tools and best practices.

Required Features (Core User Stories)
These are the essential features that must be completed for a passing grade.

User Management
As a user, I want to sign up for an account, so I can have my own personal task list.
As a user, I want to log in, so I can access my tasks and manage my profile.
As a user, I want to securely log out, so my data is protected from others.
Task Management
As a user, I want to create a new task, so I can add things I need to do to my list.
As a user, I want to view all my tasks, so I can see everything I need to get done.
As a user, I want to update a task's details, so I can change its title, description, or status (e.g., incomplete to complete).
As a user, I want to delete a task, so I can remove completed or irrelevant items from my list.
Required Task Fields: Every task must include a title, an optional description, a priority level (e.g., High, Medium, Low), and a deadline (date).
Labeling System
As a user, I want to create and manage labels (e.g., 'Work,' 'Personal,' 'Urgent'), so I can categorize and/or prioritize my tasks.
As a user, I want to assign one or more labels to a task, so I can easily filter and organize my tasks.
Data Persistence
The application must persist all user, task, and label data in a MongoDB database.
Stretch Goals as User Stories
These features are not required but will demonstrate advanced understanding and improve the user experience.

As a user, I want to filter my tasks by label, so I can quickly find and organize what I need to work on.
As a user, I want to be able to edit my profile details, so I can keep my information up to date.
As a user, I want the application to be responsive and work well on different screen sizes, so I can access my tasks from any device, including my phone or tablet.
As a user, I want to see clear, helpful messages when something goes wrong, so I know what happened and how to proceed.
Technical Requirements & File Structure
Students must adhere to these technical and structural guidelines.

Database: MongoDB
The project should leverage a MongoDB database filled with appropriately modeled documents & collections. Please reference this document on the MongoDB guidelines for embeding vs referencing information in a document

*This is my MongoDB connection string. You can save this to .env file. 
mongodb+srv://db_user1:XM4Q2jcOShpjAUHG@cluster0.faxo8fl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

*This is my MongoDB cluster info. I access them through MongoDB Compass
cluster0.faxo8fl.mongodb.net


Guideline Name	Question	Embed	Reference
Simplicity	Would keeping the pieces of information together lead to a simpler data model and code?	Yes	No
Go Together	Do the pieces of information have a "has-a," "contains," or similar relationship?	Yes	No
Query Atomicity	Does the application query the pieces of information together?	Yes	No
Update Complexity	Are the pieces of information updated together?	Yes	No
Archival	Should the pieces of information be archived at the same time?	Yes	No
Cardinality	Is there a high cardinality (current or growing) in the child side of the relationship?	No	Yes
Data Duplication	Would data duplication be too complicated to manage and undesired?	No	Yes
Document Size	Would the combined size of the pieces of information take too much memory or transfer bandwidth for the application?	No	Yes
Document Growth	Would the embedded piece grow without bound?	No	Yes
Workload	Are the pieces of information written at different times in a write-heavy workload?	No	Yes
Individuality	For the children side of the relationship, can the pieces exist by themselves without a parent?	No	Yes



Backend: FastAPI
The project directory should follow a clean, modular structure. Refer to these resources for examples:

Simplified FastAPI structure
Detailed FastAPI best practices
Frontend: Next.js
The project structure should follow best practices for a Next.js application. Refer to these resources for examples:

Simplified Next.js structure
Detailed Next.js best practices
Students must pick one UI library from this list for component styling.

Git & GitHub
Students must create a public GitHub repository for their project.
The repository URL should be submitted on Day 1 to an Excel document that will be created for the cohort.
Students are expected to make daily commits with clear, descriptive commit messages. This will be a key part of the evaluation, as it demonstrates consistent progress and version control proficiency.
They must also create a README.md file that includes:
A brief description of the project.
Instructions on how to set up and run the application.
A list of technologies used.
A list of completed features (and stretch goals, if any).
Project Expectations & Code Integrity
While you are welcome to "vibe code" and explore your creativity, all students will be held accountable for their work.

Code Review: Each student will undergo a single mandatory code review with trainer or TA prior to the project's completion. This will be scheduled via a sign-up sheet and is meant to facilitate a deeper understanding of the codebase.
Best Practices: You are expected to follow best practices for code readability, modularity, and maintainability.
Code Accountability: You must be prepared to answer questions and explain the purpose of any line of your code.
Submission & Evaluation
Submission: Students will submit a link to their GitHub repository and their project demo video via the provided Excel document here.

The project demo video must be uploaded as an unlisted YouTube video, with the link shared in the submission spreadsheet. Step-by-Step Guide to Record & Upload Unlisted Video
Evaluation: The project will be evaluated based on a separate rubric.
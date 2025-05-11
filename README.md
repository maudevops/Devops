🚀 Flask + React + MongoDB – Manual Docker Setup Task In this task, you’ll learn how to set up a full-stack web application using Flask, React, and MongoDB, by manually creating Docker containers for each part — without using Docker Compose.

The app is divided into 3 parts:

🗃️ MongoDB (Database)

🐍 Flask (Backend)

⚛️ React (Frontend)

You will run each of these in its own Docker container.

🛠️ Step 1: Clone the Repository Start by cloning the project code.

bash Copy Edit git clone Project folders:

backend/ — Flask app code

frontend/ — React app code

🗄️ Step 2: Set Up MongoDB Container Create a Docker container for MongoDB using an official MongoDB image.

Make sure the database is:

Running

Listening on port 27017

Named something you can reference later (e.g., mongo-container)

This container should be started first, since your backend depends on it.

⚙️ Step 3: Update the .env Files After MongoDB is running, update the .env files to make sure the app components can talk to each other.

Why? .env files define the URLs and settings each part of your app uses. If they are incorrect, the components won’t connect properly.

🔧 Backend .env Location: backend/.env

Update the MongoDB connection string and backend port, like:

MONGO_URI=...

FLASK_APP_PORT=5000

Hint: use your MongoDB container’s name as the host in the URI.

🔧 Frontend .env Location: frontend/.env

Update the backend API URL and the port the frontend will use:

VITE_API_URL=http://:5000

Set the frontend to run on port 3000

🐍 Step 4: Containerize and Run Flask Backend Go to the backend/ folder.

Your task:

Write a Dockerfile for the Flask app

Build the Docker image

Run the container with correct .env settings

The backend must be able to connect to the MongoDB container using the info from .env.

⚛️ Step 5: Containerize and Run React Frontend Go to the frontend/ folder.

Your task:

Write a Dockerfile for the React app

Build the Docker image

Run the container and expose it on port 3000

The frontend should use the API URL from .env to reach the backend.

✅ Step 6: Test Everything Once all containers are up:

Open your browser and go to: http://localhost:3000

Try to create, update, and delete users from the UI.

Make sure:

Frontend talks to backend

Backend talks to MongoDB

🔄 Summary Component What to do MongoDB Run first, standalone container Flask Build and run after MongoDB is ready React Build and run after backend is running .env files Update for both backend and frontend




⚠️ Note: Missing .env Files
If you do not see a .env file in the following directories:

backend/

frontend/

You must create them manually before running the application.

🔧 Backend .env file should contain:

DB_NAME=your_database_name
DB_HOST=mongo-container-name
DB_PORT=27017
MONGO_USERNAME=your_mongo_user_if_any
MONGO_PASSWORD=your_mongo_password_if_any
🔧 Frontend .env file should contain:

VITE_API_URL=http://backend-container-name:5000
💡 Replace container names and credentials based on your setup








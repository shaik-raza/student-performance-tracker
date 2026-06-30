Student Performance Tracker

A web app for storing student marks and automatically calculating results, built with Flask and a MySQL backend.

Overview

This project lets you record student marks for different subjects, store them in a MySQL database, and view calculated results (such as totals, averages, or pass/fail status) through a simple web interface.

Tech Stack


Backend: Flask (Python)
Database: MySQL, hosted on Railway
Frontend: HTML, CSS (with a dark glassmorphism UI)
Deployment: Vercel


Features


Add and store student marks across subjects
Automatically calculates results (totals/averages) from stored marks
Clean, responsive frontend with custom styling
Cloud-hosted MySQL database for persistent storage


Project Structure

student-performance-tracker/
├── app.py                  # Flask backend and routes
├── db.py                   # Database connection logic
├── marks.py                # Marks handling / calculation logic
├── student_tracker.sql     # Database schema
├── requirements.txt        # Python dependencies
├── vercel.json              # Deployment config
├── static/
│   └── CSS/                 # Stylesheets
├── templates/
│   ├── index.html
│   └── result.html

Running Locally


Install dependencies:


bashpip install -r requirements.txt


Set up your database connection in a .env file:


DB_HOST=your_host
DB_PORT=your_port
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database

Run the app:


bashpython app.py

Then open http://127.0.0.1:5000 in your browser.

Database

The database schema is defined in student_tracker.sql. Hosted on Railway for cloud accessibility, allowing the app to read and write student data from anywhere.

Author

Shaik Raza

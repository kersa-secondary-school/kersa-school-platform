# # Kersa Secondary School Platform

Full‑stack web application for Kersa Secondary School.

## Features
- Public website with announcements, gallery, resources
- Student registration
- Teacher‑student messaging
- Admin dashboard
- AI tutor (optional API)

## Tech Stack
- Frontend: HTML, CSS, JavaScript, React (later)
- Backend: Django REST Framework
- Database: SQLite (development), PostgreSQL (production)

## Setup (Backend)
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Setup (Frontend)
cd frontend
npm install
npm run dev
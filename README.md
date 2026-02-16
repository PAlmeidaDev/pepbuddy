PepBuddy: Advanced Medication Tracker

PepBuddy is a full-stack health-tech application designed to manage complex medication schedules. 
Unlike standard pill reminders, PepBuddy is built to handle non-traditional intervals (e.g., 96-hour cycles) often required for specialized treatments and peptides.

##  Key Features
* **Dynamic Scheduling Engine:** Automatically calculates the next dose time based on custom intervals (Daily, 48-hour, 96-hour, etc.).
* **Inventory Management:** Real-time stock tracking that decrements automatically when a dose is logged.
* **RESTful Architecture:** A decoupled Django backend serving a React frontend, allowing for a fast, "app-like" user experience.
* **Action Tracking:** Custom API endpoints to log doses with a single click, updating both timing and stock levels simultaneously.

## Stack
* **Frontend:** React.js (Vite), Tailwind CSS
* **Backend:** Python, Django REST Framework (DRF)
* **Database:** PostgreSQL / SQLite
* **Environment:** Node.js (Frontend Tooling)



##  Technical Challenges Solved
* **Custom Business Logic:** Implemented a backend system that uses `timezone` aware datetime math to ensure dose accuracy across different global time zones.
* **CORS Configuration:** Handled Cross-Origin Resource Sharing to allow secure communication between the React frontend and Django backend.
* **User Ownership:** Built a data model where medications are securely tied to specific user profiles.

## 🏁 Getting Started

### Backend Setup
1. `cd backend`
2. `python -m venv .venv`
3. `source .venv/bin/activate` (or `.venv\Scripts\activate` on Windows)
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py runserver`

### Frontend Setup
1. `cd frontend`
2. `npm install`
3. `npm run dev`

---
*Developed as a personal project to showcase Full-Stack capabilities in Python and JavaScript.*
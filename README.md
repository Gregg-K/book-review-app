# Book Review Management System

## Overview

The Book Review Management System is a full-stack web application built with React and Flask. The system allows users to register, log in, manage books, write reviews, and organize books into categories.

This project demonstrates the use of React for the frontend, Flask for the backend, SQLAlchemy for database management, and JWT for authentication.

---

## Features

### Authentication

* User Registration
* User Login
* User Logout
* JWT Authentication
* Protected Routes

### Book Management

* Add Books
* View Books
* Update Books
* Delete Books

### Review Management

* Create Reviews
* View Reviews
* Update Reviews
* Delete Reviews

### Category Management

* Organize Books into Categories
* View Books by Category

---

## Technologies Used

### Frontend

* React
* React Router DOM
* Fetch API

### Backend

* Flask
* Flask SQLAlchemy
* Flask Migrate
* Flask JWT Extended
* Flask CORS

### Database

* SQLite

---

## Database Relationships

### One-to-Many

* One User can create many Books
* One User can write many Reviews

### Many-to-Many

* Many Books can belong to many Categories
* One Category can contain many Books

---

## Project Structure

```text
book-review-app/
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── seed.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── context/
│   │   └── App.jsx
│   └── package.json
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd book-review-app
```

### Backend Setup

```bash
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
DATABASE_URL=sqlite:///book_review.db
JWT_SECRET_KEY=your-secret-key
```

Run database migrations:

```bash
flask db upgrade
```

Start Flask server:

```bash
flask run
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

The frontend will run on:

```text
http://localhost:5173
```

---

## API Endpoints

### Authentication

```http
POST /register
POST /login
GET /profile
```

### Books

```http
GET /books
POST /books
GET /books/<id>
PATCH /books/<id>
DELETE /books/<id>
```

### Reviews

```http
GET /reviews
POST /reviews
PATCH /reviews/<id>
DELETE /reviews/<id>
```

---

## Future Improvements

* Book search functionality
* User profile management
* Review ratings and likes
* Advanced filtering by category
* Responsive UI improvements

---

## Author

Gregory Kip

Moringa School Full Stack Development Project

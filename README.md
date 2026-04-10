# 🎓 Student-Teacher Appointment Booking System

A full-stack web application that allows students to book appointments with teachers and manage scheduling efficiently.

---

## 🚀 Features

### 👩‍🎓 Student
- Login securely
- View available slots
- Book appointments
- View appointment status (Pending / Approved / Rejected)

### 👩‍🏫 Teacher
- Add availability slots
- View student booking requests
- Approve / Reject appointments
- Add remarks

---

## 🛠️ Tech Stack

### Frontend
- React.js
- HTML, CSS
- JavaScript

### Backend
- Flask (Python)
- REST API

### Database
- SQLite

---

## 📂 Project Structure
student-teacher-booking/
│
├── backend/
│ ├── routes/
│ ├── models.py
│ ├── app.py
│
├── frontend/
│ ├── src/
│ ├── components/
│ ├── pages/
│
└── README.md


---

## ⚙️ Installation & Setup

### 🔹 Backend

-cd backend
- pip install -r requirements.txt
- python app.py

### Frontend
- cd frontend
- npm install
- npm start

  🌐 API Endpoints
Student
GET /student/available-slots

POST /student/book

GET /student/my-appointments/<id>

Teacher
POST /teacher/add-availability

GET /teacher/appointments/<id>

POST /teacher/update-status

 Future Improvements
- Notifications system
- Calendar integration
- Email alerts
- UI enhancements

👩‍💻 Author
- Sirisha
- IT Student | Full Stack Developer

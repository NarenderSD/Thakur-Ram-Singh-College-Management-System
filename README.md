<p align="center">
  <img src="student_management_app/static/branding/CollegeLogo.png" alt="TRSC College Logo" width="180"/>
</p>

<h1 align="center">Thakur Ram Singh College (TRSC) - College Management System</h1>

<p align="center">
  <strong>A premium, modern, and fully-featured student management portal designed for TRSC College, Sankhi.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Django-3.2%2B-green.svg" alt="Django Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/UI/UX-Premium-orange" alt="UI/UX">
</p>

---

## ✨ Key Features

- **Modern Animated UI**: Glassmorphism cards, smooth animations, and a professional design.
- **Full TRSC Branding**: Consistent logo and branding across all pages.
- **Role-Based Dashboards**: Unique dashboards for HOD, Staff, and Students.
- **Contact & Feedback System**: Public contact form, HOD inbox, and feedback for staff/students.
- **Attendance & Result Management**: For staff and students.
- **Leave Management**: Apply and manage leaves for staff and students.
- **Secure Authentication**: Email-based role detection and password hashing.
- **Responsive Design**: Works on desktop, tablet, and mobile.

---

## 🛠️ Tech Stack

| Category      | Technology                                                                                 |
|---------------|--------------------------------------------------------------------------------------------|
| **Backend**   | Python 3.8+, Django 3.2+                                                                  |
| **Frontend**  | HTML5, CSS3, JavaScript, Bootstrap, jQuery                                                |
| **UI/UX**     | Animate.css, FontAwesome, Google Fonts, Glassmorphism UI                                  |
| **Database**  | SQLite (development)                                                                      |

---

## 🚀 Setup & Installation

**1. Prerequisites:**
- Python 3.8+
- `pip` package manager

**2. Clone the Repository:**
```bash
git clone https://github.com/your-username/college-management-system.git
cd college-management-system
```

**3. Create and Activate a Virtual Environment:**
- **Windows:**
  ```bash
  python -m venv env
  .\env\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

**4. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**5. Run Database Migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Run the Development Server:**
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

## 📖 Usage Guide

- **Registration:** Use your college email (e.g., `yourname.hod@trsc.edu.in`, `yourname.staff@trsc.edu.in`, `yourname.student@trsc.edu.in`).
- **Login:** Use your registered email and password.
- **Dashboards:**
  - HOD: Manage staff, students, courses, subjects, view contact messages, etc.
  - Staff: Take attendance, manage results, feedback, leave, etc.
  - Student: View attendance, results, apply for leave, send feedback, etc.
- **Contact Form:** Public users can send queries via the contact page; HOD can view all messages in their dashboard.

---

## 📸 Screenshots

> _Add screenshots of the login page, dashboards, and contact messages inbox here for a more premium look._

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/college-management-system/issues).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ by <b>Narender Singh</b> for <b>Thakur Ram Singh College (TRSC)</b>
</p> 

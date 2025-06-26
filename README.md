# Thakur Ram Singh College (TRSC) - Student Management System

<p align="center">
  <img src="httpsa://github.com/user-attachments/assets/b21584c6-2580-4960-8488-29408b0f9f1b" alt="TRSC Logo" width="150"/>
</p>

<p align="center">
  <strong>A premium, modern, and fully-featured student management portal designed to streamline college administration and enhance the student experience.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Django-3.2%2B-green.svg" alt="Django Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/UI/UX-Premium-orange" alt="UI/UX">
</p>

---

## ✨ Key Features

This portal is built with a role-based workflow for HOD, Staff, and Students, providing each with a unique, feature-rich dashboard.

### 💎 General & UI/UX
- **Modern Animated UI**: Glassmorphism cards, smooth animations, and a professional design.
- **Full TRSC Branding**: Consistent logo and branding across all pages.
- **Fully Responsive**: Works seamlessly on desktops, tablets, and mobile devices.
- **Secure Authentication**: Robust login and registration system with email-based role detection.

### 👑 HOD Dashboard
- **User Management**: Add, view, and manage all Staff and Students.
- **Course & Subject Management**: Easily create and manage courses and subjects.
- **View Contact Queries**: A dedicated page to view and manage all messages from the contact form.
- **Centralized Dashboard**: At-a-glance view of all users with interactive cards.

### 👨‍🏫 Staff Dashboard
- **Attendance Management**: Take and update student attendance efficiently.
- **Result Management**: Add and view student results.
- **Leave Management**: View and manage student leave applications.
- **Feedback System**: Send and receive feedback.
- **Interactive Dashboard**: Animated cards for key metrics.

### 🎓 Student Dashboard
- **Personalized Dashboard**: Quick links and animated cards for key actions.
- **View Attendance & Results**: Easily track academic progress.
- **Apply for Leave**: A simple and intuitive leave application process.
- **Send Feedback**: Communicate directly with staff and administration.

---

## 🛠️ Tech Stack

This project is built with a modern and robust technology stack:

| Category      | Technology                                                                                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Backend**   | <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" /> |
| **Frontend**  | <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" /> |
| **UI Framework** | <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" /> <img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white" /> |
| **Database**  | <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" /> (for development)                                                 |
| **Design & Icons** | Animate.css, FontAwesome, Google Fonts, Glassmorphism UI                                                                                                               |

---

## 🚀 Setup & Installation

Follow these steps to get the project running locally:

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

**1. Registration:**
- Navigate to the **Register** page.
- Your role (HOD, Staff, Student) is automatically determined by your email format:
  - **HOD**: `yourname.hod@trsc.edu.in`
  - **Staff**: `yourname.staff@trsc.edu.in`
  - **Student**: `yourname.student@trsc.edu.in`

**2. Login:**
- Use your registered email and password to log in. You will be redirected to your respective dashboard.

**3. Explore Your Dashboard:**
- Each dashboard is tailored to the user's role, providing access to relevant features and information.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/college-management-system/issues).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ by <b>Narender Singh</b>
</p> 
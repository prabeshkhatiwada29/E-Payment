# E-Payment
# 💸 E-Payment System

A full-stack Django-based **E-Payment System** built for managing book sales with integrated eSewa payment gateway, PostgreSQL database, and a customized admin panel powered by Jazzmin.

![Django](https://img.shields.io/badge/Backend-Django-green)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![eSewa](https://img.shields.io/badge/Payment-eSewa-yellow)
![Jazzmin](https://img.shields.io/badge/Admin-Jazzmin-orange)

---

## 🚀 Features

- 📚 Book Management System (CRUD)
- 🧾 Secure eSewa Payment Gateway Integration
- 👨‍💼 Admin Dashboard with Jazzmin
- 🛠️ Custom Styling with HTML/CSS/JavaScript
- 🌐 Responsive Web UI
- 🔐 Environment-friendly with `.env` support

---

## 🛠 Tech Stack

| Layer         | Technology               |
|---------------|---------------------------|
| Backend       | Django (Python)           |
| Frontend      | HTML, CSS, JavaScript     |
| Database      | PostgreSQL                |
| Payment       | eSewa API (RC Test Mode)  |
| Admin Panel   | Jazzmin                   |

---

## 🧑‍💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/prabeshkhatiwada29/E-Payment.git
cd E-Payment


python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows


pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser


python manage.py runserver

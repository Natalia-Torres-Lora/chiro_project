# 🏥 Chiro Care – Chiropractor Patient Management System

**Chiro Care** is a Django-based web application designed to help chiropractic clinics efficiently manage patients, appointments, treatments, and documentation. This project is built with Django REST Framework, PostgreSQL, Docker, and deployed on AWS—demonstrating real-world backend engineering skills in a healthcare context.

> **Final Project for Certification: NuCamp Backend, SQL and DevOps with Python Bootcamp**

---

## 🚀 Features

- **User Authentication & Role-Based Access**
  - **Chiropractors:** Full access to patient and treatment records
  - **Patients:** View-only access to their own records and appointments
- **Patient Management:** Chiropractors can create, read, update, and delete patient records
- **Appointment Scheduling:** Smart scheduling with conflict detection
- **Treatment Management:** Track and link treatments to patients and appointments
- **Private Notes:** Chiropractor-only notes for each treatment session
- **Admin Dashboard:** Full data access and control via Django Admin interface

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Authentication:** Django built-in with custom permissions
- **Deployment:** AWS (EC2, RDS, optional S3)
- **CI/CD:** GitHub + AWS (optional)

---

## 📁 Project Structure

```
chiro_project/
├── chiro_project/         # Project settings and URLs
├── app/               # Main application logic (models, views, etc.)
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🐳 Local Development (Docker)

```bash
# Clone the repository
git clone https://github.com/Natalia-Torres-Lora/chiro_project.git
cd chiro_project

# Build and start containers
docker-compose up --build

# Apply migrations
docker-compose exec web python manage.py migrate

# Create a superuser
docker-compose exec web python manage.py createsuperuser
```

---

## 🔗 Sample API Endpoints

| Endpoint               | Method         | Description                          |
|------------------------|---------------|--------------------------------------|
| `/api/login/`          | POST          | User login                           |
| `/api/patients/`       | GET, POST     | List or create patients              |
| `/api/patients/<id>/`  | GET, PUT, DELETE | View, update, or delete a patient |
| `/api/appointments/`   | GET, POST     | View or schedule appointments        |
| `/api/treatments/`     | GET, POST     | View or record treatments            |


---

## 🌐 Deployment on AWS

This project is deployed using:

- **EC2** for Django app
- **RDS** for PostgreSQL database
- **S3** (optional) for media/static file storage
- **Elastic Beanstalk** or Docker on EC2 for hosting
- Environment variables managed via EC2 or EB configuration

---

## 🔐 Environment Variables (`.env` example)

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost 127.0.0.1
DATABASE_NAME=chiro_project_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```

---
<!-- 
## 📸 Screenshots

*(Add screenshots here if available)* -->

---

## ✅ Future Improvements

- Email notifications for appointments
- Patient self-registration
- API pagination & filtering
- Unit and integration testing
- Swagger/OpenAPI docs

---

## ✍️ Author

Natalia Torres Lora  
Backend Developer | NuCamp Graduate

[LinkedIn](https://www.linkedin.com/in/natalia-torres-lora/)  
[GitHub](https://github.com/Natalia-Torres-Lora)

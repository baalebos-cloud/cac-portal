CAC Portal – Business Registration & Compliance Automation Platform
                                                 Overview
CAC Portal is a production-ready web application designed to automate Corporate Affairs Commission (CAC) registrations and statutory compliance processes in Nigeria. The platform digitizes Business Name registration, Limited Liability Companies, NGO registrations, payments, document uploads, admin approvals, and WhatsApp notifications.
This project demonstrates real-world backend engineering, API integration, database migrations, and cloud deployment using modern DevOps practices.

Key Features

Business Name, Company & NGO registration workflows
Secure file uploads (NIN, signatures, IDs)
Admin dashboard for approvals and status updates
Payment tracking with status lifecycle (Pending → Processing → Completed)
WhatsApp Cloud API notifications
JWT authentication and role-based access
Database migrations with Flask-Migrate
Cloud-ready deployment on Render


Tech Stack

Backend: Python 3.12, Flask
Database: SQLite (dev), PostgreSQL (prod-ready)
ORM: SQLAlchemy
Auth: Flask-Login, Flask-JWT-Extended
Messaging: WhatsApp Cloud API
Deployment: Render
DevOps: Gunicorn, Environment-based config, Alembic migrations


Project Structure
cac-portal/
│
├── app.py
├── config.py
├── extensions.py
├── routes/
│   ├── business_name.py
│   ├── company.py
│   ├── ngo.py
│   └── admin.py
├── models/
├── templates/
├── static/
├── uploads/
├── migrations/
├── requirements.txt
└── README.md


Setup Instructions
git clone https://github.com/baalebo-cloud/cac-portal.git
cd cac-portal
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Environment Variables
SECRET_KEY
JWT_SECRET_KEY
DATABASE_URL
WHATSAPP_TOKEN
WHATSAPP_PHONE_NUMBER_ID
MAIL_USERNAME
MAIL_PASSWORD

Database Migration
flask db upgrade

Run Locally
flask run


Deployment
The application is fully deployable on Render using Gunicorn with environment-based configuration.

Use Case
Ideal for:

CAC agents & compliance consultants
SMEs and startups
Digital governance platforms
Enterprise registration automation


License
MIT License


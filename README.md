
# Anbuild Integrated Project Control System (AIPCS)

AIPCS is a full-stack construction project management platform tailored for contractors in Uganda. It integrates cost tracking, time management, scope control, and real-time reporting.


## 🚀 Features

- Project setup and BOQ management
- Real-time cost and expense tracking
- Schedule and milestone monitoring
- Scope variation logging and analysis
- GIS and Geo-tagged Photo Gallery
- Daily Site Diary Logging
- Procurement and Inventory Modules
- Role-Based Access Control
- CI/CD and Dockerized Deployment
- Role-based dashboards and KPIs
- Exportable reports (PDF, Excel)

## 🧱 Technology Stack

| Layer     | Stack                       |
|-----------|-----------------------------|
| Frontend  | React JS, Tailwind CSS      |
| Backend   | Node.js (Express) or Django |
| Database  | PostgreSQL                  |
| Auth      | JWT                         |
| CI/CD     | GitHub Actions              |
Backend: FastAPI (Python)
- Database: PostgreSQL
- Deployment: Railway + Netlify
- CI/CD: GitHub Actions + DockerBackend: FastAPI (Python)
- Database: PostgreSQL
- Deployment: Railway + Netlify
- CI/CD: GitHub Actions + Docker

## 📦 Folder Structure

```
aipcs/
├── client/        # React frontend
├── server/        # Backend API
├── database/      # SQL and migration scripts
├── docs/          # Documentation
├── tests/         # Unit, integration, performance tests
└── .github/       # CI workflows
```

## ⚙️ Local Setup

```bash
git clone https://github.com/collebankunda/aipcs.git
cd aipcs

# Frontend
cd client
npm install
npm run dev

# Backend
cd ../server
pip install -r requirements.txt
python manage.py runserver
```

## 🧪 Running Tests

```bash
# Frontend
npm run test

# Backend
pytest
```
## Getting Started

1. Clone the repository
2. Copy `.env.example` to `.env`
3. Set up PostgreSQL and run migrations
4. Run backend: `uvicorn main:app --reload`
5. Run frontend: `npm run dev`

## 📄 License

MIT License. Created by anbuild, 2025.

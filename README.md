
# Armpass Integrated Project Control System (AIPCS)

A centralized web-based platform for managing and tracking cost, time, and scope across all Armpass Technical Services Ltd construction projects.

## 🚀 Features

- Project setup and BOQ management
- Real-time cost and expense tracking
- Schedule and milestone monitoring
- Scope variation logging and analysis
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
git clone https://github.com/armpass/aipcs.git
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

## 📄 License

MIT License. Created by Armpass Technical Services Ltd, 2025.

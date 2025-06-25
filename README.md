# Anbuild Integrated Project Control System (AIPCS)

AIPCS is a full-stack construction project management platform tailored for contractors in Uganda. It integrates cost tracking, time management, scope control, and real-time reporting.

## Features

- Project Setup & Assignment
- Budgeting and Cost Tracking
- Schedule Monitoring (Gantt, SPI)
- Variation and Scope Management
- GIS and Geo-tagged Photo Gallery
- Daily Site Diary Logging
- Procurement and Inventory Modules
- Role-Based Access Control
- CI/CD and Dockerized Deployment

## Technologies Used

- Frontend: React + Tailwind CSS
- Backend: FastAPI (Python)
- Database: PostgreSQL
- Deployment: Railway + Netlify
- CI/CD: GitHub Actions + Docker

## Getting Started

1. Clone the repository
2. Copy `.env.example` to `.env`
3. Set up PostgreSQL and run migrations
4. Run backend: `uvicorn main:app --reload`
5. Run frontend: `npm run dev`

## License

© 2025 Anbuild

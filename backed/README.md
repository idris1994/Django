# Minimal E-commerce App (Django REST + React)

A simplified e-commerce platform with a Django REST API backend and a React frontend, Dockerized for easy setup.

## Features (intended)
- JWT auth (DRF + SimpleJWT)
- Products, Categories
- Cart (add/update/remove)
- Orders + order history
- Admin product/category management (custom views, not Django admin)
- Checkout + Stripe (or mock) payment intent
- Celery task to send order confirmation email
- Unit tests (pytest/DRF tests)
- PDF receipt (bonus)

## Repo Structure
```
backend/     # Django project
frontend/    # React app (Vite or CRA)
docker-compose.yml
Dockerfile
.env.example
```
> Note: This scaffold includes Docker & env templates. Integrate with your code under `backend/`.

## Quick Start (Docker)
1. Copy `.env.example` to `.env` and adjust values.
2. Put your Django project under `backend/` (or update `Dockerfile` paths).
3. Build & run:
   ```bash
   docker compose up --build
   ```
4. API available at `http://localhost:8000/`
5. Optional React dev server at `http://localhost:3000/`

## Manual Setup (Backend)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export $(grep -v '^#' .env | xargs)  # or set variables manually
python manage.py migrate
python manage.py runserver
```

## API Docs
- `drf-spectacular` schema at `/api/schema/`
- Swagger UI at `/api/docs/`

## Tests
```bash
pytest -q
```

## Postman
- Import `postman_collection.json` (add one if available).
```


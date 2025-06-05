# FastAPI ML Service

A production-ready FastAPI application for serving machine learning models, featuring a real-time dashboard and internal tools.

## Features

- 🚀 FastAPI-based REST API with automatic OpenAPI documentation
- 🔒 JWT-based authentication and role-based access control
- 📊 Real-time dashboard with WebSocket support
- 🤖 ML model serving with background task processing
- 💾 PostgreSQL database with SQLModel ORM
- 🔄 Redis for caching and task queue
- 📈 Prometheus metrics and structured logging
- 🧪 Comprehensive test suite with pytest
- 🎨 Modern development tools (black, isort, mypy)

## Requirements

- Python 3.9+
- PostgreSQL
- Redis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-ml-service.git
cd fastapi-ml-service
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e ".[dev]"
```

4. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

5. Update the `.env` file with your configuration.

## Development

1. Start the development server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation at http://localhost:8000/docs

3. Run tests:
```bash
pytest
```

4. Format code:
```bash
black .
isort .
```

5. Type checking:
```bash
mypy .
```

## Project Structure

```bash
my_fastapi_ml_project/
├── app/
│   ├── __init__.py
│   ├── main.py                # Application entry point (FastAPI app, events, middleware, routers)
│   ├── api/                   # API package (routers, dependencies, versioning)
│   │   ├── __init__.py
│   │   ├── dependencies.py    # Reusable dependency functions (e.g., get_db, auth handlers)
│   │   └── routers/           # Modular route definitions
│   │       ├── __init__.py
│   │       ├── auth.py        # Auth & token endpoints (login, signup, refresh)
│   │       ├── users.py       # User management endpoints
│   │       ├── ml_model.py    # ML model serving endpoints (prediction, status)
│   │       ├── dashboard.py   # Dashboard endpoints (analytics, SSE/WebSocket streams)
│   │       └── internal.py    # Internal tooling endpoints (admin tasks, etc.)
│   ├── core/                  # Core configuration, security, and app-wide utilities
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration settings (Pydantic BaseSettings for env vars)
│   │   ├── security.py        # Security utils (JWT token creation/validation, password hashing)
│   │   ├── middleware.py      # Custom middleware (e.g., logging, timing, CORS, RBAC enforcement)
│   │   └── rbac.py            # Role-based access control logic (if not in middleware)
│   ├── models/                # ORM database models (SQLModel/SQLAlchemy classes)
│   │   ├── __init__.py
│   │   ├── user.py            # User model (with roles/permissions fields)
│   │   ├── item.py            # Example domain model (if needed for internal tools)
│   │   └── ...
│   ├── schemas/               # Pydantic models for requests and responses
│   │   ├── __init__.py
│   │   ├── user.py            # Pydantic schemas for User (UserCreate, UserRead, etc.)
│   │   ├── ml.py              # Schemas for ML input payloads and prediction results
│   │   └── dashboard.py       # Schemas for dashboard data (if any)
│   ├── db/                    # Database configuration and sessions
│   │   ├── __init__.py
│   │   ├── session.py         # SQLAlchemy/SQLModel session, engine setup (PostgreSQL connection)
│   │   ├── redis.py           # Redis client setup (for caching, task queue)
│   │   └── migrations/        # DB migration scripts (e.g., Alembic)
│   ├── services/              # Business logic, integrations, and long-running tasks
│   │   ├── __init__.py
│   │   ├── ml_service.py      # ML model loading, inference logic (could use BackgroundTasks/Celery)
│   │   ├── dashboard_service.py # Real-time data aggregation for dashboard, WebSocket broadcast logic
│   │   ├── auth_service.py    # User auth helpers (if not using external library)
│   │   ├── external_api.py    # External API client calls (using httpx for async requests)
│   │   └── tasks.py           # Background task functions (e.g., Celery tasks definitions)
│   └── middleware/ (optional) # If multiple middleware components, could be a package
│       ├── __init__.py
│       └── rbac_middleware.py # Example: middleware class enforcing RBAC on requests
├── tests/                     # Test suite for unit and integration tests
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_ml_model.py
│   ├── test_dashboard.py
│   └── ...
├── .env                       # Environment variables for development (never commit secrets)
├── pyproject.toml or requirements.txt  # Project dependencies
├── Dockerfile                 # Containerization configuration (for deployment)
└── README.md                  # Project documentation
```


## License

This project is licensed under the MIT License - see the LICENSE file for details.

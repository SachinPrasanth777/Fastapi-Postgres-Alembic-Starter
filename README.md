<h1 align="center" id="title">FastAPI-PostgresSQL-Alembic-Starter</h1>

## Installation 🔧

Install Dependencies

```
pip install -r requirements.txt
```

Make the Migrations

```
alembic revision --autogenerate -m "your_migration_message"
```

```
alembic upgrade head
```

Start the development server

```
uvicorn app:app --reload --host 0.0.0.0 --port 8080
```

Format the code

```
black format .
```

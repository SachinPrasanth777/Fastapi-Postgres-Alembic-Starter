from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import get_settings

settings = get_settings()

DB_URL = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@localhost:8000/{settings.DB_NAME}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

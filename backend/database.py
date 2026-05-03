from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv() 

DATABASE_URL = os.getenv('DATABASE_URL')

# Fail fast with an explicit error when DATABASE_URL is not provided.
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL environment variable is not set.\n"
        "On Railway: ensure your backend service's Root Directory is 'backend' and that you have added a PostgreSQL plugin/service.\n"
        "Then set the 'DATABASE_URL' variable for the backend service to the provided connection string."
    )

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print("DB URL:", os.getenv("DATABASE_URL"))
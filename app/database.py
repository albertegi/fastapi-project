from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os
import time



SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Regibert@localhost:5432/fastapi'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency: A method that talks to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
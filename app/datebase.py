# Function for creating a connection to a database.
from sqlalchemy import create_engine
# Function to create a base class for models.
from sqlalchemy.ext.declarative import declarative_base
# Function for creating session classes that are used to interact with the database.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from fastapi import Depends



# connection to bd
DATABASE_URL = "sqlite:///./.notes.db"

# connection management
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# create session
# autocommit=False - Disables automatic commit of changes.
# autoflush=False - Disables automatic data refresh in the session.
# bind=engine - Associates sessions with the database engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# class for inheritance
Base = declarative_base()

# function that creates and returns a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class NoteDB(Base):
    # create table name
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(String)
    # date of creation
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # date of update
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
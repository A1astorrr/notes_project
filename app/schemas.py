from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    title: str
    text: str 
    
class Note(NoteCreate):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True # orm-object as pydantic models
    

class NoteUpdate(BaseModel):
    title: str | None = None
    text: str | None = None 
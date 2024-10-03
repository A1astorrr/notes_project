from pydantic import BaseModel
from datetime import datetime

class Note(BaseModel):
    id: int
    title: int
    text: str
    created_at: datetime
    
    
class NoteCreate(BaseModel):
    title: str
    text: str 
    
class NoteUpdate(BaseModel):
    title: str | None = None
    text: str | None = None 
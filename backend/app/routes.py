from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import NoteDB
from .database import get_db
from .schemas import Note, NoteCreate, NoteUpdate

router = APIRouter(prefix="/notes")

#create notes
@router.post("/", response_model=Note)
async def create_notes(note: NoteCreate, db: Session = Depends(get_db)):
    # creating note models
    db_note = NoteDB(**note.dict())
    # adding note in session
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# read notes
@router.get("/", response_model=list[Note])
async def read_notes(db: Session = Depends(get_db)):
    # getting all notes
    notes = db.query(NoteDB).all()
    return notes

#read noted by id
@router.get("/{note_id}/", response_model=Note)
async def read_notes_by_id(note_id: int, db: Session = Depends(get_db)):
    note = db.query(NoteDB).filter(NoteDB.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

#update notes
@router.put("/{note_id}/", response_model=Note)
async def update_notes(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    db_note = db.query(NoteDB).filter(NoteDB.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    for key, value in note.dict(exclude_unset=True).items():
        # update note field
        setattr(db_note, key, value)
    
    db.commit()
    db.refresh(db_note)
    return db_note

#delete notes
@router.delete("/{note_id}/")
async def delete_notes(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(NoteDB).filter(NoteDB.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(db_note)
    db.commit()
    return {"detail": "Note deleted successfully"}
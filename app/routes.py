from fastapi import APIRouter
from .models import Note, NoteCreate, NoteUpdate

router = APIRouter(prefix="/notes")

#create notes
@router.post("/", response_model=Note)
async def create_notes(note: NoteCreate):
    pass

# read notes
@router.get("/", response_model=list[Note])
async def read_notes():
    pass

#read noted by id
@router.get("/{note_id}/", response_model=Note)
async def read_notes_by_id(note_id: int):
    pass

#update notes
@router.put("/{note_id}/", response_model=Note)
async def update_notes(note_id: int, note: NoteUpdate):
    pass

#delete notes
@router.delete("/{note_id}/")
async def delete_notes(note_id: int):
    pass
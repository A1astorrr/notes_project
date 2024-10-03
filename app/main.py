from fastapi import FastAPI
from .datebase import engine, Base
from .models import NoteDB

app = FastAPI()
# register router
Base.include_router(bind=engine)
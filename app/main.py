from fastapi import FastAPI
from .datebase import engine, Base
from .routes import router as note_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
# register router
app.include_router(note_router)
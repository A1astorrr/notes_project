from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .database import engine, Base
from .routes import router as note_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory='frontend/static'), name='static')
# register router
app.include_router(note_router)

@app.get("/")
async def index():
    return FileResponse("frontend/index.html")

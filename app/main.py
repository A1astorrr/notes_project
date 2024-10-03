from fastapi import FastAPI
from .routes import router as nr

app = FastAPI()
# register router
app.include_router(nr)
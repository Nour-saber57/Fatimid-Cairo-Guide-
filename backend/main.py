from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.database import get_db, initialize_database
from models.place import Place
from schemas.places import PlaceRead
from routers.places import router as places_router


app = FastAPI()

app.include_router(places_router)

initialize_database()


@app.get("/health")
def health():
    return {"status": "backend is healthy"}



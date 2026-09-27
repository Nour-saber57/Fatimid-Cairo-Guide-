from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.database import get_db, initialize_database
from models.place import Place
from schemas.places import PlaceRead


app = FastAPI()


initialize_database()


@app.get("/health")
def health():
    return {"status": "backend is healthy"}


@app.get("/places", response_model=list[PlaceRead])
def get_places(db: Session = Depends(get_db)):
    return db.query(Place).all()
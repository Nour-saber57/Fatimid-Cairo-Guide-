from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.database import Base, engine, get_db
from models.place import Place


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "backend is healthy"}


@app.get("/places")
def get_places(db: Session = Depends(get_db)):
    places = db.query(Place).all()
    return places
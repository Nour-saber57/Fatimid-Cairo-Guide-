from fastapi import APIRouter

from database.database import SessionLocal
from models.place import Place


router = APIRouter()


@router.get("/places")
def get_places():
    db = SessionLocal()

    places = db.query(Place).all()

    db.close()

    return places
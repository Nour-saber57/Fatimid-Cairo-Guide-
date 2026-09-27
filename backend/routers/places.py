from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from models.place import Place
from schemas import PlaceRead


router = APIRouter()


@router.get("/places", response_model=list[PlaceRead])
def get_places(db: Annotated[Session, Depends(get_db)]) -> list[Place]:
    return db.query(Place).all()
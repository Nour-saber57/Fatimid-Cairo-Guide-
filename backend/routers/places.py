from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from database.database import get_db
from models.place import Place
from schemas.places import PlaceRead


router = APIRouter()


@router.get("/places", response_model=list[PlaceRead])
def get_places(db: Annotated[Session, Depends(get_db)]) -> list[Place]:
    return db.query(Place).all()


@router.get("/places/{place_id}", response_model=PlaceRead)
def get_place(place_id: int, db: Annotated[Session, Depends(get_db)]) -> Place:
    place = db.query(Place).filter(Place.id == place_id).first()
    if place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return place


@router.get("/places/search/", response_model=list[PlaceRead])
def search_places(q: str, db: Annotated[Session, Depends(get_db)]) -> list[Place]:
    return (
        db.query(Place)
        .filter(
            or_(
                Place.name_en.ilike(f"%{q}%"),
                Place.name_ar.ilike(f"%{q}%"),
            )
        )
        .all()
    )
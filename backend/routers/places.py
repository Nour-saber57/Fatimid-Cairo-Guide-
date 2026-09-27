from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from models.place import Place
from schemas.places import PlaceRead
from sqlalchemy import or_


router = APIRouter()


@router.get("/places", response_model=list[PlaceRead])
def get_places(db: Annotated[Session, Depends(get_db)]) -> list[Place]:
    return db.query(Place).all()


@router.get("/places/search/", response_model=list[PlaceRead])
def search_places(
    q: str,
    db: Annotated[Session, Depends(get_db)],
):
    places = (
        db.query(Place)
        .filter(
            or_(
                Place.name.ilike(f"%{q}%"),
                Place.name_ar.contains(q),
            )
        )
        .all()
    )

    return places
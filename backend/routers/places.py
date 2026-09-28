from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from database.database import get_db
from models.place import Place
from schemas.places import PlaceRead


router = APIRouter()


@router.get(
    "/places",
    response_model=list[PlaceRead]
)
def get_places(
    db: Annotated[Session, Depends(get_db)]
):
    return (
        db.query(Place)
        .order_by(Place.route_order)
        .all()
    )


@router.get(
    "/places/search/",
    response_model=list[PlaceRead]
)
def search_places(
    q: str,
    db: Annotated[Session, Depends(get_db)]
):
    return (
        db.query(Place)
        .filter(
            or_(
                Place.name_en.ilike(f"%{q}%"),
                Place.name_ar.contains(q)
            )
        )
        .order_by(Place.route_order)
        .all()
    )


@router.get(
    "/places/{slug}",
    response_model=PlaceRead
)
def get_place(
    slug: str,
    db: Annotated[Session, Depends(get_db)]
):
    place = (
        db.query(Place)
        .filter(Place.slug == slug)
        .first()
    )

    if place is None:
        raise HTTPException(
            status_code=404,
            detail="Place not found"
        )

    return place
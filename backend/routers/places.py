from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from database.database import get_db
from models.features import Feature
from models.images import PlaceImage
from models.place import Place
from schemas.places import PlaceDetailRead, PlaceRead


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
    "/places/{identifier}",
    response_model=PlaceDetailRead
)
def get_place(
    identifier: str,
    db: Annotated[Session, Depends(get_db)]
):
    place = None
    if identifier.isdecimal():
        place = db.query(Place).filter(Place.id == int(identifier)).first()

    if place is None:
        place = db.query(Place).filter(Place.slug == identifier).first()

    if place is None:
        raise HTTPException(
            status_code=404,
            detail="Place not found"
        )

    place_data = PlaceRead.model_validate(place).model_dump()
    place_data["images"] = (
        db.query(PlaceImage)
        .filter(PlaceImage.place_id == place.id)
        .all()
    )
    place_data["features"] = (
        db.query(Feature)
        .filter(Feature.place_id == place.id)
        .all()
    )
    return place_data
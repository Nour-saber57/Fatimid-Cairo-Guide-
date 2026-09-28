from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from models.images import PlaceImage
from schemas.images import ImageRead


router = APIRouter()


@router.get(
    "/places/{place_id}/images",
    response_model=list[ImageRead]
)
def get_images(
    place_id: int,
    db: Annotated[Session, Depends(get_db)]
):
    return (
        db.query(PlaceImage)
        .filter(PlaceImage.place_id == place_id)
        .all()
    )
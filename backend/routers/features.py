from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from models.features import Feature
from models.place import Place
from schemas.features import FeatureRead


router = APIRouter()


@router.get(
    "/places/{place_slug}/features",
    response_model=list[FeatureRead]
)
def get_features(
    place_slug: str,
    db: Annotated[Session, Depends(get_db)]
):
    return (
        db.query(Feature)
        .join(Place, Feature.place_id == Place.id)
        .filter(Place.slug == place_slug)
        .all()
    )
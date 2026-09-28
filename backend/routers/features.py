from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from models.features import Feature
from models.place import Place
from schemas.features import FeatureRead


router = APIRouter()


@router.get(
    "/places/{place_id}/features",
    response_model=list[FeatureRead]
)
def get_features(
    place_id: int,
    db: Annotated[Session, Depends(get_db)]
):
    return (
        db.query(Feature)
        .join(Place, Feature.place_id == Place.id)
        .filter(Place.id == place_id)
        .all()
    )
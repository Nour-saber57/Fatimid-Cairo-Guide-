from pydantic import BaseModel, ConfigDict


class FeatureCreate(BaseModel):
    place_id: int
    title: str
    title_ar: str
    description: str | None = None
    description_ar: str | None = None
    image_url: str | None = None


class FeatureRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    place_id: int

    title: str
    title_ar: str

    description: str | None = None
    description_ar: str | None = None

    image_url: str | None = None
from pydantic import BaseModel, ConfigDict


class PlaceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    name_ar: str | None = None
    category: str | None = None
    short_description: str | None = None
    story: str | None = None
    built_year: int | None = None
    dynasty: str | None = None
    location: str | None = None
    image_url: str | None = None

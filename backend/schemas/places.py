from pydantic import BaseModel, Field


class PlaceCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    name_ar: str = Field(min_length=1, max_length=200)

    category: str = Field(min_length=1, max_length=100)

    short_description: str | None = None
    story: str | None = None

    built_year: int | None = Field(default=None, ge=900, le=2100)

    dynasty: str | None = None
    location: str | None = None
    image_url: str | None = None
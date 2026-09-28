from pydantic import BaseModel, ConfigDict, Field


class PlaceCreate(BaseModel):
    name_en: str = Field(min_length=1, max_length=255)
    name_ar: str = Field(min_length=1, max_length=255)

    category: str = Field(min_length=1, max_length=100)

    built_year: int | None = Field(default=None, ge=900, le=2100)
    built_year_hijri: str | None = None

    dynasty_en: str | None = None
    dynasty_ar: str | None = None

    patron_en: str | None = None
    patron_ar: str | None = None

    short_description_en: str | None = None
    short_description_ar: str | None = None

    overview_en: str | None = None
    overview_ar: str | None = None

    history_en: str | None = None
    history_ar: str | None = None

    architecture_en: str | None = None
    architecture_ar: str | None = None

    details_en: str | None = None
    details_ar: str | None = None

    story_en: str | None = None
    story_ar: str | None = None

    location_en: str | None = None
    location_ar: str | None = None

    latitude: float | None = None
    longitude: float | None = None

    hero_image_url: str | None = None
    thumbnail_url: str | None = None

    source_title: str | None = None
    source_pages: str | None = None


class PlaceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name_en: str
    name_ar: str
    category: str

    built_year: int | None = None
    built_year_hijri: str | None = None

    dynasty_en: str | None = None
    dynasty_ar: str | None = None

    patron_en: str | None = None
    patron_ar: str | None = None

    short_description_en: str | None = None
    short_description_ar: str | None = None

    overview_en: str | None = None
    overview_ar: str | None = None

    history_en: str | None = None
    history_ar: str | None = None

    architecture_en: str | None = None
    architecture_ar: str | None = None

    details_en: str | None = None
    details_ar: str | None = None

    story_en: str | None = None
    story_ar: str | None = None

    location_en: str | None = None
    location_ar: str | None = None

    latitude: float | None = None
    longitude: float | None = None

    hero_image_url: str | None = None
    thumbnail_url: str | None = None

    source_title: str | None = None
    source_pages: str | None = None
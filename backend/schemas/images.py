from pydantic import BaseModel, ConfigDict


class ImageCreate(BaseModel):
    place_id: int
    image_url: str

    caption_en: str | None = None
    caption_ar: str | None = None


class ImageRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    place_id: int
    image_url: str

    caption_en: str | None = None
    caption_ar: str | None = None
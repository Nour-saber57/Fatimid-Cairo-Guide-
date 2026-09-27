from pydantic import BaseModel, ConfigDict, Field

class featureCreate(BaseModel):
    id: int
    place_id: int
    title:str
    title_ar:str
    description:str | None = None
    description_ar:str | None = None
    image_url:str | None=None
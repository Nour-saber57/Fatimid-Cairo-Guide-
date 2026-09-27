from pydantic import BaseModel, ConfigDict, Field

class ImageCreate(BaseModel):
    place_id: int
    image_url:str
    caption:str
    caption_ar:str
    
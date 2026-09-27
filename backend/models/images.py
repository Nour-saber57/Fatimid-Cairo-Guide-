from sqlalchemy import Column, Integer, String, Text,Float
from database.database import Base

class image(Base):
    __tablename__ = "images"

    id = Column(Integer,primary_key=True, index=True)
    place_id=Column(Integer,nullable=False)
    image_url=Column(String,nullable=False)
    caption=Column(String,nullable=False)
    caption_ar=Column(String,nullable=False)



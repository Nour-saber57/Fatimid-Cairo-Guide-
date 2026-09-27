from sqlalchemy import Column, Integer, String, Text,Float
from database.database import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    name_ar = Column(String, nullable=False)

    category = Column(String, nullable=False)

    short_description = Column(Text)
    overview = Column(Text)
    history = Column(Text)
    architecture = Column(Text)
    details = Column(Text)
    

    built_year = Column(Integer)

    dynasty = Column(String)

    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    hero_image_url = Column(String)
    thumbnail_url= Column(String)
from sqlalchemy import Column, Integer, String, Text
from backend.database import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    name_ar = Column(String, nullable=False)

    category = Column(String, nullable=False)

    short_description = Column(Text)
    story = Column(Text)

    built_year = Column(Integer)

    dynasty = Column(String)

    location = Column(String)

    image_url = Column(String)
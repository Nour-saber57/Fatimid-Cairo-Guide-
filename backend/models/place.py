from sqlalchemy import Column, Integer, String, Text, Float
from database.database import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)

    # Name
    name_en = Column(String, nullable=False)
    name_ar = Column(String, nullable=False)

    # Classification
    category = Column(String, nullable=False)

    # Date / period
    built_year = Column(Integer)
    built_year_hijri = Column(String)

    dynasty_en = Column(String)
    dynasty_ar = Column(String)

    patron_en = Column(String)
    patron_ar = Column(String)

    # Short card text
    short_description_en = Column(Text)
    short_description_ar = Column(Text)

    # Monument detail page
    overview_en = Column(Text)
    overview_ar = Column(Text)

    history_en = Column(Text)
    history_ar = Column(Text)

    architecture_en = Column(Text)
    architecture_ar = Column(Text)

    details_en = Column(Text)
    details_ar = Column(Text)

    # Storytelling section
    story_en = Column(Text)
    story_ar = Column(Text)

    # Map
    location_en = Column(String)
    location_ar = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    # Images
    hero_image_url = Column(String)
    thumbnail_url = Column(String)

    # Source tracking
    source_title = Column(String)
    source_pages = Column(String)
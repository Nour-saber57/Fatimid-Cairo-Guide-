from sqlalchemy import Column, Float, Integer, String, Text

from database.database import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)

    slug = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    route_order = Column(
        Integer,
        nullable=False
    )

    name_en = Column(String, nullable=False)
    name_ar = Column(String, nullable=False)

    category = Column(String, nullable=False)

    built_year = Column(Integer)

    built_date_en = Column(String)
    built_date_ar = Column(String)

    period_en = Column(String)
    period_ar = Column(String)

    patron_en = Column(String)
    patron_ar = Column(String)

    short_description_en = Column(Text)
    short_description_ar = Column(Text)

    overview_en = Column(Text)
    overview_ar = Column(Text)

    history_en = Column(Text)
    history_ar = Column(Text)

    architecture_en = Column(Text)
    architecture_ar = Column(Text)

    details_en = Column(Text)
    details_ar = Column(Text)

    story_en = Column(Text)
    story_ar = Column(Text)

    location_en = Column(String)
    location_ar = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    hero_image_url = Column(String)
    thumbnail_url = Column(String)

    source_title = Column(String)
    source_reference = Column(String)

    verification_url = Column(String)
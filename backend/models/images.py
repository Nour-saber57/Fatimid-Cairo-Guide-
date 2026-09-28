from sqlalchemy import Column, ForeignKey, Integer, String

from database.database import Base


class PlaceImage(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)

    place_id = Column(
        Integer,
        ForeignKey("places.id"),
        nullable=False
    )

    image_url = Column(String, nullable=False)

    caption_en = Column(String)
    caption_ar = Column(String)
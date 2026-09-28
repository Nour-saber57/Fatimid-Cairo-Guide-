from sqlalchemy import Column, ForeignKey, Integer, String, Text

from database.database import Base


class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True)

    place_id = Column(
        Integer,
        ForeignKey("places.id"),
        nullable=False
    )

    title_en = Column(String, nullable=False)
    title_ar = Column(String, nullable=False)

    description_en = Column(Text)
    description_ar = Column(Text)

    image_url = Column(String)
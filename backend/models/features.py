from sqlalchemy import Column, Integer, String, Text, Float
from database.database import Base

class feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    title_ar = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    description_ar = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)
    
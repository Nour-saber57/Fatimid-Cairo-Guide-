from sqlalchemy import Integer, String, Column, Text
from sqlalchemy.orm import relationship
from database.database import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)

    name_en = Column(String, nullable=False)

    name_ar = Column(String, nullable=False)

    category = Column(String, nullable=False)

    year = Column(Integer, nullable=True)

    slug = Column(String, unique=True, nullable=False)
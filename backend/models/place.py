from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Place(Base):
    __tablename__ = "places"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    name_ar: Mapped[str | None] = mapped_column(String(255), nullable=True)
    category: Mapped[str | None] = mapped_column(String(100), nullable=True)
    short_description: Mapped[str | None] = mapped_column(Text, nullable=True)
    story: Mapped[str | None] = mapped_column(Text, nullable=True)
    built_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    dynasty: Mapped[str | None] = mapped_column(String(100), nullable=True)
    location: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

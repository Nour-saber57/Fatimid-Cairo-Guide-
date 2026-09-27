from sqlalchemy import select

from database.database import Base, SessionLocal, engine
from models.place import Place


def seed_places() -> None:
    Base.metadata.create_all(bind=engine)
    with SessionLocal.begin() as db:
        existing_place = db.scalar(
            select(Place).where(Place.slug == "al-hakim-mosque")
        )
        if existing_place is not None:
            print("Al-Hakim Mosque already exists; skipping seed.")
            return

        place = Place(
            name_en="Al-Hakim Mosque",
            name_ar="جامع الحاكم بأمر الله",
            category="mosque",
            year=1013,
            slug="al-hakim-mosque",
        )
        db.add(place)
        db.flush()

        print("Inserted place:")
        print(place.id)
        print(place.name_en)


if __name__ == "__main__":
    seed_places()
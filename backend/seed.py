from database.database import SessionLocal
from models.place import Place


db = SessionLocal()


place = Place(
    name_en="Al-Hakim Mosque",
    name_ar="جامع الحاكم بأمر الله",
    category="mosque",
    year=1013,
    slug="al-hakim-mosque"
)


db.add(place)

db.commit()

db.refresh(place)


print("Inserted place:")
print(place.id)
print(place.name_en)


db.close()
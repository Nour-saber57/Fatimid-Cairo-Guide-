from database.database import SessionLocal, initialize_database
from models.place import Place


place_data = dict(
    name="Al-Aqmar Mosque",
    name_ar="الجامع الأقمر",
    category="mosque",

    short_description=(
        "A 12th-century Fatimid mosque on Al-Muizz Street, "
        "known for its carved stone façade."
    ),

    overview=(
        "Al-Aqmar Mosque is one of the most important surviving "
        "Fatimid monuments in Historic Cairo."
    ),

    history=(
        "The mosque was built in 1125 CE during the reign of "
        "the Fatimid caliph al-Amir bi-Ahkam Allah."
    ),

    architecture=(
        "The mosque is notable for its decorated stone façade "
        "and for aligning its exterior with Al-Muizz Street while "
        "orienting the prayer hall toward the qibla."
    ),

    details=(
        "Its façade includes carved inscriptions, medallions, "
        "and decorative Fatimid motifs."
    ),

    built_year=1125,
    dynasty="Fatimid",

    location="Al-Muizz Street, Historic Cairo, Cairo, Egypt",

    latitude=30.0515,
    longitude=31.2613,

    hero_image_url=(
        "https://commons.wikimedia.org/wiki/Special:Redirect/file/"
        "Aqmar%20Mosque%202019.jpg"
    ),

    thumbnail_url=(
        "https://commons.wikimedia.org/wiki/Special:Redirect/file/"
        "Aqmar%20Mosque%202019.jpg"
    )
)


def seed_places() -> None:
    initialize_database()

    with SessionLocal() as db:

        existing_place = (
            db.query(Place)
            .filter(Place.name == place_data["name"])
            .first()
        )

        if existing_place:
            for key, value in place_data.items():
                setattr(existing_place, key, value)

            print(f"Updated: {existing_place.name}")

        else:
            new_place = Place(**place_data)
            db.add(new_place)

            print(f"Seeded: {place_data['name']}")

        db.commit()


if __name__ == "__main__":
    seed_places()
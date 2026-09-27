from database.database import SessionLocal
from backend.models.place import Place


db = SessionLocal()


place = Place(
    name="Al-Aqmar Mosque",
    name_ar="الجامع الأقمر",
    category="mosque",

    short_description=(
        "A 12th-century Fatimid mosque on Al-Muizz Street, famous for its "
        "richly carved stone façade and its ingenious adaptation to the "
        "alignment of the historic street."
    ),

    story=(
        "Al-Aqmar Mosque was built in 519 AH / 1125 CE during the reign of "
        "the Fatimid caliph al-Amir bi-Ahkam Allah. Its construction was "
        "supervised by the powerful Fatimid vizier al-Ma'mun al-Bata'ihi. "
        "The mosque stood close to the Fatimid caliphal palaces on the great "
        "ceremonial avenue of medieval Cairo, the street now known as "
        "Al-Muizz Street. "

        "One of the mosque's most important features is its stone façade, "
        "which is among the oldest surviving decorated stone mosque façades "
        "in Cairo. The façade contains elaborate carved decoration, Kufic "
        "inscriptions, Qur'anic verses, medallions, and repeated references "
        "to Muhammad and Ali. These decorations make the façade an important "
        "example of Fatimid religious and architectural expression. "

        "The mosque also demonstrates an ingenious architectural solution. "
        "Al-Muizz Street does not run in exactly the same direction as the "
        "qibla. Instead of allowing the mosque's façade to sit at an awkward "
        "angle to the street, its designers aligned the exterior façade with "
        "the street while arranging the interior prayer space toward Mecca. "
        "As a result, the exterior and interior follow slightly different "
        "orientations. "

        "The interior is organized around an open courtyard surrounded by "
        "four arcades. The qibla arcade marks the direction of prayer. "
        "Centuries after its Fatimid construction, the mosque underwent "
        "renovation during the reign of the Mamluk Sultan Barquq in "
        "799 AH / 1397 CE under Prince Yalbugha al-Salmi. "

        "Today, Al-Aqmar Mosque remains one of the most significant surviving "
        "monuments of Fatimid Cairo and an important stop along Al-Muizz "
        "Street, revealing how architecture, urban planning, decoration, "
        "religion, and Fatimid political culture came together in medieval Cairo."
    ),

    built_year=1125,

    dynasty="Fatimid",

    location="Al-Muizz Street, Historic Cairo, Cairo, Egypt",

    image_url=(
        "https://commons.wikimedia.org/wiki/Special:Redirect/file/"
        "Aqmar%20Mosque%202019.jpg"
    )
)


db.add(place)
db.commit()

db.close()
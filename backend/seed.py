from database.database import SessionLocal, initialize_database
from models.place import Place
from models.features import Feature

BOOK_TITLE = "الشارع الأعظم - شارع المعز لدين الله"


places_data = [

    # =========================================================
    # 1. BAB AL-FUTUH
    # =========================================================

    {
        "slug": "bab-al-futuh",
        "route_order": 1,

        "name_en": "Bab al-Futuh",
        "name_ar": "باب الفتوح",

        "category": "gate",

        "built_year": 1087,
        "built_date_en": "1087 CE / 480 AH",
        "built_date_ar": "1087م / 480هـ",

        "period_en": "Fatimid",
        "period_ar": "العصر الفاطمي",

        "patron_en": "Vizier Badr al-Jamali",
        "patron_ar": "الوزير بدر الجمالي",

        "short_description_en":
            "The monumental northern Gate of Conquests and one of the "
            "great surviving entrances to Fatimid Cairo.",

        "short_description_ar":
            "بوابة الفتوح الشمالية الضخمة، وأحد أهم المداخل الباقية "
            "من أسوار القاهرة الفاطمية.",

        "overview_en":
            "Bab al-Futuh marks the northern beginning of the journey "
            "through Al-Muizz Street. Built in stone in the late "
            "eleventh century, it transformed the entrance to Cairo "
            "into both a defensive structure and a statement of power.",

        "overview_ar":
            "يمثل باب الفتوح البداية الشمالية للرحلة في شارع المعز. "
            "شُيد بالحجر في أواخر القرن الحادي عشر ليجمع بين وظيفة "
            "التحصين العسكري وهيبة مدخل العاصمة الفاطمية.",

        "history_en":
            "The gate was constructed by Badr al-Jamali during the "
            "reign of the Fatimid caliph al-Mustansir Billah. It "
            "replaced an earlier gate associated with the armies that "
            "left Cairo on military campaigns.",

        "history_ar":
            "أنشأ بدر الجمالي الباب في عهد الخليفة الفاطمي المستنصر بالله. "
            "وحل محل باب أقدم ارتبط بخروج الجيوش من القاهرة في حملاتها.",

        "architecture_en":
            "Two massive rounded towers frame the passage. Defensive "
            "features were integrated into the upper structure, while "
            "the entrance arch carries carefully carved stone decoration.",

        "architecture_ar":
            "يحيط بالمدخل برجان ضخمان مستديران، وتضم الأجزاء العليا "
            "عناصر دفاعية، بينما يتميز عقد المدخل بالزخارف الحجرية المحفورة.",

        "details_en":
            "Together with Bab al-Nasr and Bab Zuwayla, it is one of the "
            "great surviving examples of Fatimid military architecture.",

        "details_ar":
            "يشكل مع باب النصر وباب زويلة واحدًا من أهم الشواهد الباقية "
            "على العمارة الحربية الفاطمية.",

        "story_en":
            "Begin here, beneath two stone towers that once announced "
            "the edge of Cairo. Beyond this gate, the city changes from "
            "fortification to street, and the long story of Al-Muizz begins.",

        "story_ar":
            "ابدأ رحلتك هنا، تحت برجين حجريين كانا يعلنان قديمًا حدود القاهرة. "
            "بعد عبور الباب تتحول الأسوار إلى شارع، وتبدأ أمامك حكاية المعز الطويلة.",

        "location_en": "Northern end of Al-Muizz Street, Historic Cairo",
        "location_ar": "النهاية الشمالية لشارع المعز، القاهرة التاريخية",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh31.pdf, pp. 4-5",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/bab-al-futuh/",
    },


    # =========================================================
    # 2. AL-HAKIM MOSQUE
    # =========================================================

    {
        "slug": "al-hakim-mosque",
        "route_order": 2,

        "name_en": "Mosque of al-Hakim bi-Amr Allah",
        "name_ar": "جامع الحاكم بأمر الله",

        "category": "mosque",

        "built_year": 1013,
        "built_date_en": "Construction began in 990 CE and was completed in 1013 CE",
        "built_date_ar": "بدأ إنشاؤه سنة 990م واكتمل سنة 1013م",

        "period_en": "Fatimid",
        "period_ar": "العصر الفاطمي",

        "patron_en":
            "Begun by Caliph al-Aziz bi-Allah and completed by al-Hakim bi-Amr Allah",

        "patron_ar":
            "بدأه الخليفة العزيز بالله وأتمه الخليفة الحاكم بأمر الله",

        "short_description_en":
            "One of Cairo's great Fatimid congregational mosques, standing "
            "beside Bab al-Futuh.",

        "short_description_ar":
            "أحد أكبر الجوامع الفاطمية الباقية في القاهرة، ويقع بجوار باب الفتوح.",

        "overview_en":
            "The vast mosque opens immediately after the northern gate, "
            "creating one of the most dramatic entrances into Al-Muizz Street.",

        "overview_ar":
            "يفتح الجامع بساحته الواسعة مباشرة بعد البوابة الشمالية، "
            "ليشكّل أحد أكثر مشاهد الدخول إلى شارع المعز تأثيرًا.",

        "history_en":
            "Caliph al-Aziz began the mosque in 990, but died before it "
            "was finished. His son al-Hakim completed it in 1013. "
            "Its later history included use as military barracks and "
            "other functions before restoration.",

        "history_ar":
            "بدأ الخليفة العزيز بالله بناء الجامع سنة 990م، لكنه توفي "
            "قبل اكتماله، فأتمه ابنه الحاكم بأمر الله سنة 1013م. "
            "وعرف المبنى عبر القرون استخدامات مختلفة قبل أعمال ترميمه.",

        "architecture_en":
            "A large central courtyard is surrounded by arcades, while "
            "two distinctive minarets flank the monumental western façade.",

        "architecture_ar":
            "يتوسط الجامع صحن كبير تحيط به الأروقة، وتقوم على جانبي "
            "واجهته الغربية مئذنتان مميزتان.",

        "details_en":
            "Its monumental projecting entrance is among the important "
            "surviving features of early Fatimid mosque architecture.",

        "details_ar":
            "يعد مدخله البارز الضخم من العناصر المهمة الباقية في "
            "عمارة المساجد الفاطمية المبكرة.",

        "story_en":
            "Step through its entrance and the crowded city suddenly "
            "falls away. The courtyard opens like a pause in the journey—"
            "a vast field of stone, arcades and sky framed by Fatimid Cairo.",

        "story_ar":
            "ما إن تعبر المدخل حتى يتراجع صخب المدينة فجأة. ينفتح الصحن "
            "كاستراحة واسعة في الرحلة؛ حجر وأروقة وسماء تحيط بها القاهرة الفاطمية.",

        "location_en": "Al-Muizz Street beside Bab al-Futuh, al-Gamaliya",
        "location_ar": "شارع المعز بجوار باب الفتوح، الجمالية",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh31.pdf, pp. 6-9",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/mosque-of-al-hakim-bi-amr-allah/",
    },


    # =========================================================
    # 3. AL-AQMAR MOSQUE
    # =========================================================

    {
        "slug": "al-aqmar-mosque",
        "route_order": 3,

        "name_en": "Al-Aqmar Mosque",
        "name_ar": "جامع الأقمر",

        "category": "mosque",

        "built_year": 1125,
        "built_date_en": "1125 CE / 519 AH",
        "built_date_ar": "1125م / 519هـ",

        "period_en": "Fatimid",
        "period_ar": "العصر الفاطمي",

        "patron_en": "Caliph al-Amir bi-Ahkam Allah",
        "patron_ar": "الخليفة الآمر بأحكام الله",

        "short_description_en":
            "A small Fatimid mosque whose carved façade became one of "
            "the architectural signatures of Al-Muizz Street.",

        "short_description_ar":
            "جامع فاطمي صغير أصبحت واجهته الحجرية المنحوتة من أشهر "
            "العلامات المعمارية في شارع المعز.",

        "overview_en":
            "Al-Aqmar appears almost woven into the street itself. "
            "Its importance lies not in monumental scale, but in the "
            "remarkable intelligence and richness of its façade.",

        "overview_ar":
            "يبدو الجامع الأقمر وكأنه منسوج داخل نسيج الشارع نفسه. "
            "ولا تأتي أهميته من ضخامة الحجم، بل من براعة تصميم واجهته "
            "وغناها بالزخارف.",

        "history_en":
            "The mosque was commissioned in 1125 by the Fatimid caliph "
            "al-Amir bi-Ahkam Allah, with construction supervised by "
            "the vizier al-Ma'mun al-Bata'ihi. It was renovated in 1397.",

        "history_ar":
            "أنشأه الخليفة الفاطمي الآمر بأحكام الله سنة 1125م، "
            "وتولى البناء الوزير المأمون البطائحي، ثم جُدد في سنة 1397م.",

        "architecture_en":
            "Its famous stone façade follows the alignment of Al-Muizz "
            "Street while the prayer space behind it maintains the qibla. "
            "Carved medallions, Kufic inscriptions and radiating arches "
            "animate the surface.",

        "architecture_ar":
            "تتبع الواجهة الحجرية اتجاه شارع المعز بينما يحافظ بيت الصلاة "
            "على اتجاه القبلة. وتغطي الواجهة جامات وكتابات كوفية وعقود مشعة.",

        "details_en":
            "The mosque contains a central open courtyard surrounded by "
            "four arcades.",

        "details_ar":
            "يتكون الجامع من صحن أوسط مكشوف تحيط به أربعة أروقة.",

        "story_en":
            "Al-Aqmar hides an architectural puzzle in plain sight. "
            "The street points one way and prayer another, so its builders "
            "created a façade for the city and an interior for the qibla.",

        "story_ar":
            "يخفي الجامع الأقمر لغزًا معماريًا أمام العين مباشرة. "
            "فالشارع يسير في اتجاه والقبلة في اتجاه آخر، فصنع المعمار "
            "واجهة تخاطب المدينة وداخلًا يتجه إلى القبلة.",

        "location_en": "Al-Muizz Street, Historic Cairo",
        "location_ar": "شارع المعز، القاهرة التاريخية",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh31.pdf, pp. 20-21",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/al-aqmar-mosque/",
    },


    # =========================================================
    # 4. ABD AL-RAHMAN KATKHUDA
    # =========================================================

    {
        "slug": "abd-al-rahman-katkhuda-sabil-kuttab",
        "route_order": 4,

        "name_en": "Sabil-Kuttab of Abd al-Rahman Katkhuda",
        "name_ar": "سبيل وكتاب عبد الرحمن كتخدا",

        "category": "sabil_kuttab",

        "built_year": 1744,
        "built_date_en": "1744 CE / 1157 AH",
        "built_date_ar": "1744م / 1157هـ",

        "period_en": "Ottoman",
        "period_ar": "العصر العثماني",

        "patron_en": "Prince Abd al-Rahman Katkhuda al-Qazdagli",
        "patron_ar": "الأمير عبد الرحمن كتخدا القازدغلي",

        "short_description_en":
            "An elegant Ottoman sabil and Quranic school positioned at a "
            "prominent junction of Al-Muizz Street.",

        "short_description_ar":
            "سبيل وكتاب عثماني أنيق يحتل موقعًا بارزًا عند أحد تقاطعات شارع المعز.",

        "overview_en":
            "Water below and education above: the building combines two "
            "charitable functions in a compact urban monument.",

        "overview_ar":
            "ماء في الأسفل وتعليم في الأعلى؛ جمع المبنى وظيفتين خيريتين "
            "في منشأة حضرية صغيرة ومميزة.",

        "history_en":
            "Abd al-Rahman Katkhuda established the monument in 1744 "
            "as part of his extensive architectural patronage in Cairo.",

        "history_ar":
            "أنشأه عبد الرحمن كتخدا سنة 1744م ضمن نشاطه المعماري "
            "الواسع في القاهرة.",

        "architecture_en":
            "The sabil has three prominent façades with copper windows "
            "and marble drinking basins. The upper kuttab was used to "
            "teach children the Quran.",

        "architecture_ar":
            "للسبيل ثلاث واجهات بارزة ذات شبابيك نحاسية وأحواض رخامية "
            "للشرب، بينما خُصص الكتاب في الطابق العلوي لتعليم الأطفال القرآن.",

        "details_en":
            "The interior preserves Ottoman ceramic decoration and religious inscriptions.",

        "details_ar":
            "تحتفظ حجرة السبيل بزخارف خزفية عثمانية وكتابات دينية.",

        "story_en":
            "Imagine the street before bottled water and modern schools. "
            "A passer-by could drink here, while above him children learned "
            "to read and recite—a whole charitable institution stacked into one corner.",

        "story_ar":
            "تخيل الشارع قبل المياه المعبأة والمدارس الحديثة. كان المار "
            "يشرب هنا، بينما يتعلم الأطفال القراءة والقرآن في الطابق الأعلى؛ "
            "مؤسسة خيرية كاملة فوق زاوية واحدة من الشارع.",

        "location_en": "Intersection of Al-Muizz and Tambakshiya streets",
        "location_ar": "تقاطع شارع المعز مع شارع تمبكشية",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh31.pdf, pp. 22-23",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/sabil-kuttab-of-abd-al-rahman-katkhuda/",
    },


    # =========================================================
    # 5. AMIR BASHTAK PALACE
    # =========================================================

    {
        "slug": "amir-bashtak-palace",
        "route_order": 5,

        "name_en": "Palace of Amir Bashtak",
        "name_ar": "قصر الأمير بشتاك",

        "category": "palace",

        "built_year": 1339,
        "built_date_en": "1334–1339 CE / 735–740 AH",
        "built_date_ar": "1334–1339م / 735–740هـ",

        "period_en": "Mamluk",
        "period_ar": "العصر المملوكي",

        "patron_en": "Amir Sayf al-Din Bashtak al-Nasiri",
        "patron_ar": "الأمير سيف الدين بشتاك الناصري",

        "short_description_en":
            "A rare surviving Mamluk palace built over part of the site "
            "of the former Fatimid Eastern Palace.",

        "short_description_ar":
            "قصر مملوكي نادر البقاء، شُيد فوق جزء من موقع القصر "
            "الفاطمي الشرقي القديم.",

        "overview_en":
            "Bashtak Palace changes the journey from religious architecture "
            "to elite domestic life, revealing how a powerful Mamluk prince lived.",

        "overview_ar":
            "ينقل قصر بشتاك الرحلة من العمارة الدينية إلى الحياة السكنية "
            "للنخبة، ويكشف كيف عاش أحد كبار أمراء المماليك.",

        "history_en":
            "Amir Bashtak al-Nasiri built the palace between 1334 and 1339 "
            "on land associated with the former Fatimid Eastern Palace.",

        "history_ar":
            "شيد الأمير بشتاك الناصري القصر بين عامي 1334 و1339م "
            "على أرض ارتبطت بالقصر الفاطمي الشرقي.",

        "architecture_en":
            "The surviving palace includes reception spaces, service areas "
            "and richly treated wooden interiors. Its long façade opens "
            "toward the medieval street through numerous windows.",

        "architecture_ar":
            "يضم الجزء الباقي قاعات استقبال ومناطق خدمية وعناصر خشبية "
            "ثرية، وتفتح واجهته الطويلة على الشارع من خلال عدد كبير من النوافذ.",

        "details_en":
            "The main hall preserves decorated wooden ceilings and a marble fountain.",

        "details_ar":
            "تحتفظ القاعة الرئيسية بأسقف خشبية مزخرفة وفسقية رخامية.",

        "story_en":
            "Behind the stone street façade was another Cairo: receptions, "
            "music, servants, stables and courtly display. Bashtak Palace "
            "lets the visitor step briefly into that private world.",

        "story_ar":
            "خلف الواجهة المطلة على الشارع كانت هناك قاهرة أخرى: "
            "استقبالات وموسيقى وخدم وإسطبلات ومظاهر للحياة الأميرية. "
            "يفتح القصر نافذة قصيرة على ذلك العالم الخاص.",

        "location_en": "Darb Qirmiz off Al-Muizz Street, al-Nahhasin",
        "location_ar": "درب قرمز المتفرع من شارع المعز، النحاسين",

        "latitude": 30.0504,
        "longitude": 31.2616,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh31.pdf, pp. 24-25",
        "verification_url":
            "https://cairo.gov.eg/ar/culture/cultural-destinations/cairo-palaces/amir-bashtak-palace/",
    },


    # =========================================================
    # 6. AL-SALIH AYYUB
    # =========================================================

    {
        "slug": "al-salih-najm-al-din-ayyub",
        "route_order": 6,

        "name_en": "Madrasa and Mausoleum of al-Salih Najm al-Din Ayyub",
        "name_ar": "مدرسة وقبة الصالح نجم الدين أيوب",

        "category": "madrasa_mausoleum",

        "built_year": 1243,
        "built_date_en": "Madrasa: 1243 CE; Mausoleum: 1249–1250 CE",
        "built_date_ar": "المدرسة: 1243م؛ القبة: 1249–1250م",

        "period_en": "Ayyubid",
        "period_ar": "العصر الأيوبي",

        "patron_en": "Sultan al-Salih Najm al-Din Ayyub; mausoleum commissioned by Shajarat al-Durr",
        "patron_ar": "السلطان الصالح نجم الدين أيوب؛ وأنشأت شجر الدر القبة الضريحية",

        "short_description_en":
            "An important Ayyubid madrasa and mausoleum in Bayn al-Qasrayn.",

        "short_description_ar":
            "مدرسة وقبة ضريحية من أهم آثار العصر الأيوبي في منطقة بين القصرين.",

        "overview_en":
            "Here the street records a major political and religious transition "
            "between the Fatimid and later Sunni city.",

        "overview_ar":
            "يسجل هذا الأثر تحولًا سياسيًا ودينيًا مهمًا بين القاهرة "
            "الفاطمية والمدينة في عصرها السني اللاحق.",

        "history_en":
            "The madrasa was founded in 1243 and became the first institution "
            "in Egypt designed to teach all four Sunni schools of jurisprudence. "
            "Shajarat al-Durr later commissioned the mausoleum for her husband.",

        "history_ar":
            "أنشئت المدرسة سنة 1243م، وكانت من أوائل المنشآت التي خصصت "
            "لتدريس المذاهب السنية الأربعة، ثم أنشأت شجر الدر القبة "
            "لزوجها السلطان الصالح.",

        "architecture_en":
            "Only part of the original madrasa survives, including its façade, "
            "minaret and western iwan. The adjoining mausoleum forms a distinct "
            "funerary component.",

        "architecture_ar":
            "بقي من المدرسة أجزاء تشمل الواجهة والمئذنة والإيوان الغربي، "
            "وتجاورها القبة الضريحية كوحدة جنائزية مستقلة.",

        "details_en":
            "The mausoleum contains notable surviving Ayyubid wooden work.",

        "details_ar":
            "تضم القبة نماذج مهمة من الأعمال الخشبية الأيوبية الباقية.",

        "story_en":
            "The stones here tell of a changing Cairo. The city that had been "
            "built for Fatimid rule was being rewritten for a new political "
            "and religious order.",

        "story_ar":
            "تحكي حجارة هذا المكان عن قاهرة تتغير. فالمدينة التي تشكلت "
            "في ظل الحكم الفاطمي كانت يعاد تشكيلها لعصر سياسي وديني جديد.",

        "location_en": "Bayn al-Qasrayn, Al-Muizz Street",
        "location_ar": "بين القصرين، شارع المعز",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh41.pdf, pp. 16-17",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/madrasa-and-mausoleum-of-al-salih-nagm-al-din-ayyub/",
    },


    # =========================================================
    # 7. QALAWUN COMPLEX
    # =========================================================

    {
        "slug": "qalawun-complex",
        "route_order": 7,

        "name_en": "Complex of Sultan al-Mansur Qalawun",
        "name_ar": "مجموعة السلطان المنصور قلاوون",

        "category": "complex",

        "built_year": 1284,
        "built_date_en": "1283–1284 CE / 683–684 AH",
        "built_date_ar": "1283–1284م / 683–684هـ",

        "period_en": "Mamluk",
        "period_ar": "العصر المملوكي",

        "patron_en": "Sultan al-Mansur Sayf al-Din Qalawun",
        "patron_ar": "السلطان المنصور سيف الدين قلاوون",

        "short_description_en":
            "A monumental Mamluk foundation combining worship, education, burial and medicine.",

        "short_description_ar":
            "مجموعة مملوكية ضخمة جمعت بين العبادة والتعليم والدفن والعلاج.",

        "overview_en":
            "The Qalawun complex turns Bayn al-Qasrayn into a wall of monumental "
            "architecture and demonstrates how one foundation could serve "
            "religion, learning, memory and public welfare.",

        "overview_ar":
            "تحول مجموعة قلاوون منطقة بين القصرين إلى واجهة معمارية ضخمة، "
            "وتوضح كيف جمعت منشأة واحدة الدين والتعليم والذكرى والرعاية العامة.",

        "history_en":
            "Sultan Qalawun established the complex in 1283–1284. "
            "Its components included a madrasa, mausoleum and bimaristan hospital.",

        "history_ar":
            "أنشأ السلطان قلاوون المجموعة بين عامي 1283 و1284م، "
            "وضمت مدرسة وقبة ضريحية وبيمارستانًا للعلاج.",

        "architecture_en":
            "The complex is distinguished by monumental façades, elaborate "
            "stone and marble decoration and richly treated interiors.",

        "architecture_ar":
            "تتميز المجموعة بواجهاتها الضخمة وزخارفها الحجرية والرخامية "
            "الغنية وتفاصيلها الداخلية الدقيقة.",

        "details_en":
            "Its bimaristan made medical care part of the same architectural foundation.",

        "details_ar":
            "جعل البيمارستان الرعاية الطبية جزءًا من المؤسسة المعمارية نفسها.",

        "story_en":
            "This was not simply a monument to a ruler. Behind its façade "
            "people prayed, studied, were treated for illness and remembered "
            "the dead—a small city of institutions compressed into one complex.",

        "story_ar":
            "لم تكن المجموعة مجرد نصب لسلطان. خلف الواجهة صلى الناس "
            "وتعلموا وتلقوا العلاج واستعادوا ذكرى الموتى؛ مدينة صغيرة "
            "من المؤسسات مجتمعة في مبنى واحد.",

        "location_en": "Bayn al-Qasrayn, Al-Muizz Street",
        "location_ar": "بين القصرين، شارع المعز",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh41.pdf, pp. 10-15",
        "verification_url":
            "https://egymonuments.gov.eg/en/monuments/madrasa-mausaleum-and-bimaristan-of-al-mansur-qalawun/",
    },


    # =========================================================
    # 8. AL-NASIR MUHAMMAD
    # =========================================================

    {
        "slug": "al-nasir-muhammad-madrasa",
        "route_order": 8,

        "name_en": "Mosque and Madrasa of al-Nasir Muhammad ibn Qalawun",
        "name_ar": "مسجد ومدرسة الناصر محمد بن قلاوون",

        "category": "madrasa",

        "built_year": 1303,
        "built_date_en": "Begun in 1296 and completed between 1298–1303 CE",
        "built_date_ar": "بدأت سنة 1296م واكتملت بين 1298 و1303م",

        "period_en": "Mamluk",
        "period_ar": "العصر المملوكي",

        "patron_en": "Sultan al-Nasir Muhammad ibn Qalawun",
        "patron_ar": "السلطان الناصر محمد بن قلاوون",

        "short_description_en":
            "A Mamluk madrasa wedged into the monumental sequence of Bayn al-Qasrayn.",

        "short_description_ar":
            "مدرسة مملوكية تتوسط السلسلة المعمارية الضخمة في بين القصرين.",

        "overview_en":
            "Its location places it directly between the monuments of Qalawun "
            "and Barquq, making the street itself read like a timeline of Mamluk rule.",

        "overview_ar":
            "يقع الأثر بين منشآت قلاوون وبرقوق، حتى يبدو الشارع نفسه "
            "كأنه خط زمني متتابع لدولة المماليك.",

        "history_en":
            "Construction began under Sultan Katbugha in 1296 and was later "
            "completed under al-Nasir Muhammad.",

        "history_ar":
            "بدأ العمل في المدرسة في عهد السلطان كتبغا سنة 1296م، "
            "ثم استكملها السلطان الناصر محمد.",

        "architecture_en":
            "Its surviving eastern and western iwans, stone façade, marble portal "
            "and square minaret preserve a distinctive mixture of decoration.",

        "architecture_ar":
            "تحتفظ المدرسة بإيوانين باقين وواجهة حجرية ومدخل رخامي "
            "ومئذنة مربعة ذات زخارف مميزة.",

        "details_en":
            "The mausoleum contains burials of members of al-Nasir Muhammad's family.",

        "details_ar":
            "تضم القبة مدافن لعدد من أفراد أسرة الناصر محمد.",

        "story_en":
            "Stand here and look along the façades: generations of rulers "
            "seem to compete for space on the same street, each adding another "
            "layer to Cairo's stone memory.",

        "story_ar":
            "قف هنا وانظر إلى امتداد الواجهات؛ تبدو أجيال من الحكام "
            "وكأنها تتنافس على مساحة في الشارع نفسه، وكل جيل يضيف طبقة "
            "جديدة إلى ذاكرة القاهرة الحجرية.",

        "location_en": "Bayn al-Qasrayn, Al-Muizz Street",
        "location_ar": "بين القصرين، شارع المعز",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh41.pdf, pp. 4-7",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/mosque-and-madrasa-of-al-nasir-muhammad-ibn-qalawun-1/",
    },


    # =========================================================
    # 9. BARQUQ
    # =========================================================

    {
        "slug": "sultan-barquq-madrasa-khanqah",
        "route_order": 9,

        "name_en": "Madrasa and Khanqah of Sultan al-Zahir Barquq",
        "name_ar": "مدرسة وخانقاه السلطان الظاهر برقوق",

        "category": "madrasa_khanqah",

        "built_year": 1386,
        "built_date_en": "1384–1386 CE / 786–788 AH",
        "built_date_ar": "1384–1386م / 786–788هـ",

        "period_en": "Mamluk",
        "period_ar": "العصر المملوكي",

        "patron_en": "Sultan al-Zahir Barquq",
        "patron_ar": "السلطان الظاهر برقوق",

        "short_description_en":
            "A major religious and educational foundation of the early Circassian Mamluk period.",

        "short_description_ar":
            "منشأة دينية وتعليمية كبرى من بدايات عصر المماليك الجراكسة.",

        "overview_en":
            "Barquq's complex adds another monumental layer to Bayn al-Qasrayn, "
            "combining madrasa, mosque, Sufi khanqah and family mausoleum.",

        "overview_ar":
            "تضيف مجموعة برقوق طبقة معمارية ضخمة جديدة إلى بين القصرين، "
            "إذ جمعت مدرسة ومسجدًا وخانقاه وقبة ضريحية للأسرة.",

        "history_en":
            "Sultan al-Zahir Barquq founded the complex between 1384 and 1386.",

        "history_ar":
            "أنشأ السلطان الظاهر برقوق المجموعة بين عامي 1384 و1386م.",

        "architecture_en":
            "An open courtyard is surrounded by four iwans. The qibla iwan "
            "contains a marble mihrab and finely worked wooden furnishings.",

        "architecture_ar":
            "يحيط بالصحن المكشوف أربعة إيوانات، ويضم إيوان القبلة "
            "محرابًا رخاميًا وعناصر خشبية دقيقة الصنع.",

        "details_en":
            "The complex also contained accommodation and service spaces for students and Sufis.",

        "details_ar":
            "اشتملت المنشأة كذلك على مساكن وخدمات للطلاب والصوفية.",

        "story_en":
            "By this point in the walk, Al-Muizz no longer feels like a line "
            "of separate buildings. It becomes a continuous architectural wall "
            "built by rulers across generations.",

        "story_ar":
            "عند هذه النقطة من الرحلة لا يعود شارع المعز مجرد صف من المباني "
            "المنفصلة، بل يتحول إلى جدار معماري متصل صنعته أجيال من الحكام.",

        "location_en": "Bayn al-Qasrayn, Al-Muizz Street",
        "location_ar": "بين القصرين، شارع المعز",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh31.pdf pp. 30-31; continuation in Intro.fh41.pdf",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/madrasa-and-khanaqah-of-sultan-al-zahir-barquq/",
    },


    # =========================================================
    # 10. HAMMAM INAL
    # =========================================================

    {
        "slug": "hammam-sultan-inal",
        "route_order": 10,

        "name_en": "Hammam of Sultan Inal",
        "name_ar": "حمام السلطان إينال",

        "category": "hammam",

        "built_year": 1456,
        "built_date_en": "1456 CE / 861 AH",
        "built_date_ar": "1456م / 861هـ",

        "period_en": "Mamluk",
        "period_ar": "العصر المملوكي",

        "patron_en": "Sultan al-Ashraf Inal",
        "patron_ar": "السلطان الأشرف إينال",

        "short_description_en":
            "A surviving Mamluk public bath that reveals everyday social life beyond palaces and mosques.",

        "short_description_ar":
            "حمام مملوكي باقٍ يكشف جانبًا من الحياة الاجتماعية اليومية "
            "بعيدًا عن القصور والمساجد.",

        "overview_en":
            "The hammam reminds visitors that Al-Muizz was a lived city, "
            "not simply a ceremonial avenue.",

        "overview_ar":
            "يذكرنا الحمام بأن شارع المعز كان مدينة حية، لا مجرد طريق للاحتفالات والآثار.",

        "history_en":
            "Sultan al-Ashraf Inal commissioned the bathhouse in 1456.",

        "history_ar":
            "أنشأ السلطان الأشرف إينال الحمام سنة 1456م.",

        "architecture_en":
            "A bent entrance protected privacy and led successively through "
            "cool, warm and hot spaces. Perforated domes admitted filtered light "
            "and helped regulate heat.",

        "architecture_ar":
            "يحفظ المدخل المنكسر الخصوصية ويقود بالتتابع إلى الحجرات "
            "الباردة والدافئة والساخنة. وتسمح فتحات القباب بدخول الضوء "
            "والمساعدة في تنظيم الحرارة.",

        "details_en":
            "Water was raised from a well and heated before being distributed through the bath.",

        "details_ar":
            "كانت المياه ترفع من بئر ثم تسخن وتوزع على أجزاء الحمام.",

        "story_en":
            "Not every story on Al-Muizz belongs to a sultan. Here the story "
            "is steam, water, conversation and the rhythms of ordinary urban life.",

        "story_ar":
            "ليست كل حكايات المعز عن السلاطين. هنا الحكاية عن البخار "
            "والماء والحديث وإيقاع الحياة اليومية لسكان المدينة.",

        "location_en": "Al-Muizz Street, Historic Cairo",
        "location_ar": "شارع المعز، القاهرة التاريخية",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh31.pdf, pp. 26-27",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/hammam-of-sultan-inal/",
    },


    # =========================================================
    # 11. AL-GHURI COMPLEX
    # =========================================================

    {
        "slug": "sultan-al-ghuri-complex",
        "route_order": 11,

        "name_en": "Sultan al-Ghuri Complex",
        "name_ar": "مجموعة السلطان الغوري",

        "category": "complex",

        "built_year": 1504,
        "built_date_en": "1503–1504 CE / 909–910 AH",
        "built_date_ar": "1503–1504م / 909–910هـ",

        "period_en": "Mamluk",
        "period_ar": "العصر المملوكي",

        "patron_en": "Sultan Qansuh al-Ghuri",
        "patron_ar": "السلطان قانصوه الغوري",

        "short_description_en":
            "A late-Mamluk urban complex split across the street and tied directly to commercial life.",

        "short_description_ar":
            "مجموعة حضرية من أواخر العصر المملوكي تمتد على جانبي الشارع "
            "وترتبط مباشرة بالحياة التجارية.",

        "overview_en":
            "Al-Ghuri's foundation turns the street itself into part of the monument. "
            "Religious, educational, funerary and commercial functions meet here.",

        "overview_ar":
            "تجعل مجموعة الغوري الشارع نفسه جزءًا من الأثر، حيث تلتقي "
            "الوظائف الدينية والتعليمية والجنائزية والتجارية.",

        "history_en":
            "Sultan Qansuh al-Ghuri established the complex in 1503–1504, "
            "little more than a decade before the end of Mamluk rule.",

        "history_ar":
            "أنشأ السلطان قانصوه الغوري المجموعة بين عامي 1503 و1504م، "
            "قبل نهاية حكم المماليك بقليل.",

        "architecture_en":
            "The complex includes a madrasa-mosque and, across the street, "
            "a mausoleum, khanqah, sabil and kuttab. Rich stone, marble and "
            "wood decoration characterize the ensemble.",

        "architecture_ar":
            "تضم المجموعة مدرسة ومسجدًا، ويقابلهما على الجانب الآخر "
            "قبة وخانقاه وسبيل وكتاب، وتتميز بزخارف حجرية ورخامية وخشبية ثرية.",

        "details_en":
            "Its architectural composition deliberately frames the street between its two halves.",

        "details_ar":
            "صُممت المجموعة بحيث يصبح الفراغ بين جانبيها جزءًا من التكوين المعماري.",

        "story_en":
            "Here the street becomes a stage. Buildings rise on both sides "
            "while shops and movement continue between them—the monument and "
            "the city become almost impossible to separate.",

        "story_ar":
            "هنا يتحول الشارع إلى مسرح. ترتفع المباني على الجانبين بينما "
            "تستمر الحركة والتجارة بينهما، حتى يصعب فصل الأثر عن المدينة نفسها.",

        "location_en": "Al-Ghuriyya, southern Al-Muizz Street",
        "location_ar": "الغورية، الجزء الجنوبي من شارع المعز",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh41.pdf, al-Ghuri monument section",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/sultan-al-ghuri-complex/",
    },


    # =========================================================
    # 12. AL-MU'AYYAD SHAYKH
    # =========================================================

    {
        "slug": "al-muayyad-shaykh-mosque",
        "route_order": 12,

        "name_en": "Mosque of Sultan al-Mu'ayyad Shaykh",
        "name_ar": "جامع السلطان المؤيد شيخ",

        "category": "mosque",

        "built_year": 1421,
        "built_date_en": "1415–1421 CE / 818–824 AH",
        "built_date_ar": "1415–1421م / 818–824هـ",

        "period_en": "Mamluk",
        "period_ar": "العصر المملوكي",

        "patron_en": "Sultan al-Mu'ayyad Shaykh",
        "patron_ar": "السلطان المؤيد شيخ",

        "short_description_en":
            "A monumental Mamluk mosque whose twin minarets rise directly above Bab Zuwayla.",

        "short_description_ar":
            "جامع مملوكي ضخم ترتفع مئذنتاه مباشرة فوق برجي باب زويلة.",

        "overview_en":
            "At the southern end of the journey, the mosque and the Fatimid gate "
            "below it fuse two different centuries into a single skyline.",

        "overview_ar":
            "عند النهاية الجنوبية للرحلة يندمج الجامع مع البوابة الفاطمية "
            "تحته، فتجتمع قرون مختلفة في مشهد معماري واحد.",

        "history_en":
            "Al-Mu'ayyad Shaykh founded the mosque between 1415 and 1421 "
            "on the site of a former prison where he had once been confined.",

        "history_ar":
            "أنشأ المؤيد شيخ الجامع بين عامي 1415 و1421م فوق موقع سجن "
            "كان قد حُبس فيه قبل أن يصبح سلطانًا.",

        "architecture_en":
            "The mosque has a courtyard surrounded by arcades. Its most dramatic "
            "urban feature is the pair of Mamluk minarets built on the towers "
            "of the much older Bab Zuwayla.",

        "architecture_ar":
            "يتكون الجامع من صحن تحيط به الأروقة، أما أبرز عناصره في المشهد "
            "الحضري فهما المئذنتان المملوكيتان المقامتان فوق برجي باب زويلة الأقدم.",

        "details_en":
            "One surviving funerary dome contains the burial of the sultan and some of his sons.",

        "details_ar":
            "تضم إحدى القباب الباقية مدفن السلطان وبعض أبنائه.",

        "story_en":
            "The story begins with imprisonment and ends with a mosque. "
            "A place once associated with confinement became the foundation "
            "through which a sultan chose to be remembered.",

        "story_ar":
            "تبدأ الحكاية بالسجن وتنتهي بجامع. فالمكان الذي ارتبط يومًا "
            "بالحبس أصبح المنشأة التي اختار السلطان أن يخلد بها اسمه.",

        "location_en": "Beside Bab Zuwayla, southern Al-Muizz Street",
        "location_ar": "ملاصق لباب زويلة، جنوب شارع المعز",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh41.pdf pp. 40-41 and continuation",
        "verification_url":
            "https://egymonuments.gov.eg/en/monuments/al-muayyad-sheikh-mosque/",
    },


    # =========================================================
    # 13. NAFISA AL-BAYDA
    # =========================================================

    {
        "slug": "nafisa-al-bayda-sabil-kuttab",
        "route_order": 13,

        "name_en": "Sabil-Kuttab of Nafisa al-Bayda",
        "name_ar": "سبيل وكتاب نفيسة البيضا",

        "category": "sabil_kuttab",

        "built_year": 1796,
        "built_date_en": "1796 CE / 1211 AH",
        "built_date_ar": "1796م / 1211هـ",

        "period_en": "Ottoman",
        "period_ar": "العصر العثماني",

        "patron_en": "Nafisa al-Bayda",
        "patron_ar": "نفيسة البيضا",

        "short_description_en":
            "An elegant late-Ottoman charitable monument associated with "
            "one of Cairo's notable women patrons.",

        "short_description_ar":
            "أثر خيري عثماني أنيق يرتبط بإحدى أبرز النساء الراعيات "
            "للعمارة في القاهرة.",

        "overview_en":
            "The monument combines a public water fountain and school, "
            "showing how charity was embedded directly into the life of the street.",

        "overview_ar":
            "يجمع الأثر بين سبيل للمياه وكتاب للتعليم، ويبين كيف كانت "
            "الأعمال الخيرية جزءًا مباشرًا من حياة الشارع.",

        "history_en":
            "Nafisa al-Bayda established the complex in 1796. "
            "It formed part of a larger commercial and charitable foundation.",

        "history_ar":
            "أنشأت نفيسة البيضا المجموعة سنة 1796م، وكانت جزءًا من "
            "منظومة تجارية وخيرية أكبر.",

        "architecture_en":
            "The rounded Ottoman-style sabil façade has three decorated "
            "copper windows, while the upper kuttab opens through arches "
            "supported on marble columns.",

        "architecture_ar":
            "تتميز واجهة السبيل العثمانية المستديرة بثلاثة شبابيك نحاسية "
            "مزخرفة، بينما يفتح الكتاب العلوي من خلال عقود ترتكز على أعمدة رخامية.",

        "details_en":
            "The associated wikala was known for commercial activity including candle production and sale.",

        "details_ar":
            "ارتبطت الوكالة التابعة للمجموعة بالنشاط التجاري ومنه صناعة وبيع الشموع.",

        "story_en":
            "Near the end of the street, the monument tells a quieter story "
            "of water, education, commerce and female patronage in Ottoman Cairo.",

        "story_ar":
            "قرب نهاية الشارع يروي الأثر حكاية أكثر هدوءًا عن الماء "
            "والتعليم والتجارة ورعاية النساء للعمارة في القاهرة العثمانية.",

        "location_en": "Southern Al-Muizz Street, near Bab Zuwayla",
        "location_ar": "جنوب شارع المعز بالقرب من باب زويلة",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh71.pdf, pp. 8-9",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/sabil-kuttab-of-nafisa-al-bayda/",
    },


    # =========================================================
    # 14. BAB ZUWAYLA
    # =========================================================

    {
        "slug": "bab-zuwayla",
        "route_order": 14,

        "name_en": "Bab Zuwayla",
        "name_ar": "باب زويلة",

        "category": "gate",

        "built_year": 1092,
        "built_date_en": "1092 CE / 485 AH",
        "built_date_ar": "1092م / 485هـ",

        "period_en": "Fatimid",
        "period_ar": "العصر الفاطمي",

        "patron_en": "Vizier Badr al-Jamali",
        "patron_ar": "الوزير بدر الجمالي",

        "short_description_en":
            "The monumental southern gate of Fatimid Cairo and the dramatic "
            "end of the Al-Muizz journey.",

        "short_description_ar":
            "البوابة الجنوبية الضخمة للقاهرة الفاطمية والنهاية الدرامية "
            "لرحلة شارع المعز.",

        "overview_en":
            "Bab Zuwayla closes the historic axis begun at Bab al-Futuh. "
            "Its towers carry the later minarets of al-Mu'ayyad Shaykh, "
            "turning the gate into a layered record of Cairo's history.",

        "overview_ar":
            "يغلق باب زويلة المحور التاريخي الذي يبدأ عند باب الفتوح. "
            "وتحمل أبراجه مئذنتي جامع المؤيد شيخ اللاحقتين، فيتحول الباب "
            "إلى سجل متعدد الطبقات لتاريخ القاهرة.",

        "history_en":
            "Badr al-Jamali built the gate in 1092 during the reign of "
            "the Fatimid caliph al-Mustansir. Centuries later it witnessed "
            "major political events, including the end of Mamluk rule.",

        "history_ar":
            "أنشأ بدر الجمالي الباب سنة 1092م في عهد الخليفة المستنصر بالله. "
            "وشهد بعد ذلك بقرون أحداثًا سياسية مهمة ارتبط بعضها بنهاية دولة المماليك.",

        "architecture_en":
            "Two semicircular towers flank the central passage. "
            "The towers later became the bases for the twin minarets "
            "of the Mosque of al-Mu'ayyad Shaykh.",

        "architecture_ar":
            "يحيط بالممر الأوسط برجان نصف دائريان، واستُخدمت قواعدهما "
            "لاحقًا لإقامة مئذنتي جامع المؤيد شيخ.",

        "details_en":
            "The gate was also historically known as Bab al-Mitwalli.",

        "details_ar":
            "عُرف الباب تاريخيًا أيضًا باسم باب المتولي.",

        "story_en":
            "The walk that began beneath Bab al-Futuh ends beneath another "
            "Fatimid gate. Look upward: Mamluk minarets rise from Fatimid towers. "
            "Few places summarize Cairo's habit of building one age upon another so clearly.",

        "story_ar":
            "الرحلة التي بدأت تحت باب الفتوح تنتهي تحت بوابة فاطمية أخرى. "
            "ارفع رأسك؛ مآذن مملوكية ترتفع فوق أبراج فاطمية. قليل من الأماكن "
            "يلخص عادة القاهرة في بناء عصر فوق عصر بهذه الصورة الواضحة.",

        "location_en": "Southern end of Al-Muizz Street, Historic Cairo",
        "location_ar": "النهاية الجنوبية لشارع المعز، القاهرة التاريخية",

        "latitude": None,
        "longitude": None,

        "hero_image_url": None,
        "thumbnail_url": None,

        "source_title": BOOK_TITLE,
        "source_reference": "Intro.fh71.pdf, pp. 10-11",
        "verification_url":
            "https://egymonuments.gov.eg/monuments/bab-zuwayla/",
    },
]

features_data = [

    # =========================================================
    # 1. BAB AL-FUTUH
    # =========================================================

    {
        "place_slug": "bab-al-futuh",
        "title_en": "Twin Defensive Towers",
        "title_ar": "البرجان الدفاعيان",
        "description_en":
            "Two massive rounded stone towers frame the entrance "
            "and give Bab al-Futuh its fortified character.",
        "description_ar":
            "يحيط بمدخل باب الفتوح برجان حجريان ضخمان مستديران "
            "يمنحان البوابة طابعها الدفاعي.",
        "image_url": None,
    },

    {
        "place_slug": "bab-al-futuh",
        "title_en": "Central Gateway",
        "title_ar": "الممر المركزي",
        "description_en":
            "The gateway passes between the two towers and forms "
            "the monumental northern entrance into historic Cairo.",
        "description_ar":
            "يمر المدخل بين البرجين ويشكل بوابة ضخمة للدخول "
            "إلى القاهرة التاريخية من الشمال.",
        "image_url": None,
    },

    {
        "place_slug": "bab-al-futuh",
        "title_en": "Stone Fortifications",
        "title_ar": "التحصينات الحجرية",
        "description_en":
            "The gate is integrated into the heavy stone defensive "
            "walls of Fatimid Cairo.",
        "description_ar":
            "يرتبط الباب بالأسوار والتحصينات الحجرية الضخمة "
            "للقاهرة الفاطمية.",
        "image_url": None,
    },


    # =========================================================
    # 2. AL-HAKIM MOSQUE
    # =========================================================

    {
        "place_slug": "al-hakim-mosque",
        "title_en": "Great Courtyard",
        "title_ar": "الصحن الكبير",
        "description_en":
            "A vast open courtyard forms the heart of the mosque "
            "and is surrounded by arcaded prayer spaces.",
        "description_ar":
            "يشكل الصحن المكشوف الواسع قلب الجامع، "
            "وتحيط به الأروقة من جوانبه.",
        "image_url": None,
    },

    {
        "place_slug": "al-hakim-mosque",
        "title_en": "Arcaded Prayer Halls",
        "title_ar": "أروقة الصلاة",
        "description_en":
            "Rows of arches and columns surround the courtyard "
            "and organize the large interior space.",
        "description_ar":
            "تحيط بالصحن صفوف من العقود والأعمدة "
            "التي تنظم المساحات الداخلية للجامع.",
        "image_url": None,
    },

    {
        "place_slug": "al-hakim-mosque",
        "title_en": "Mihrab",
        "title_ar": "المحراب",
        "description_en":
            "The prayer direction is marked by a richly treated "
            "mihrab within the qibla wall.",
        "description_ar":
            "يتحدد اتجاه الصلاة من خلال محراب بارز "
            "داخل جدار القبلة.",
        "image_url": None,
    },


    # =========================================================
    # 3. AL-AQMAR MOSQUE
    # =========================================================

    {
        "place_slug": "al-aqmar-mosque",
        "title_en": "Carved Stone Façade",
        "title_ar": "الواجهة الحجرية المنحوتة",
        "description_en":
            "The street façade is covered with finely carved "
            "stone decoration and inscriptions.",
        "description_ar":
            "تغطي الواجهة المطلة على الشارع زخارف وكتابات "
            "حجرية منحوتة بدقة.",
        "image_url": None,
    },

    {
        "place_slug": "al-aqmar-mosque",
        "title_en": "Radiating Medallions",
        "title_ar": "الجامات والزخارف المشعة",
        "description_en":
            "Circular medallions and radiating carved patterns "
            "are among the façade's most recognizable details.",
        "description_ar":
            "تعد الجامات الدائرية والزخارف الحجرية المشعة "
            "من أبرز تفاصيل واجهة الجامع.",
        "image_url": None,
    },

    {
        "place_slug": "al-aqmar-mosque",
        "title_en": "Central Courtyard",
        "title_ar": "الصحن الأوسط",
        "description_en":
            "The mosque is organized around a compact open "
            "courtyard surrounded by arcades.",
        "description_ar":
            "ينظم الجامع حول صحن أوسط مكشوف "
            "تحيط به الأروقة.",
        "image_url": None,
    },


    # =========================================================
    # 4. ABD AL-RAHMAN KATKHUDA
    # =========================================================

    {
        "place_slug": "abd-al-rahman-katkhuda-sabil-kuttab",
        "title_en": "Sabil Chamber",
        "title_ar": "حجرة السبيل",
        "description_en":
            "The lower level contains the sabil, where drinking "
            "water was distributed to people passing through the street.",
        "description_ar":
            "يضم المستوى السفلي حجرة السبيل التي خصصت "
            "لتوفير مياه الشرب للمارة.",
        "image_url": None,
    },

    {
        "place_slug": "abd-al-rahman-katkhuda-sabil-kuttab",
        "title_en": "Kuttab Loggia",
        "title_ar": "الكتاب العلوي",
        "description_en":
            "Above the sabil is an open kuttab level used "
            "for children's education.",
        "description_ar":
            "يقع فوق السبيل كتاب مفتوح كان يستخدم "
            "لتعليم الأطفال.",
        "image_url": None,
    },

    {
        "place_slug": "abd-al-rahman-katkhuda-sabil-kuttab",
        "title_en": "Decorated Window Screens",
        "title_ar": "شبابيك السبيل المزخرفة",
        "description_en":
            "Decorative metal window screens distinguish "
            "the curved street-facing façade.",
        "description_ar":
            "تتميز واجهة السبيل المطلة على الشارع "
            "بشبابيك معدنية مزخرفة.",
        "image_url": None,
    },


    # =========================================================
    # 5. AMIR BASHTAK PALACE
    # =========================================================

    {
        "place_slug": "amir-bashtak-palace",
        "title_en": "Grand Reception Hall",
        "title_ar": "قاعة الاستقبال الكبرى",
        "description_en":
            "A tall reception hall forms one of the principal "
            "interior spaces of the palace.",
        "description_ar":
            "تمثل قاعة الاستقبال المرتفعة أحد أهم "
            "الفراغات الداخلية في القصر.",
        "image_url": None,
    },

    {
        "place_slug": "amir-bashtak-palace",
        "title_en": "Decorated Wooden Ceiling",
        "title_ar": "السقف الخشبي المزخرف",
        "description_en":
            "The palace preserves richly decorated wooden "
            "ceilings above its principal spaces.",
        "description_ar":
            "يحتفظ القصر بأسقف خشبية غنية "
            "بالزخارف فوق قاعاته الرئيسية.",
        "image_url": None,
    },

    {
        "place_slug": "amir-bashtak-palace",
        "title_en": "Interior Arches",
        "title_ar": "العقود الداخلية",
        "description_en":
            "Large arches divide and frame the palace's "
            "main interior spaces.",
        "description_ar":
            "تستخدم العقود الكبيرة في تحديد وتقسيم "
            "المساحات الرئيسية داخل القصر.",
        "image_url": None,
    },


    # =========================================================
    # 6. AL-SALIH AYYUB
    # =========================================================

    {
        "place_slug": "al-salih-najm-al-din-ayyub",
        "title_en": "Mausoleum Dome",
        "title_ar": "القبة الضريحية",
        "description_en":
            "The mausoleum is crowned by a prominent dome "
            "that marks the burial chamber.",
        "description_ar":
            "تغطي حجرة الدفن قبة بارزة "
            "تميز الجزء الضريحي من المنشأة.",
        "image_url": None,
    },

    {
        "place_slug": "al-salih-najm-al-din-ayyub",
        "title_en": "Burial Chamber",
        "title_ar": "حجرة الدفن",
        "description_en":
            "The interior contains the funerary space "
            "associated with Sultan al-Salih Ayyub.",
        "description_ar":
            "يضم الداخل الحجرة الجنائزية المرتبطة "
            "بالسلطان الصالح أيوب.",
        "image_url": None,
    },

    {
        "place_slug": "al-salih-najm-al-din-ayyub",
        "title_en": "Mihrab",
        "title_ar": "المحراب",
        "description_en":
            "A decorated mihrab marks the direction of prayer "
            "inside the mausoleum.",
        "description_ar":
            "يحدد محراب مزخرف اتجاه الصلاة "
            "داخل القبة الضريحية.",
        "image_url": None,
    },


    # =========================================================
    # 7. QALAWUN COMPLEX
    # =========================================================

    {
        "place_slug": "qalawun-complex",
        "title_en": "Monumental Street Façade",
        "title_ar": "الواجهة الضخمة المطلة على الشارع",
        "description_en":
            "A long monumental façade defines the complex "
            "along Bayn al-Qasrayn.",
        "description_ar":
            "تمتد واجهة ضخمة للمجموعة على منطقة "
            "بين القصرين وتحدد حضورها في الشارع.",
        "image_url": None,
    },

    {
        "place_slug": "qalawun-complex",
        "title_en": "Mausoleum",
        "title_ar": "القبة الضريحية",
        "description_en":
            "The mausoleum is one of the principal components "
            "of the complex and contains an elaborate interior.",
        "description_ar":
            "تعد القبة الضريحية أحد العناصر الرئيسية "
            "للمجموعة وتتميز بداخل غني بالتفاصيل.",
        "image_url": None,
    },

    {
        "place_slug": "qalawun-complex",
        "title_en": "Minaret",
        "title_ar": "المئذنة",
        "description_en":
            "The complex's minaret rises above the dense "
            "architectural fabric of Al-Muizz Street.",
        "description_ar":
            "ترتفع مئذنة المجموعة فوق النسيج "
            "العمراني الكثيف لشارع المعز.",
        "image_url": None,
    },


    # =========================================================
    # 8. AL-NASIR MUHAMMAD
    # =========================================================

    {
        "place_slug": "al-nasir-muhammad-madrasa",
        "title_en": "Monumental Portal",
        "title_ar": "المدخل التذكاري",
        "description_en":
            "A prominent entrance portal announces the madrasa "
            "from the street.",
        "description_ar":
            "يبرز مدخل ضخم للمدرسة "
            "على واجهتها المطلة على الشارع.",
        "image_url": None,
    },

    {
        "place_slug": "al-nasir-muhammad-madrasa",
        "title_en": "Courtyard",
        "title_ar": "الصحن",
        "description_en":
            "The interior is organized around an open courtyard "
            "linked to the teaching and prayer spaces.",
        "description_ar":
            "ينظم المبنى حول صحن مكشوف "
            "ترتبط به مساحات التعليم والصلاة.",
        "image_url": None,
    },

    {
        "place_slug": "al-nasir-muhammad-madrasa",
        "title_en": "Decorated Wooden Elements",
        "title_ar": "العناصر الخشبية المزخرفة",
        "description_en":
            "The monument preserves detailed wooden decoration "
            "in several interior architectural elements.",
        "description_ar":
            "تظهر داخل المبنى عناصر خشبية "
            "ذات زخارف دقيقة.",
        "image_url": None,
    },


    # =========================================================
    # 9. SULTAN BARQUQ
    # =========================================================

    {
        "place_slug": "sultan-barquq-madrasa-khanqah",
        "title_en": "Striped Stone Façade",
        "title_ar": "الواجهة الحجرية ذات الأشرطة",
        "description_en":
            "The exterior uses alternating stone bands that "
            "give the façade a strong visual rhythm.",
        "description_ar":
            "تستخدم الواجهة أشرطة حجرية متعاقبة "
            "تمنحها إيقاعًا بصريًا واضحًا.",
        "image_url": None,
    },

    {
        "place_slug": "sultan-barquq-madrasa-khanqah",
        "title_en": "Decorated Wooden Ceiling",
        "title_ar": "السقف الخشبي المزخرف",
        "description_en":
            "Richly painted and decorated wooden ceilings "
            "survive within the complex.",
        "description_ar":
            "تحتفظ المجموعة بأسقف خشبية "
            "ملونة وغنية بالزخارف.",
        "image_url": None,
    },

    {
        "place_slug": "sultan-barquq-madrasa-khanqah",
        "title_en": "Minaret",
        "title_ar": "المئذنة",
        "description_en":
            "The tall minaret forms an important vertical "
            "element in the street skyline.",
        "description_ar":
            "تشكل المئذنة المرتفعة عنصرًا رأسيًا "
            "بارزًا في خط سماء شارع المعز.",
        "image_url": None,
    },


    # =========================================================
    # 10. HAMMAM INAL
    # =========================================================

    {
        "place_slug": "hammam-sultan-inal",
        "title_en": "Domed Bathing Chamber",
        "title_ar": "قاعة الاستحمام المقببة",
        "description_en":
            "One of the main bathing spaces is covered by "
            "a rounded dome.",
        "description_ar":
            "تغطي إحدى قاعات الاستحمام الرئيسية "
            "قبة مستديرة.",
        "image_url": None,
    },

    {
        "place_slug": "hammam-sultan-inal",
        "title_en": "Roof Light Openings",
        "title_ar": "فتحات الإضاءة في القبة",
        "description_en":
            "Small openings in the dome allow filtered "
            "light into the bathing space.",
        "description_ar":
            "تسمح الفتحات الصغيرة في القبة "
            "بدخول الضوء إلى قاعة الحمام.",
        "image_url": None,
    },

    {
        "place_slug": "hammam-sultan-inal",
        "title_en": "Bathing Rooms",
        "title_ar": "غرف الحمام",
        "description_en":
            "The hammam is composed of a sequence of enclosed "
            "spaces serving the bathing process.",
        "description_ar":
            "يتكون الحمام من مجموعة من الحجرات "
            "المتتابعة المخصصة لعملية الاستحمام.",
        "image_url": None,
    },


    # =========================================================
    # 11. AL-GHURI COMPLEX
    # =========================================================

    {
        "place_slug": "sultan-al-ghuri-complex",
        "title_en": "Muqarnas Portal",
        "title_ar": "المدخل ذو المقرنصات",
        "description_en":
            "The monumental entrance is emphasized by deep "
            "muqarnas decoration above the doorway.",
        "description_ar":
            "يتميز المدخل الضخم بزخارف المقرنصات "
            "العميقة أعلى فتحة الدخول.",
        "image_url": None,
    },

    {
        "place_slug": "sultan-al-ghuri-complex",
        "title_en": "Minaret",
        "title_ar": "المئذنة",
        "description_en":
            "The highly visible minaret rises above "
            "the southern section of Al-Muizz Street.",
        "description_ar":
            "ترتفع مئذنة المجموعة بشكل واضح "
            "فوق الجزء الجنوبي من شارع المعز.",
        "image_url": None,
    },

    {
        "place_slug": "sultan-al-ghuri-complex",
        "title_en": "Mihrab and Minbar",
        "title_ar": "المحراب والمنبر",
        "description_en":
            "The prayer interior includes an elaborate "
            "mihrab and wooden minbar.",
        "description_ar":
            "تضم مساحة الصلاة محرابًا غنيًا "
            "بالتفاصيل ومنبرًا خشبيًا.",
        "image_url": None,
    },

    {
        "place_slug": "sultan-al-ghuri-complex",
        "title_en": "Sabil-Kuttab Wing",
        "title_ar": "جناح السبيل والكتاب",
        "description_en":
            "The complex also includes a charitable sabil "
            "and an upper kuttab overlooking the street.",
        "description_ar":
            "تضم المجموعة أيضًا سبيلًا خيريًا "
            "وكتابًا علويًا يطل على الشارع.",
        "image_url": None,
    },


    # =========================================================
    # 12. AL-MU'AYYAD SHAYKH
    # =========================================================

    {
        "place_slug": "al-muayyad-shaykh-mosque",
        "title_en": "Twin Minarets",
        "title_ar": "المئذنتان",
        "description_en":
            "Two Mamluk minarets rise above the towers "
            "of Bab Zuwayla.",
        "description_ar":
            "ترتفع مئذنتان مملوكيتان فوق "
            "برجي باب زويلة.",
        "image_url": None,
    },

    {
        "place_slug": "al-muayyad-shaykh-mosque",
        "title_en": "Arcaded Courtyard",
        "title_ar": "الصحن المحاط بالأروقة",
        "description_en":
            "The mosque contains a central courtyard "
            "surrounded by arcaded spaces.",
        "description_ar":
            "يحتوي الجامع على صحن مركزي "
            "تحيط به الأروقة.",
        "image_url": None,
    },

    {
        "place_slug": "al-muayyad-shaykh-mosque",
        "title_en": "Monumental Entrance",
        "title_ar": "المدخل الضخم",
        "description_en":
            "A large decorated entrance announces the mosque "
            "within the dense southern part of the street.",
        "description_ar":
            "يظهر للجامع مدخل كبير مزخرف "
            "وسط النسيج العمراني الكثيف للمنطقة.",
        "image_url": None,
    },


    # =========================================================
    # 13. NAFISA AL-BAYDA
    # =========================================================

    {
        "place_slug": "nafisa-al-bayda-sabil-kuttab",
        "title_en": "Rounded Sabil Façade",
        "title_ar": "واجهة السبيل المستديرة",
        "description_en":
            "The lower sabil projects toward the street "
            "with a curved façade.",
        "description_ar":
            "يبرز الجزء السفلي للسبيل نحو الشارع "
            "بواجهة منحنية.",
        "image_url": None,
    },

    {
        "place_slug": "nafisa-al-bayda-sabil-kuttab",
        "title_en": "Decorative Window Grilles",
        "title_ar": "الشبابيك المعدنية المزخرفة",
        "description_en":
            "Large decorative grilles cover the windows "
            "of the sabil chamber.",
        "description_ar":
            "تغطي شبابيك حجرة السبيل "
            "حواجز معدنية كبيرة مزخرفة.",
        "image_url": None,
    },

    {
        "place_slug": "nafisa-al-bayda-sabil-kuttab",
        "title_en": "Upper Kuttab",
        "title_ar": "الكتاب العلوي",
        "description_en":
            "An upper open level forms the kuttab "
            "above the water fountain.",
        "description_ar":
            "يقع الكتاب في مستوى علوي مفتوح "
            "فوق حجرة السبيل.",
        "image_url": None,
    },


    # =========================================================
    # 14. BAB ZUWAYLA
    # =========================================================

    {
        "place_slug": "bab-zuwayla",
        "title_en": "Twin Rounded Towers",
        "title_ar": "البرجان المستديران",
        "description_en":
            "Two massive rounded towers flank the southern "
            "gateway into the historic city.",
        "description_ar":
            "يحيط بالبوابة الجنوبية برجان ضخمان "
            "مستديران.",
        "image_url": None,
    },

    {
        "place_slug": "bab-zuwayla",
        "title_en": "Central Arched Passage",
        "title_ar": "الممر ذو العقد",
        "description_en":
            "A monumental arched opening passes between "
            "the two defensive towers.",
        "description_ar":
            "يمر مدخل كبير معقود بين "
            "البرجين الدفاعيين.",
        "image_url": None,
    },

    {
        "place_slug": "bab-zuwayla",
        "title_en": "Minarets Above the Gate",
        "title_ar": "المآذن فوق الباب",
        "description_en":
            "The later minarets of al-Mu'ayyad Shaykh rise "
            "directly from the two gate towers.",
        "description_ar":
            "ترتفع مئذنتا جامع المؤيد شيخ "
            "مباشرة فوق برجي الباب.",
        "image_url": None,
    },
]

def seed_places() -> None:
    initialize_database()

    with SessionLocal() as db:
        for place_data in places_data:
            existing_place = (
                db.query(Place)
                .filter(Place.slug == place_data["slug"])
                .first()
            )

            if existing_place:
                for key, value in place_data.items():
                    setattr(existing_place, key, value)
                print(f"Updated: {existing_place.name_en}")
            else:
                new_place = Place(**place_data)
                db.add(new_place)
                print(f"Seeded: {place_data['name_en']}")

        db.commit()


def seed_features() -> None:

    with SessionLocal() as db:

        for feature_data in features_data:

            place = (
                db.query(Place)
                .filter(
                    Place.slug == feature_data["place_slug"]
                )
                .first()
            )

            if place is None:
                print(
                    f"Place not found: "
                    f"{feature_data['place_slug']}"
                )
                continue

            existing_feature = (
                db.query(Feature)
                .filter(
                    Feature.place_id == place.id,
                    Feature.title_en == feature_data["title_en"]
                )
                .first()
            )

            if existing_feature:

                existing_feature.title_ar = (
                    feature_data["title_ar"]
                )

                existing_feature.description_en = (
                    feature_data["description_en"]
                )

                existing_feature.description_ar = (
                    feature_data["description_ar"]
                )

                existing_feature.image_url = (
                    feature_data["image_url"]
                )

                print(
                    f"Updated feature: "
                    f"{feature_data['title_en']}"
                )

            else:

                new_feature = Feature(
                    place_id=place.id,

                    title_en=feature_data["title_en"],
                    title_ar=feature_data["title_ar"],

                    description_en=feature_data["description_en"],
                    description_ar=feature_data["description_ar"],

                    image_url=feature_data["image_url"],
                )

                db.add(new_feature)

                print(
                    f"Seeded feature: "
                    f"{feature_data['title_en']}"
                )

        db.commit()

        db.add(new_feature)
        db.commit()
        print("Feature added successfully")


if __name__ == "__main__":
    seed_places()
    seed_features()
import React, { useEffect, useMemo, useState } from "react";
import bundledPlaces from "./places.json";

const words = {
  en: {
    nav: { home: "Home", explore: "Explore", map: "Map", stories: "Stories", about: "About" },
    search: "Search places", enter: "Enter Fatimid Cairo", begin: "Begin the journey", scroll: "Scroll to explore",
    eyebrow: "A WALK THROUGH FATIMID CAIRO", street: "AL-MUIZZ LI-DIN ALLAH STREET", centuries: "One street. Centuries of stories.",
    heritage: "A Living Heritage", intro: "Al-Muizz Street is the heart of historic Cairo, where mosques, madrasas, palaces and lanes tell the story of the Fatimid era and the centuries that followed.",
    discover: "Explore the Street", stops: "stops", exploreTitle: "Explore Al-Muizz Street", exploreSub: "Walk through time and discover its most important monuments.",
    route: "THE HISTORIC ROUTE", north: "NORTH GATE", south: "SOUTH GATE", mapTitle: "Map of Al-Muizz Street", mapSub: "Explore the monuments and their stories.",
    categories: { mosque: "Mosques", madrasa: "Madrasas", madrasa_mausoleum: "Madrasas", madrasa_khanqah: "Madrasas", palace: "Palaces", sabil_kuttab: "Houses", gate: "Gates", complex: "Complexes", hammam: "Houses" },
    overview: "Overview", history: "History", architecture: "Architecture", details: "Details", gallery: "Gallery", location: "Location", features: "Architectural Features", featureIntro: "Discover the unique elements that make this monument special.",
    story: "Read the Story", sources: "Sources", official: "Official reference", built: "Built", period: "Period", patron: "Patron", locationLabel: "Location", viewAll: "View all", all: "All", ask: "Ask Your Historical Guide", askSub: "Ask anything about Al-Muizz Street, its monuments, architecture, or the culture of Fatimid Cairo.",
    prompt1: "Why is Al-Hakim Mosque important?", prompt2: "What is the meaning of this decoration?", prompt3: "How did people live in Fatimid Cairo?", prompt4: "Compare Al-Aqmar and Al-Hakim Mosques.", input: "Type your question...", send: "Send question", loading: "Opening the guide...", error: "The guide could not load. Check that the backend is running.", retry: "Try again", noMatch: "No places match your search.", back: "Back to the route", aboutTitle: "A city shaped by centuries", aboutText: "Al-Muizz Street gathers the layers of Cairo in one walk: Fatimid gates, Mamluk schools, Ottoman houses and the everyday life that continues around them.", answerFallback: "Choose a monument from the route to explore its history, architecture and stories.", guideIntro: "I can help you explore the places along Al-Muizz Street. Try one of these questions or ask about the selected monument.",
  },
  ar: {
    nav: { home: "الرئيسية", explore: "استكشف", map: "الخريطة", stories: "الحكايات", about: "عن الدليل" },
    search: "ابحث عن مكان", enter: "ادخل إلى القاهرة الفاطمية", begin: "ابدأ الرحلة", scroll: "تابع للاستكشاف",
    eyebrow: "جَوْلَةٌ فِي القَاهِرَةِ الفَاطِمِيَّة", street: "شَارِعُ المُعِزّ لِدِينِ الله", centuries: "شارع واحد، وحكايات تمتد عبر القرون.",
    heritage: "تراث حيّ", intro: "شارع المعز قلب القاهرة التاريخية؛ حيث تحكي المساجد والمدارس والقصور والأزقة قصة العصر الفاطمي وما تلاه من عصور.",
    discover: "استكشف الشارع", stops: "موقعًا", exploreTitle: "استكشف شارع المعز", exploreSub: "امشِ عبر الزمن واكتشف أبرز معالم الشارع.",
    route: "المسار التاريخي", north: "البوابة الشمالية", south: "البوابة الجنوبية", mapTitle: "خريطة شارع المعز", mapSub: "اكتشف المعالم والحكايات من حولها.",
    categories: { mosque: "مساجد", madrasa: "مدارس", madrasa_mausoleum: "مدارس", madrasa_khanqah: "مدارس", palace: "قصور", sabil_kuttab: "بيوت", gate: "أبواب", complex: "مجموعات معمارية", hammam: "بيوت" },
    overview: "نظرة عامة", history: "التاريخ", architecture: "العمارة", details: "تفاصيل", gallery: "الصور", location: "الموقع", features: "عناصر معمارية", featureIntro: "اكتشف العناصر الفريدة التي تمنح هذا الأثر تميّزه.",
    story: "اقرأ الحكاية", sources: "المراجع", official: "المصدر الرسمي", built: "تاريخ البناء", period: "العصر", patron: "الراعي", locationLabel: "الموقع", viewAll: "عرض الكل", all: "الكل", ask: "اسأل دليلك التاريخي", askSub: "اسأل عن شارع المعز أو معالمه أو عمارته أو ثقافة القاهرة الفاطمية.",
    prompt1: "ما أهمية جامع الحاكم؟", prompt2: "ما معنى هذه الزخارف؟", prompt3: "كيف عاش الناس في القاهرة الفاطمية؟", prompt4: "قارن بين جامعي الأقمر والحاكم.", input: "اكتب سؤالك...", send: "إرسال السؤال", loading: "جارٍ فتح الدليل...", error: "تعذر تحميل الدليل. تأكد من تشغيل الخادم.", retry: "حاول مرة أخرى", noMatch: "لا توجد أماكن تطابق البحث.", back: "العودة إلى المسار", aboutTitle: "مدينة صاغتها القرون", aboutText: "يجمع شارع المعز طبقات القاهرة في مسيرة واحدة: أبواب فاطمية ومدارس مملوكية وبيوت عثمانية وحياة يومية تستمر حولها.", answerFallback: "اختر معلمًا من المسار لاستكشاف تاريخه وعماره وحكاياته.", guideIntro: "أساعدك في اكتشاف معالم شارع المعز. اختر أحد الأسئلة أو اسأل عن المعلم المحدد.",
  },
};

const navItems = ["home", "explore", "map", "stories", "about"];
const categoryIcons = { mosque: "۞", madrasa: "⌂", madrasa_mausoleum: "⌂", madrasa_khanqah: "⌂", palace: "♜", sabil_kuttab: "⌂", gate: "◈", complex: "✳", hammam: "⌂" };
const mapPositions = [[24,10],[28,16],[32,22],[35,28],[39,34],[43,40],[47,46],[50,52],[54,58],[58,64],[62,70],[66,76],[70,82],[74,88]];

function categoryGroup(value) {
  if (value?.startsWith("madrasa")) return "madrasa";
  if (["hammam", "sabil_kuttab"].includes(value)) return "sabil_kuttab";
  return value;
}

function local(record, field, language) {
  return record?.[`${field}_${language}`] || record?.[`${field}_en`] || "";
}

function App() {
  const [language, setLanguage] = useState("en");
  const [page, setPage] = useState("landing");
  const [places, setPlaces] = useState([]);
  const [selectedSlug, setSelectedSlug] = useState(null);
  const [detail, setDetail] = useState(null);
  const [detailTab, setDetailTab] = useState("overview");
  const [search, setSearch] = useState("");
  const [searchOpen, setSearchOpen] = useState(false);
  const [category, setCategory] = useState("all");
  const [mapZoom, setMapZoom] = useState(1);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [retry, setRetry] = useState(0);
  const [activeImage, setActiveImage] = useState(null);
  const [question, setQuestion] = useState("");
  const [conversation, setConversation] = useState([]);
  const text = words[language];
  const isArabic = language === "ar";

  useEffect(() => {
    const controller = new AbortController();
    setLoading(true);
    setError(false);
    fetch("/api/places", { signal: controller.signal })
      .then((response) => {
        if (!response.ok) throw new Error("Places request failed");
        return response.json();
      })
      .then((data) => {
        const records = data.length ? data.map((place) => { const saved = bundledPlaces.find((p) => p.slug === place.slug); return { ...saved, ...place, hero_image_url: place.hero_image_url || saved?.hero_image_url, thumbnail_url: place.thumbnail_url || saved?.thumbnail_url }; }) : bundledPlaces;
        setPlaces(records);
        setSelectedSlug((current) => current ?? records[0]?.slug ?? null);
      })
      .catch((requestError) => {
        if (requestError.name !== "AbortError") { setPlaces(bundledPlaces); setSelectedSlug((current) => current ?? bundledPlaces[0]?.slug); }
      })
      .finally(() => {
        if (!controller.signal.aborted) setLoading(false);
      });
    return () => controller.abort();
  }, [retry]);

  const selectedPlace = places.find((place) => place.slug === selectedSlug);

  useEffect(() => {
    if (!selectedPlace) return undefined;
    const controller = new AbortController();
    setDetail(null);
    setActiveImage(null);
    fetch(`/api/places/${encodeURIComponent(selectedPlace.slug)}`, { signal: controller.signal })
      .then((response) => {
        if (!response.ok) throw new Error("Place detail request failed");
        return response.json();
      })
      .then((record) => { const saved = bundledPlaces.find((p) => p.slug === record.slug); setDetail({ ...saved, ...record, hero_image_url: record.hero_image_url || saved?.hero_image_url, images: record.images?.length ? record.images : saved?.images || [], features: record.features?.length ? record.features : saved?.features || [] }); })
      .catch((requestError) => {
        if (requestError.name !== "AbortError") setDetail(bundledPlaces.find((place) => place.slug === selectedPlace.slug) || null);
      });
    return () => controller.abort();
  }, [selectedPlace]);

  const visiblePlaces = useMemo(() => {
    const query = search.trim().toLocaleLowerCase();
    return places.filter((place) => {
      const matchesQuery = !query || [place.name_en, place.name_ar, place.category, place.short_description_en]
        .filter(Boolean).some((value) => value.toLocaleLowerCase().includes(query));
      const matchesCategory = category === "all" || categoryGroup(place.category) === category;
      return matchesQuery && matchesCategory;
    });
  }, [places, search, category]);

  const activePlace = detail?.slug === selectedSlug ? detail : selectedPlace;
  const images = activePlace?.images ?? [];
  const heroImage = activeImage || (activePlace?.slug === "al-hakim-mosque" ? images[1]?.image_url : null) || activePlace?.hero_image_url || images[0]?.image_url || activePlace?.thumbnail_url;

  function navigate(nextPage) {
    setPage(nextPage);
    setSearch("");
    setCategory("all");
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function selectPlace(place) {
    setSelectedSlug(place.slug);
    setDetailTab("overview");
    setPage("detail");
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function sendQuestion(value = question) {
    const prompt = value.trim();
    if (!prompt) return;
    const normalized = prompt.toLocaleLowerCase();
    const match = places.find((place) => [place.name_en,place.name_ar,place.slug.replaceAll("-"," ")].filter(Boolean).some((name) => normalized.includes(name.toLocaleLowerCase()))) || (normalized.includes("hakim") || normalized.includes("الحاكم") ? places.find((p) => p.slug === "al-hakim-mosque") : null) || activePlace;
    const field = /decor|architect|زخرف|عمار/.test(normalized) ? "architecture" : "history";
    const answer = local(match, field, language) || local(match, "overview", language) || text.answerFallback;
    setConversation((current) => [...current, { question: prompt, answer }]);
    setQuestion("");
  }

  function photo(url, alt, className = "", eager = false, width = 480) {
    if (!url) return null;
    const localImageUrl = url.startsWith("/images/") ? url.replace(/\.png$/, ".webp") : url;
    const imageUrl = localImageUrl.includes("commons.wikimedia.org/wiki/Special:FilePath/")
      ? `${localImageUrl}${localImageUrl.includes("?") ? "&" : "?"}width=${width}`
      : localImageUrl;
    return <img className={className} src={imageUrl} alt={alt} loading={eager ? "eager" : "lazy"} decoding="async" fetchPriority={eager ? "high" : "auto"} onError={(event) => { if (!event.currentTarget.dataset.fallback) { event.currentTarget.dataset.fallback = "true"; event.currentTarget.src = "/images/street.webp"; } }} />;
  }

  function categoryLabel(value) {
    return text.categories[categoryGroup(value)] || value.replaceAll("_", " ");
  }

  function placeCard(place, index, compact = false) {
    const photoUrl = place.hero_image_url || place.thumbnail_url;
    return (
      <button className={`monument-card ${compact ? "compact" : ""}`} key={place.id} onClick={() => selectPlace(place)} type="button">
        <div className="monument-photo">
          <span className="image-number">{String(place.route_order).padStart(2, "0")}</span>
          {photo(photoUrl, local(place, "name", language))}
          <span className="photo-arrow" aria-hidden="true">↗</span>
        </div>
        <div className="monument-card-copy">
          <div><h3>{local(place, "name", language)}</h3><span>{place.built_year ? `${place.built_year}` : categoryLabel(place.category)}</span></div>
          {!compact && <span className="card-open" aria-hidden="true">›</span>}
        </div>
      </button>
    );
  }

  function header() {
    return (
      <header className={`site-header ${page === "landing" ? "on-hero" : ""}`}>
        <button className="menu-button" type="button" aria-label={isArabic ? "القائمة" : "Menu"} onClick={() => navigate(page === "landing" ? "home" : "landing")}>☰</button>
        <button className="brand" type="button" onClick={() => navigate("landing")}>
          <span className="brand-mark">۞</span>
          <span><b>Al-Muizz</b><small>FATIMID CAIRO</small></span>
        </button>
        <nav className="main-nav" aria-label="Main navigation">
          {navItems.map((item) => <button type="button" key={item} className={page === item ? "current" : ""} onClick={() => navigate(item)}>{text.nav[item]}</button>)}
        </nav>
        <div className="header-actions">
          {searchOpen && <input className="header-search" autoFocus placeholder={text.search} value={search} onChange={(event) => { setSearch(event.target.value); setPage("explore"); }} />}
          <button className="icon-button" type="button" aria-label={text.search} onClick={() => setSearchOpen((value) => !value)}>⌕</button>
          <button className="guide-shortcut" type="button" aria-label={text.ask} onClick={() => navigate("guide")}>✳</button>
          <span className="header-rule" />
          <div className="language-switch">
            <button type="button" className={language === "ar" ? "active" : ""} onClick={() => setLanguage("ar")}>عربي</button>
            <span>/</span>
            <button type="button" className={language === "en" ? "active" : ""} onClick={() => setLanguage("en")}>EN</button>
          </div>
        </div>
      </header>
    );
  }

  function landing() {
    const gate = places.find((place) => place.category === "gate") || places[0];
    return (
      <main className="landing-page">
        {photo("/images/entrance.png", "Illustrated entrance to historic Cairo", "landing-photo", true, 1280)}
        <div className="landing-vignette" />
        <div className="landing-ornament" aria-hidden="true">۞</div>
        <section className="landing-copy">
          <span className="small-arabic" lang="ar">ادخل إلى<br />القاهرة الفاطمية</span>
          <h1>{isArabic ? "القاهرة الفاطمية" : "Enter Fatimid Cairo"}</h1>
          <p>{isArabic ? "اكتشف التاريخ والعمارة وحكايات شارع المعز" : "Discover the history, architecture and stories of Al-Muizz Street"}</p>
          <button className="gold-button" type="button" onClick={() => navigate("home")}>
            <span>{text.begin}</span><b aria-hidden="true">→</b>
          </button>
        </section>
        <div className="landing-bottom"><span className="bottom-rule" />{text.scroll}<span className="bottom-rule" /></div>
      </main>
    );
  }

  function overview() {
    const featurePlaces = places;
    const groups = ["mosque", "madrasa", "palace", "sabil_kuttab", "gate"];
    return (
      <main className="page-shell overview-page">
        <section className="overview-hero">
          {photo("/images/street.png", "Al-Muizz Street architectural illustration", "", true, 1280)}
          <div className="overview-shade" />
          <div className="overview-hero-copy">
            <span className="arabic-title">شارع المعز لدين الله</span>
            <h1>{text.street}</h1>
            <p>{text.centuries}</p>
            <button className="green-button" type="button" onClick={() => navigate("explore")}>{text.discover}<b>→</b></button>
          </div>
          <span className="hero-index">30°03′N&nbsp; / &nbsp;31°15′E</span>
        </section>
        <section className="heritage-intro">
          <span className="arabic-divider">۞</span>
          <h2>{text.heritage}</h2>
          <p>{text.intro}</p>
        </section>
        <section className="category-strip" aria-label={text.exploreTitle}>
          {groups.map((group) => {
            const representative = featurePlaces.find((place) => categoryGroup(place.category) === group);
            return (
              <button className="category-tile" key={group} type="button" onClick={() => { setCategory(group); navigate("explore"); setCategory(group); }}>
                <span className="category-image">
                  {photo(representative?.hero_image_url || representative?.thumbnail_url, categoryLabel(group))}
                  <span>{categoryIcons[group]}</span>
                </span>
                <strong>{categoryLabel(group)}</strong>
                <small>{representative ? local(representative, "name", language) : text.viewAll}</small>
              </button>
            );
          })}
        </section>
        <div className="overview-bottomline"><span>AL-MUIZZ STREET</span><span>FROM BAB AL-FUTUH TO BAB ZUWAYLA</span><span>{places.length} {text.stops}</span></div>
      </main>
    );
  }

  function explore() {
    const filterCategories = ["all", ...new Set(places.map((place) => categoryGroup(place.category)))];
    return (
      <main className="page-shell explore-page">
        <div className="page-heading">
          <div><span className="eyebrow">{text.route}</span><h1>{text.exploreTitle}</h1><p>{text.exploreSub}</p></div>
          <span className="heading-stamp">{String(places.length).padStart(2, "0")} <small>{text.stops}</small></span>
        </div>
        <div className="filter-row">
          <div className="category-filters">{filterCategories.map((item) => <button type="button" className={category === item ? "active" : ""} key={item} onClick={() => setCategory(item)}>{item === "all" ? text.all : categoryLabel(item)}</button>)}</div>
          <label className="search-field"><span>⌕</span><input aria-label={text.search} placeholder={text.search} value={search} onChange={(event) => setSearch(event.target.value)} /></label>
        </div>
        {visiblePlaces.length ? <div className="timeline-list">{visiblePlaces.map((place, index) => (
          <button className="timeline-row" key={place.id} type="button" onClick={() => selectPlace(place)}>
            <span className="timeline-number">{String(place.route_order).padStart(2, "0")}</span>
            <span className="timeline-thumb">{photo(place.thumbnail_url || place.hero_image_url, local(place, "name", language))}</span>
            <span className="timeline-copy"><strong>{local(place, "name", language)}</strong><small>{place.built_year || categoryLabel(place.category)}</small></span>
            <span className="timeline-category">{categoryLabel(place.category)}</span>
            <span className="timeline-arrow">↗</span>
          </button>
        ))}</div> : <p className="empty-note">{text.noMatch}</p>}
      </main>
    );
  }

  function mapPage() {
    const selectedPosition = Math.max(0, places.findIndex((place) => place.slug === selectedSlug));
    return (
      <main className="page-shell map-page">
        <div className="page-heading map-heading"><div><span className="eyebrow">{text.route}</span><h1>{text.mapTitle}</h1><p>{text.mapSub}</p></div><span className="map-compass">N<span>✦</span></span></div>
        <div className="map-layout">
          <section className="route-map" aria-label={text.mapTitle}>
            <div className="map-graphics" style={{ transform: `scale(${mapZoom})` }}>
              <div className="map-paper" />
              <div className="map-blocks" aria-hidden="true">{Array.from({ length: 23 }, (_, i) => <span key={i} style={{ left: `${(i * 37) % 91}%`, top: `${(i * 53) % 89}%`, width: `${3 + (i % 5)}%`, height: `${2 + (i % 4)}%`, transform: `rotate(${i * 11}deg)` }} />)}</div>
              <svg className="route-path" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="M24 10 C30 20 32 25 39 34 S48 48 54 58 S65 77 74 88" /></svg>
              <span className="map-label north-label">{text.north}</span><span className="map-label south-label">{text.south}</span>
              {places.filter((place) => category === "all" || categoryGroup(place.category) === category).map((place) => {
                const index = (place.route_order || 1) - 1;
                const [x, y] = mapPositions[index % mapPositions.length];
                return <button key={place.id} className={`map-pin ${selectedSlug === place.slug ? "selected" : ""}`} style={{ left: `${x}%`, top: `${y}%` }} type="button" onClick={() => setSelectedSlug(place.slug)} aria-label={local(place, "name", language)}><span>{index + 1}</span></button>;
              })}
              <span className="map-scale">SCHEMATIC ROUTE · AL-MUIZZ STREET&nbsp; / &nbsp;HISTORIC CAIRO</span>
            </div>
            <div className="map-controls">
              <button type="button" aria-label="Zoom in" onClick={() => setMapZoom((zoom) => Math.min(zoom + 0.15, 1.6))}>＋</button>
              <button type="button" aria-label="Zoom out" onClick={() => setMapZoom((zoom) => Math.max(zoom - 0.15, 0.85))}>−</button>
              <button type="button" aria-label={text.route} onClick={() => setMapZoom(1)}>◎</button>
            </div>
          </section>
          <aside className="map-selection">
            {photo(activePlace?.hero_image_url || activePlace?.thumbnail_url, local(activePlace, "name", language), "map-preview")}
            <span className="eyebrow">{String(activePlace?.route_order || selectedPosition + 1).padStart(2, "0")} / {categoryLabel(activePlace?.category || "")}</span>
            <h2>{local(activePlace, "name", language)}</h2>
            <p>{local(activePlace, "built_date", language) || activePlace?.built_year}</p>
            <button className="green-button" type="button" onClick={() => activePlace && selectPlace(activePlace)}>{text.discover}<b>→</b></button>
          </aside>
          <div className="map-legend">{["all", "mosque", "madrasa", "palace", "gate"].map((item) => <button key={item} type="button" onClick={() => { setCategory(item); if (item !== "all" && activePlace?.category !== item) { const firstMatch = places.find((place) => categoryGroup(place.category) === item); if (firstMatch) setSelectedSlug(firstMatch.slug); } }} className={category === item ? "active" : ""}>{item === "all" ? text.all : categoryLabel(item)}</button>)}</div>
        </div>
      </main>
    );
  }

  function detailPage() {
    const tabs = ["overview", "history", "architecture", "details", "gallery", "location"];
    const tabContent = detailTab === "gallery" ? null : local(activePlace, detailTab, language);
    return (
      <main className="page-shell detail-page">
        <div className="breadcrumb"><button type="button" onClick={() => navigate("explore")}>{text.back}</button><span>›</span><span>{local(activePlace, "name", language)}</span></div>
        <section className="detail-hero">
          <div className="detail-cover">
            {photo(heroImage, local(activePlace, "name", language), "", true, 1280)}
            <div className="detail-cover-shade" />
            <div className="detail-title"><span className="eyebrow">{categoryLabel(activePlace?.category || "")} &nbsp;·&nbsp; {activePlace?.built_year} CE</span><span className="detail-arabic">{local(activePlace, "name", "ar")}</span><h1>{local(activePlace, "name", language)}</h1><p>{local(activePlace, "short_description", language)}</p></div>
            <button className="detail-story green-button" type="button" onClick={() => setDetailTab("history")}>▶ {text.story}</button><span className="detail-count">{String(activePlace?.route_order || 1).padStart(2, "0")} / {String(places.length).padStart(2, "0")}</span>
          </div>
          <div className="detail-facts">{[[text.built, local(activePlace, "built_date", language) || activePlace?.built_year], [text.period, local(activePlace, "period", language)], [text.patron, local(activePlace, "patron", language)], [text.locationLabel, local(activePlace, "location", language)]].filter((fact) => fact[1]).map(([label, value]) => <div key={label}><small>{label}</small><strong>{value}</strong></div>)}</div>
        </section>
        <nav className="detail-tabs" aria-label="Place information">{tabs.map((tab) => <button key={tab} type="button" className={detailTab === tab ? "active" : ""} onClick={() => setDetailTab(tab)}>{text[tab]}</button>)}</nav>
        <div className="detail-body">
          <section className="detail-reading">
            {detailTab === "gallery" ? <><span className="eyebrow">{text.gallery}</span><h2>{text.features}</h2><div className="detail-gallery">{images.map((image) => <button type="button" key={image.id} onClick={() => setActiveImage(image.image_url)}>{photo(image.image_url, local(image, "caption", language))}<span>{local(image, "caption", language)}</span></button>)}</div></> : <><span className="eyebrow">{text[detailTab]}</span><h2>{local(activePlace, "name", language)}</h2><p>{tabContent || text.answerFallback}</p>{detailTab === "overview" && local(activePlace, "history", language) && <p>{local(activePlace, "history", language)}</p>}{detailTab === "architecture" && activePlace?.features?.length > 0 && <div className="feature-cards">{activePlace.features.map((feature) => <article className="feature-card" key={feature.id}>{photo(feature.image_url, local(feature, "title", language))}<span className="feature-symbol">۞</span><h3>{local(feature, "title", language)}</h3><p>{local(feature, "description", language)}</p></article>)}</div>}</>}
          </section>
          <aside className="detail-aside"><span className="eyebrow">{text.features}</span>{(activePlace?.features || []).slice(0, 3).map((feature) => <article key={feature.id}><span>۞</span><div><h3>{local(feature, "title", language)}</h3><p>{local(feature, "description", language)}</p></div></article>)}{activePlace?.verification_url && <a href={activePlace.verification_url} target="_blank" rel="noreferrer">↗ {text.official}</a>}</aside>
        </div>
        <section className="related-section"><div className="section-title"><h2>{text.features}</h2><button type="button" onClick={() => navigate("stories")}>{text.viewAll} →</button></div><p className="feature-intro">{text.featureIntro}</p><div className="feature-cards">{(activePlace?.features || []).slice(0,3).map((feature,index) => <article className="feature-card" key={feature.id}>{photo(feature.image_url || images[index]?.image_url || heroImage, local(feature,"title",language))}<span className="feature-symbol">۞</span><h3>{local(feature,"title",language)}</h3><p>{local(feature,"description",language)}</p></article>)}</div><div className="section-title"><h2>{text.gallery}</h2></div><div className="detail-gallery">{images.map((image) => <button type="button" key={image.id} onClick={() => {setActiveImage(image.image_url); window.scrollTo({top:0,behavior:"smooth"});}}>{photo(image.image_url,local(image,"caption",language))}</button>)}</div></section>
      </main>
    );
  }

  function storiesPage() {
    return <main className="page-shell stories-page"><div className="page-heading"><div><span className="eyebrow">{text.eyebrow}</span><h1>{text.features}</h1><p>{text.featureIntro}</p></div></div><div className="story-grid">{places.slice(0, 8).map((place, index) => <button className="story-card" key={place.id} type="button" onClick={() => selectPlace(place)}>{photo(place.hero_image_url || place.thumbnail_url, local(place, "name", language))}<span className="story-card-shade" /><span className="story-card-index">{String(index + 1).padStart(2, "0")}</span><span className="story-card-copy"><small>{categoryLabel(place.category)}</small><strong>{local(place, "name", language)}</strong><span>{local(place, "architecture", language)}</span></span></button>)}</div></main>;
  }

  function aboutPage() {
    return <main className="page-shell about-page"><span className="eyebrow">{text.eyebrow}</span><h1>{text.aboutTitle}</h1><p>{text.aboutText}</p><div className="about-image">{photo(activePlace?.hero_image_url || activePlace?.thumbnail_url, local(activePlace, "name", language))}<span>القاهرة الفاطمية</span></div><button className="green-button" type="button" onClick={() => navigate("explore")}>{text.discover}<b>→</b></button></main>;
  }

  function guidePage() {
    const prompts = [text.prompt1, text.prompt2, text.prompt3, text.prompt4];
    return <main className="page-shell guide-page"><section className="guide-art">{photo("/images/lantern.png", "Illustrated brass lantern in historic Cairo")}</section><section className="guide-content"><span className="eyebrow">AL-MUIZZ · FATIMID CAIRO</span><span className="guide-arabic" lang="ar">اسأل دليلك التاريخي</span><h1>{text.ask}</h1><p>{text.askSub}</p><div className="chat-thread">{conversation.length > 0 && <div className="guide-message">{text.guideIntro}</div>}{conversation.map((item, index) => <React.Fragment key={index}><div className="user-message">{item.question}</div><div className="guide-message">{item.answer}</div></React.Fragment>)}</div><div className="prompt-list">{prompts.map((prompt) => <button key={prompt} type="button" onClick={() => sendQuestion(prompt)}><span>✧</span>{prompt}<b>›</b></button>)}</div><form className="chat-form" onSubmit={(event) => { event.preventDefault(); sendQuestion(); }}><input value={question} onChange={(event) => setQuestion(event.target.value)} placeholder={text.input} aria-label={text.input} /><button type="submit" aria-label={text.send}>➤</button></form><small className="guide-footnote">{isArabic ? "إجابات من محتوى الدليل المحفوظ" : "Answers from the guide’s saved monument content"}</small></section></main>;
  }

  function body() {
    if (loading) return <main className="loading-screen"><span className="loading-rosette">۞</span><p>{text.loading}</p></main>;
    if (error) return <main className="error-screen"><h1>{text.error}</h1><button className="green-button" type="button" onClick={() => setRetry((value) => value + 1)}>{text.retry}</button></main>;
    if (page === "landing") return landing();
    if (page === "home") return overview();
    if (page === "explore") return explore();
    if (page === "map") return mapPage();
    if (page === "detail") return detailPage();
    if (page === "stories") return storiesPage();
    if (page === "about") return aboutPage();
    return guidePage();
  }

  return <div className={`experience ${isArabic ? "arabic" : ""}`} dir={isArabic ? "rtl" : "ltr"}>{header()}{body()}<footer className="site-footer"><span>AL-MUIZZ · CAIRO</span><span>{text.north} &nbsp;—&nbsp; {text.south}</span><button type="button" onClick={() => navigate("guide")}>{text.ask} ↗</button></footer></div>;
}

export default App;
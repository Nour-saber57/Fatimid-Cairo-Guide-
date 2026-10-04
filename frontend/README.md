# Al-Muizz frontend

Run `npm install` and `npm run dev` inside this folder. The frontend opens at http://localhost:5173. Run `npm run build` to create the production files in `dist`.

The development server proxies `/api` requests to FastAPI at http://127.0.0.1:8000. If the API is offline or has no monuments, the guide uses the bundled snapshot of the existing backend seed data. No database migration is required for the visual redesign.

## AI historical guide

The guide sends chat requests through FastAPI to Gemini. Set your API key in the backend terminal before starting the API; do not put the key in frontend code:

```powershell
$env:GEMINI_API_KEY = "your_gemini_api_key"
$env:GEMINI_MODEL = "gemini-2.5-flash"
uvicorn main:app --reload
```

Run these commands from `backend`. `GEMINI_MODEL` is optional; the backend defaults to `gemini-2.5-flash`. The backend keeps the key private. If a key was pasted into chat or another shared log, revoke it and use a replacement.

The entrance, street, lantern and map backgrounds in `public/images` are generated illustrations. Monument images come from the existing Wikimedia Commons records; unavailable images use the street illustration as a fallback. The map is an interactive schematic, not a geographic navigation map. The story button opens the history tab.

Pages include entrance, home, timeline, interactive route, monument details with features and gallery, stories, about and the historical guide. English and Arabic, category filtering, search, map selection/zoom and image selection are supported. Layouts adapt to mobile screens.

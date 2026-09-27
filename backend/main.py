from fastapi import FastAPI

from database.database import Base, engine
from models.place import Place
from routers.places import router as places_router


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(places_router)


@app.get("/health")
def health():
    return {"status": "backend is healthy"}
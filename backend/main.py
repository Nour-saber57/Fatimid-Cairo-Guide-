from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI

from database.database import Base, engine

from models.place import Place
from models.features import Feature
from models.images import PlaceImage

from routers.places import router as places_router
from routers.features import router as features_router
from routers.images import router as images_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(places_router)
app.include_router(features_router)
app.include_router(images_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "backend is healthy"}
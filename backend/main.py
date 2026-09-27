from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI

from database.database import Base, engine
from routers.places import router as places_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(places_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "backend is healthy"}
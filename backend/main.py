from fastapi import FastAPI

from database.database import Base, engine
from models.place import Place


Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "backend is healthy"}
from pathlib import Path

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from collections.abc import Generator

DATABASE_PATH = Path(__file__).resolve().parents[1] / "fatimid_cairo.db"
DATABASE_URL = URL.create("sqlite", database=str(DATABASE_PATH))
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
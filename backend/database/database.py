from sqlalchemy import MetaData, create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./fatimid_cairo.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


def initialize_database() -> None:
    from models.place import Place

    inspector = inspect(engine)
    if "places" in inspector.get_table_names():
        columns = {column["name"] for column in inspector.get_columns("places")}
        if "name_en" in columns:
            target_columns = [column.name for column in Place.__table__.columns]
            alternate_sources = {
                "name": ("name", "name_en"),
                "built_year": ("built_year", "year"),
            }

            def source_expression(column: str) -> str:
                candidates = alternate_sources.get(column, (column,))
                source = next((name for name in candidates if name in columns), None)
                return f'"{source}"' if source is not None else "NULL"

            with engine.begin() as connection:
                connection.execute(text("ALTER TABLE places RENAME TO places_legacy"))
                migrated_table = Place.__table__.to_metadata(
                    MetaData(), name="places_new"
                )
                migrated_table.create(connection)

                target_list = ", ".join(f'"{column}"' for column in target_columns)
                source_list = ", ".join(
                    source_expression(column) for column in target_columns
                )
                connection.execute(
                    text(
                        f"INSERT INTO places_new ({target_list}) "
                        f"SELECT {source_list} FROM places_legacy"
                    )
                )
                connection.execute(text("DROP TABLE places_legacy"))
                connection.execute(text("ALTER TABLE places_new RENAME TO places"))

    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
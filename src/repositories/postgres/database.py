from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.settings.settings import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = f"postgresql://" \
                          f"{settings.db_username}:" \
                          f"{settings.db_password}@" \
                          f"{settings.db_host}:" \
                          f"{settings.db_port}/" \
                          f"{settings.db_database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

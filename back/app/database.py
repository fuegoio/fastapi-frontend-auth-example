from typing import Generator

from sqlalchemy import MetaData, create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative.api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from app.settings import settings

SQLALCHEMY_DATABASE_URL = settings.db_uri

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_N_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

BaseMeta = DeclarativeMeta
SQLBase = declarative_base(metadata=meta, metaclass=BaseMeta)


class Base(SQLBase):
    __abstract__ = True

    def to_dict(self):
        return {
            col.key: getattr(self, col.key) for col in inspect(self).mapper.column_attrs
        }


# Dependency
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

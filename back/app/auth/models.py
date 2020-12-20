from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True, nullable=False)
    name = Column(String)
    email = Column(String)
    picture = Column(String)

    def get_display_name(self) -> str:
        return self.name if self.name is not None else self.login

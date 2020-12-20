from typing import List, Optional

from sqlalchemy.orm import Session

from .schemas import GithubUser
from .models import User


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter_by(id=user_id).first()


def get_user_by_login(db: Session, login: str) -> Optional[User]:
    return db.query(User).filter_by(login=login).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, github_user: GithubUser) -> User:
    user = User(
        login=github_user.login,
        name=github_user.name,
        email=github_user.email,
        picture=github_user.avatar_url,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


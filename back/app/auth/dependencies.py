import jwt
from fastapi import Header, HTTPException, status
from fastapi.security.utils import get_authorization_scheme_param
from pydantic import ValidationError

from app.settings import settings

from .schemas import User


def get_user_from_header(*, authorization: str = Header(None)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    scheme, token = get_authorization_scheme_param(authorization)
    if scheme.lower() != "bearer":
        raise credentials_exception

    try:
        payload = jwt.decode(
            token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm]
        )
        try:
            token_data = User(**payload)
            return token_data
        except ValidationError:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

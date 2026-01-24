from app.Servises.config import secret_key, algoritm

from jose import jwt, JWTError
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status


password_hasher = PasswordHash(
    hashers=[
        Argon2Hasher(),
    ]
)


def veryfication_password(plain_password: str, hashed_password: str) -> bool:
    return password_hasher.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_hasher.hash(password)


def create_access_token(data: dict, expires_delt: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delt or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=algoritm)


def veryfication_access_toke(token: str) -> str:
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algoritm])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validation credentails",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user_for_token(token: str) -> str:
    payload = veryfication_access_toke(token)
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentails",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return username
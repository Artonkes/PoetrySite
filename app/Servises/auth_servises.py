from app.Servises.config import secret_key, algoritm

from jose import jwt, JWTError
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from datetime import datetime, timedelta, timezone


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

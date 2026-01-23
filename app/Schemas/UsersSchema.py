from pydantic import BaseModel, Field
from typing import Optional

#schema for user
class UsersRegistration(BaseModel):
    name: str = Field()
    password: str = Field()


class UsersData(BaseModel):
    age: Optional[int]
    poetry: str


class UsersUpdata(BaseModel):
    name: Optional[str]
    password: Optional[str]

#Schema to token for user
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenDate(BaseModel):
    username: str | None = None

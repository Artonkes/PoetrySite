from pydantic import BaseModel, Field
from typing import Optional

class UsersRegistration(BaseModel):
    name: str = Field()
    password: str = Field()


class UsersData(BaseModel):
    age: Optional[int]
    poetry: str


class UsersUpdata(BaseModel):
    name: Optional[str]
    password: Optional[str]
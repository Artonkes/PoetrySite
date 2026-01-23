from pydantic import BaseModel, Field
from typing import Optional


class PoetrySchema(BaseModel):
    name: str = Field()
    text: str = Field()
    author_id: int = Field()

class PoetryUpdate(BaseModel):
    name: Optional[str] = Field()
    text: Optional[str] = Field()
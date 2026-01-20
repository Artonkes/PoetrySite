from app.DataBase.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, Text, DateTime
from datetime import datetime

class UsersModel(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    #poetry: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime] = mapped_column(DateTime)
    update_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    


class PoetryModel(Base):
    __tablename__ = "Poetry"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(ForeignKey("Users.name"))
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    update_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
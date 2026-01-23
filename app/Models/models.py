from app.DataBase.database import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.sql import func 
from datetime import datetime

class UsersModel(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    poetry = relationship("PoetryModel", back_populates='author', cascade="all, delete-orphan")
    create_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), default=func.now())
    


class PoetryModel(Base):
    __tablename__ = "Poetry"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("Users.id"), nullable=False)
    author = relationship("UsersModel", back_populates="poetry")
    create_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), default=func.now())
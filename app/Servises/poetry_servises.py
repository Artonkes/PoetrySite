from app.Models.models import PoetryModel

from sqlalchemy import select
from datetime import datetime
from fastapi import HTTPException


async def get_all_poetry(session):
    result = await session.execute(select(PoetryModel))
    poetry = result.scalars().all()
    return poetry


async def get_id(session, poetry_id: int):
    result = await session.execute(
        select(PoetryModel).where(PoetryModel.id == poetry_id)
    )

    poetry = result.scalar_one_or_none()

    if poetry is None:
        raise HTTPException(status_code=401, detail="Poetry is found")

    return poetry


async def create(session, poetry):
    result = await session.execute(
        select(PoetryModel).where(PoetryModel.name == poetry.name)
    )
    existing_poetry = result.scalars().first()

    if existing_poetry:
        raise HTTPException(status_code=401, detail="Poetry is found")

    now = datetime.utcnow()
    new_poetry = PoetryModel(
        name=poetry.name,
        text=poetry.text,
        author=poetry.author,
        create_at=now,
        update_at=now,
    )

    session.add(new_poetry)
    await session.commit()
    await session.refresh(new_poetry)
    return new_poetry


async def update(session, poetry_id: int, poetry_update):
    result = await session.execute(
        select(PoetryModel).where(PoetryModel.id == poetry_id)
    )
    db_poetry = result.scalars().first()

    if db_poetry is None:
        raise HTTPException(status_code=404, detail="Poetry is not found")

    update_data = poetry_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        if key == "updated_at":
            continue
        setattr(db_poetry, key, value)

    db_poetry.updated_at = datetime.now()

    await session.commit()
    await session.refresh(db_poetry)
    return db_poetry


async def delete(session, poetry_id: int):
    qwe = await session.execute(select(PoetryModel).where(PoetryModel.id == poetry_id))
    result = qwe.scalar_one_or_none()

    if result is None:
        raise HTTPException(status_code=404, detail="Poetry is not found")

    await session.delete(result)
    await session.commit()

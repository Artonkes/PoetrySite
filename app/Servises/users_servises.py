from app.Models.models import UsersModel
from app.DataBase.crud import CRUD

from sqlalchemy import select
from datetime import datetime
from fastapi import HTTPException



async def get_all_users(session):
    user = CRUD(session=session)
    return user.get_all_data()


async def get_id(session, user_id: int):
    result = await session.execute(
        select(UsersModel).where(UsersModel.id == user_id)
    )
    
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User is not found")

    return user


async def create(session, user):
    result = await session.execute(
        select(UsersModel).where(UsersModel.name == user.name)
    )
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=401, detail="User is found")

    now = datetime.utcnow()
    new_user = UsersModel(
        name = user.name,
        password = user.password,
        create_at = now,
        update_at = now,
    )
    
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def authorization_user(session, user):
    result = await session.execute(
        select(UsersModel).where(UsersModel.name == user.name).where(UsersModel.password == user.password)
    )
    existing_user = result.scalars().first()

    if existing_user is None:
        raise HTTPException(status_code=401, detail="User is not found")

    return {
        "user_id": existing_user.id,
        "username": existing_user.name,
    }


async def update(session, user_id: int, user_update):
    result = await session.execute(
        select(UsersModel).where(UsersModel.id == user_id)
    )
    db_user = result.scalars().first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User is not found")
    
    update_data = user_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        if key == "updated_at":
            continue
        setattr(db_user, key, value)
    
    db_user.updated_at = datetime.now()
    
    await session.commit()
    await session.refresh(db_user)
    return db_user


async def delete(session, user_id: int):
    qwe = await session.execute(
        select(UsersModel).where(UsersModel.id == user_id)
    )
    result = qwe.scalar_one_or_none()

    if result is None:
        raise HTTPException(status_code=404, detail="User is not found")

    await session.delete(result)
    await session.commit()
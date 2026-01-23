from app.Models.models import UsersModel
from app.DataBase.crud import CRUDBase

from app.Servises.auth_servises import veryfication_password, get_password_hash, create_access_token

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

user = CRUDBase(model=UsersModel)


async def get_all_id(session):
    return await user.get_all(session=session)


async def get_by_id(session, id):
    return await user.get_by_id(session=session, id=id)


async def create(session, schema):
    try:
        hash_password = get_password_hash(schema.password)

        user_data = {
            "name": schema.name,
            "password": hash_password
        }

        return await user.create(session=session, obj_in=user_data)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail="User is found")


async def authorization(session, schema):
    query = await session.execute(
        select(UsersModel).where(UsersModel.name == schema.name)
    )
    user_data = query.scalar_one_or_none()

    if user_data is None:
        raise HTTPException(status_code=401, detail="User is not found")

    if not veryfication_password(schema.password, user_data.password):
        raise HTTPException(status_code=401, detail="Invilid password")

    access_token = create_access_token(data={"sub": user_data.name})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user_data.id,
        "name": user_data.name,
    }

async def update(session, id, obj):
    try:
        if 'password' in obj and obj['password']:
            obj['password'] = get_password_hash(obj['password'])

        return await user.update(session=session, id=id, obj_in=obj)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail="User is found")


async def delete(session, id):
    return await user.delete(session=session, id=id)
    
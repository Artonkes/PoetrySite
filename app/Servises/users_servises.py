from app.Models.models import UsersModel
from app.DataBase.crud import CRUDBase

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

user = CRUDBase(model=UsersModel)


async def get_all_id(session):
    return await user.get_all(session=session)


async def get_by_id(session, id):
    return await user.get_by_id(session=session, id=id)


async def create(session, schema):
    try:
        return await user.create(session=session, obj_in=schema)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail="User is found")


async def update(session, id, obj):
    try:
        return await user.update(session=session, id=id, obj_in=obj)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail="User is found")


async def delete(session, id):
    return await user.delete(session=session, id=id)
    
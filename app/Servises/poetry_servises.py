from app.Models.models import PoetryModel
from app.DataBase.crud import CRUDBase

poetry = CRUDBase(model=PoetryModel)


async def get_all_id(session):
    return await poetry.get_all(session=session)


async def get_by_id(session, id):
    return await poetry.get_by_id(session=session, id=id)


async def create(session, schema):
    return await poetry.create(session=session, obj_in=schema)


async def update(session, id, obj):
    return await poetry.update(session=session, id=id, obj_in=obj)


async def delete(session, id):
    return await poetry.delete(session=session, id=id)
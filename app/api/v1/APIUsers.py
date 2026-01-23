from fastapi import APIRouter

from app.Schemas.UsersSchema import UsersRegistration, UsersUpdata
from app.DataBase.database import SessionDepend
# from app.Models.models import UsersModel
from app.Servises.users_servises import create, get_by_id, get_all_id, delete, update

router = APIRouter(
    prefix="/api/users/v1",
    tags=["Users"]
)

@router.post("/registration/")
async def registration(user: UsersRegistration, session: SessionDepend,):
    new_user = await create(session=session, schema=user.model_dump())
    return {"detail": new_user}


# @router.post("/authorization/")
# async def authorizations(session: SessionDepend, user=UsersRegistration):
#     user = authorization_user(session=session, user=user)
#     return {"detail": "Succes"}


@router.get("/get/{user_id}/")
async def get_user_by_id(user_id: int, session: SessionDepend):
    user = await get_by_id(session=session, id=user_id)
    return {"detail": user}


@router.get("/get_all_users/")
async def get_all(session: SessionDepend):
    users = await get_all_id(session=session)
    return {"detail": users}


@router.put("/update/{user_id}/")
async def update_user(session: SessionDepend, user_id: int, user_update: UsersUpdata):
    user = await update(session=session, id=user_id, obj=user_update.model_dump())
    return {"detail": user}


@router.delete("/delete/{user_id}/")
async def delete_user(user_id: int, session: SessionDepend):
    await delete(session=session, id=user_id)
    return {"detail": "User deleted"}
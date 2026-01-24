from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.Schemas.UsersSchema import UsersRegistration, UsersUpdata
from app.DataBase.database import SessionDepend
from app.Servises.users_servises import create, get_by_id, get_all_id, delete, update, authorization
from app.Servises.auth_servises import get_current_user_for_token

router = APIRouter(
    prefix="/api/users/v1",
    tags=["Users"]
)

security = HTTPBearer()


async def get_current_user(credentails: HTTPAuthorizationCredentials = Depends(security)) -> str:
    token = credentails.credentials
    return get_current_user_for_token(token)


@router.post("/registration/")
async def registration(user: UsersRegistration, session: SessionDepend):
    new_user = await create(session=session, schema=user)
    return {"detail": new_user}


@router.post("/authorization")
async def authorization_user(user: UsersRegistration, session: SessionDepend):
    user = await authorization(session=session, schema=user)
    return {"detail": user}


@router.get("/me/")
async def get_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}


@router.get("/profile/")
async def get_profile(session: SessionDepend, current_user: str = Depends(get_current_user)):
    return {"username": current_user}


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
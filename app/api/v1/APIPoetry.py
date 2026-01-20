from fastapi import APIRouter

from app.Schemas.PoetrySchema import PoetrySchema, PoetryUpdate
from app.DataBase.database import SessionDepend

from app.Servises.poetry_servises import create, get_id, get_all_poetry, delete, update

router = APIRouter(prefix="/api/poetry/v1", tags=["Poetry"])


@router.post("/registration/")
async def registration(poetry: PoetrySchema, session: SessionDepend):
    new_poetry = await create(session=session, poetry=poetry)
    return {"detail": new_poetry}


@router.get("/get/{poetry_id}/")
async def get_poetry_by_id(poetry_id: int, session: SessionDepend):
    poetry = await get_id(session=session, poetry_id=poetry_id)
    return {"detail": poetry}


@router.get("/get_all_poetry/")
async def get_all(session: SessionDepend):
    poetry = await get_all_poetry(session=session)
    return {"detail": poetry}


@router.put("/update/{poetry_id}/")
async def update_poetry(
        session: SessionDepend, poetry_id: int, poetry_update: PoetryUpdate
    ):
    
    poetry = await update(
        session=session, poetry_id=poetry_id, poetry_update=poetry_update
    )

    return {"detail": poetry}


@router.delete("/delete/{poetry_id}/")
async def delete_poetry(poetry_id: int, session: SessionDepend):
    await delete(session=session, poetry_id=poetry_id)
    return {"detail": "Poetry deleted"}

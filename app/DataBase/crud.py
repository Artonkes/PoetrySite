from sqlalchemy import select
from fastapi import HTTPException
from typing import Optional


class CRUD:
    def __init__(self, id: Optional[int], query: Optional[str], session: Optional[str], model: Optional[str]):
        self.id = id
        self.query = query
        self.session = session
        self.model = model

    async def get_all_data(self):
        result = await self.session.execute(
            select(self.model)
        )
        data = result.scalars().all()
        return data


    async def get_id(self):
        result = await self.session.execute(
            select(self.model).where(self.model.id == self.id)
        )
        
        user = result.scalar_one_or_none()

        if user is None:
            raise HTTPException(status_code=401, detail="User is found")

        return user
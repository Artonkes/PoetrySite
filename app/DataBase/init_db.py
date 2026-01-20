import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataBase.database import Base, engine

from Models.models import UsersModel, PoetryModel

import asyncio

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        print("✅ База данных успешно инициализирована!")
        print("📊 Созданы таблицы:", [table for table in Base.metadata.tables.keys()])

asyncio.run(init_db())
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from aplicacao.models.models import Insumo
from aplicacao.schema.schema import InsumoUpdate


async def create(db: AsyncSession, new_data: dict):
    new_data = Insumo(**new_data)
    db.add(new_data)
    await db.commit()
    await db.refresh(new_data)
    return new_data


async def get(db: AsyncSession, idx: int):
    command = (select(Insumo)
               .where(Insumo.id == idx))
    result = await db.execute(command)
    return result.scalar_one_or_none()


async def get_all(db: AsyncSession, skip: int = 0, limit: int = 100):
    command = (select(Insumo)
               .offset(skip)
               .limit(limit))
    result = await db.execute(command)
    return list(result.scalars().all())


async def update(db: AsyncSession, idx: int):
    data = await get(db, idx)
    if data:
        update_data = InsumoUpdate.__dict__
        for key,value in update_data.items():
            setattr(data, key, value)
        await db.commit()
        await db.refresh(data)
        return data
    return None


async def delete(db: AsyncSession, item_id: int):
    data = await get(db, item_id)
    if data:
        await db.delete(data)
        await db.commit()
        return True
    return None

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from aplicacao.repository.insumo_repository import create, get, get_all, update, delete
from aplicacao.schema.schema import InsumoCreate


async def create_insumo(db: AsyncSession, item: InsumoCreate):
    return await create(db, item.model_dump())


async def get_insumo(db: AsyncSession, item_id: int):
    insumo = await get(db, item_id)
    if not insumo:
        raise HTTPException(status_code=404, detail='Insumo não encontrado')
    return insumo


async def get_all_insumo(db: AsyncSession):
    return await get_all(db)


async def update_insumo(db: AsyncSession, item_id: int):
    insumo = await get(db, item_id)
    if not insumo:
        raise HTTPException(status_code=404, detail='Insumo não encontrado')
    return await update(db, item_id)


async def delete_insumo(db: AsyncSession, item_id: int):
    insumo = await get(db, item_id)
    if not insumo:
        raise HTTPException(status_code=404, detail='Insumo não encontrado')
    return await delete(db, item_id)

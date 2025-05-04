from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from aplicacao.repository.equipamento_repostitory import create, get, get_all, update, delete
from aplicacao.schema.schema import EquipamentoCreate
from aplicacao.service.departamento_service import get_departamento


async def create_equipamento(db: AsyncSession, item: EquipamentoCreate):
    departamento = await get_departamento(db, item.departamento_id)
    if not departamento:
        raise HTTPException(status_code=404, detail='Departamento não encontrado')
    return await create(db, item.model_dump())


async def get_equipamento(db: AsyncSession, item_id: int):
    equipamento = await get(db, item_id)
    if not equipamento:
        raise HTTPException(status_code=404, detail='Equipamento não encontrado')
    return equipamento


async def get_all_equipamentos(db: AsyncSession):
    return await get_all(db)


async def update_equipamento(db: AsyncSession, item_id: int):
    equipamento = await get(db, item_id)
    if not equipamento:
        raise HTTPException(status_code=404, detail='Equipamento não encontrado')
    return await update(db, item_id)


async def delete_equipamento(db: AsyncSession, item_id: int):
    equipamento = await get(db, item_id)
    if not equipamento:
        raise HTTPException(status_code=404, detail='Equipamento não encontrado')
    return await delete(db, item_id)

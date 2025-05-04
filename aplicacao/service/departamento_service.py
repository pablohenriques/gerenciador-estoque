from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from aplicacao.repository.departamento_repository import create, get, get_all, update, delete
from aplicacao.schema.schema import DepartamentoCreate, DepartamentoUpdate


async def create_departamento(db: AsyncSession, item: DepartamentoCreate):
    return await create(db, item.model_dump())


async def get_departamento(db: AsyncSession, item_id: int):
    departamento = await get(db, item_id)
    if departamento:
        raise HTTPException(status_code=404, detail='Departamento não encontrado')
    return departamento


async def get_all_departamento(db: AsyncSession):
    return await get_all(db)


async def edit_departamento(db: AsyncSession, item_id: int, item: DepartamentoUpdate):
    departamento = await get(db, item_id)
    if departamento:
        raise HTTPException(status_code=404, detail='Departamento não encontrado')
    return await update(db, item_id)


async def delete_departamento(db: AsyncSession, item_id: int):
    departamento = await get(db, item_id)
    if departamento:
        raise HTTPException(status_code=404, detail='Departamento não encontrado')
    return await delete(db, item_id)

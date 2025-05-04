from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

import aplicacao.service.insumo_service as service
from aplicacao.config import database
from aplicacao.schema.schema import InsumoCreate, Insumo

route = APIRouter(prefix='/insumo', tags=['insumo'])


@route.post('/create', response_model=InsumoCreate)
async def create(item: InsumoCreate, db: AsyncSession = Depends(database.get_db_session)):
    return await service.create_insumo(db, item)


@route.get('/get', response_model=Insumo)
async def get(item_id: int, db: AsyncSession = Depends(database.get_db_session)):
    return await service.get_insumo(db, item_id)


@route.get('/getall', response_model=list[Insumo])
async def get_all(db: AsyncSession = Depends(database.get_db_session)):
    return await service.get_all_insumo(db)


@route.put('/update', response_model=Insumo)
async def update(item_id: int, db: AsyncSession = Depends(database.get_db_session)):
    return await service.update_insumo(db, item_id)


@route.delete('/delete', response_model=bool)
async def delete(item_id: int, db: AsyncSession = Depends(database.get_db_session)):
    return await service.delete_insumo(db, item_id)

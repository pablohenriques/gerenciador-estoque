from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

import aplicacao.service.equipamento_service as service
from aplicacao.config import database
from aplicacao.schema.schema import Equipamento, EquipamentoCreate, EquipamentoUpdate

route = APIRouter(prefix='/equipament', tags=['equipament'])


@route.post('/create', response_model=EquipamentoCreate)
async def create(item: EquipamentoCreate, db: AsyncSession = Depends(database.get_db_session)):
    return await service.create_equipamento(db, item)


@route.get('/get', response_model=Equipamento)
async def get(item_id: int, db: AsyncSession = Depends(database.get_db_session)):
    return await service.get_equipamento(db, item_id)


@route.get('/getall', response_model=list[Equipamento])
async def get_all(db: AsyncSession = Depends(database.get_db_session)):
    return await service.get_all_equipamentos(db)


@route.put('/update', response_model=Equipamento)
async def update(item_id: int, db: AsyncSession = Depends(database.get_db_session)):
    return await service.update_equipamento(db, item_id)


@route.delete('/delete', response_model=bool)
async def delete(item_id: int, db: AsyncSession = Depends(database.get_db_session)):
    return await service.delete_equipamento(db, item_id)

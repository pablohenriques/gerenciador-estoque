from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

import aplicacao.service.departamento_service as service
from aplicacao.config import database
from aplicacao.schema.schema import Departamento, DepartamentoCreate, DepartamentoUpdate

route = APIRouter(prefix='/departamento', tags=['departamento'])


@route.post('/create', response_model=DepartamentoCreate)
async def create(item: DepartamentoCreate, db: AsyncSession = Depends(database.get_db_session)):
    return await service.create_departamento(db, item)


@route.get('/get', response_model=Departamento)
async def get(item_id: int, db: AsyncSession = Depends(database.get_db_session)):
    return await service.get_departamento(db, item_id)


@route.get('/getall', response_model=list[Departamento])
async def get_all(db: AsyncSession = Depends(database.get_db_session)):
    return  await service.get_all_departamento(db)


@route.put('/update', response_model=Departamento)
async def update(item_id: int, item: DepartamentoUpdate, db: AsyncSession = Depends(database.get_db_session)):
    return await service.edit_departamento(db, item_id, item)


@route.delete('/delete', response_model=bool)
async def delete(item_id: int, db: AsyncSession = Depends(database.get_db_session)):
    return await service.delete_departamento(db, item_id)
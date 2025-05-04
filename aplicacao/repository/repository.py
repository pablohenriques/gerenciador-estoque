from typing import Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from aplicacao.models.models import Equipamento

T = TypeVar('T')


async def create_item(db: AsyncSession, item: dict, model_type: Type[T]):
    db_item = model_type(**item)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def get_item(db: AsyncSession, item_id, model_type: Type[T]):
    result = await db.get(model_type, item_id)
    return result


async def get_item_equip(db: AsyncSession, item_id, model_type: Type[T]):
    stmt = select(model_type).where(model_type.id == item_id).options(selectinload(model_type.insumos))
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_items_equip(db: AsyncSession, model_type: Type[T], skip: int = 0, limit: int = 100):
    stmt = select(model_type).offset(skip).limit(limit).options(selectinload(model_type.insumos))
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def get_item_dpto(db: AsyncSession, item_id: int, model_type: Type[T], model_type_sub: Type[T]):
    stmt = select(model_type).where(model_type.id == item_id).options(selectinload(model_type.equipamentos).selectinload(model_type_sub.insumos))
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_items(db: AsyncSession, model_type: Type[T], skip: int = 0, limit: int = 100):
    stmt = select(model_type).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return list(result.scalars().all())

async def get_items_dpto(db: AsyncSession, model_type: Type[T], model_type_sub: Type[T], skip: int = 0, limit: int = 100):
    stmt = select(model_type).offset(skip).limit(limit).options(selectinload(model_type.equipamentos).selectinload(model_type_sub.insumos))
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def update_item(db: AsyncSession, item_id: int, schema_type: Type[T], model_type: Type[T]):
    db_item = await get_item(db, item_id, model_type)
    if db_item:
        update_data = schema_type.model_dump(exclude_unset=True)
        for key,value in update_data.items():
            setattr(db_item, key, value)
        await db.commit()
        await db.refresh(db_item)
        return db_item
    return None


async def update_item_dpto(db: AsyncSession, item_id: int, schema_type: Type[T], model_type: Type[T]):
    db_item = await get_item_dpto(db, item_id, model_type, Equipamento)
    if db_item:
        update_data = schema_type.model_dump(exclude_unset=True)
        for key,value in update_data.items():
            setattr(db_item, key, value)
        await db.commit()
        await db.refresh(db_item)
        return db_item
    return None


async def delete_item(db: AsyncSession, item_id: int, model_type: Type[T]):
    db_item = await get_item(db, item_id, model_type)
    if db_item:
        await db.delete(db_item)
        await db.commit()
        return True
    return None

async def delete_item_dpto(db: AsyncSession, item_id: int, model_type: Type[T]):
    db_item = await get_item_dpto(db, item_id, model_type, Equipamento)
    if db_item:
        await db.delete(db_item)
        await db.commit()
        return True
    return None

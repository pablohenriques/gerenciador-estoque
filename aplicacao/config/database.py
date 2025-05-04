import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv('database', 'sqlite+aiosqlite:///.test.db')
echo=True

async_engine = create_async_engine(database_url, echo=True)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


async def create_database_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db_session():
    async with async_session_factory() as session:
        try:
            yield session
            # await session.commit()
        except Exception:
            await session.rollback()
            raise
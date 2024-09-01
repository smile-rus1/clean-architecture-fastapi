from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.config import DBConfig
from src.infrastructure.database.utils.connection_sting_maker import make_connection_sting


def get_db_connection(db_config: DBConfig):
    engine = create_async_engine(make_connection_sting(db_config))
    maker = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    return maker

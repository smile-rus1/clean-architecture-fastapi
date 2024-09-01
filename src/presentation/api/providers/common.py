from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.api.presenter.presenters.build_presenter import build_presenter
from src.infrastructure.database.connections import get_db_connection
from src.infrastructure.database.uow.build_uow import build_uow
from src.infrastructure.database.uow.uow import UoW
from src.infrastructure.hasher import Hasher
from src.infrastructure.mapper.build_mapper import build_mapper
from src.infrastructure.mapper.mapper import Mapper
from src.presentation.api.presenter.presenter import Presenter
from src.presentation.api.providers.abstract.common import session_provider, mapper_provider
from src.presentation.config.config import Config


def db_session(config: Config):
    sessionmaker = get_db_connection(config.db)

    async def get_db_session() -> AsyncSession:
        async with sessionmaker() as session:
            yield session

    return get_db_session


def mapper_getter() -> Mapper:
    mapper = build_mapper()
    return mapper


def presenter_getter() -> Presenter:
    presenter = build_presenter()
    return presenter


def uow_getter(
        session: AsyncSession = Depends(session_provider),
        mapper: Mapper = Depends(mapper_provider)
) -> UoW:
    return build_uow(
        session=session,
        mapper=mapper
    )


def hasher_getter() -> Hasher:
    return Hasher()

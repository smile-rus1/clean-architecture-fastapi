from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.interfaces.mapper import IMapper
from src.infrastructure.database.uow.uow import UoW

from src.infrastructure.database import repo


def build_uow(session: AsyncSession, mapper: IMapper) -> UoW:
    return UoW(
        session=session,
        mapper=mapper,
        user_repo=repo.UserRepo,
        user_reader=repo.UserReader
    )

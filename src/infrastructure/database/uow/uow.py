from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.interfaces.mapper import IMapper
from src.application.user.interfaces.repo.user_repo import IUserRepo, IUserReader
from src.infrastructure.database.uow.base import BaseUoW


class UoW(BaseUoW):
    user_repo: IUserRepo
    user_reader: IUserReader

    def __init__(
            self,
            session: AsyncSession,
            mapper: IMapper,
            user_repo: Type[IUserRepo],
            user_reader: Type[IUserReader]
    ):
        super().__init__(session=session)
        self.user_repo = user_repo(session=session, mapper=mapper)
        self.user_reader = user_reader(session=session, mapper=mapper)

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.interfaces.mapper import IMapper
from src.infrastructure.database.repo.common.exceptions.database_exceptions import InvalidID, LimitError, OffSetError


class SQLAlchemyRepo:
    def __init__(self, session: AsyncSession, mapper: IMapper):
        self._session = session
        self._mapper = mapper

    @staticmethod
    def _validate_id(model_id: int, field: str):
        if model_id <= 0:
            raise InvalidID(field)

    @staticmethod
    def _validate_limit_offset(limit: int, offset: int):
        if limit <= 0:
            raise LimitError()
        elif offset < 0:
            raise OffSetError()

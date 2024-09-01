from sqlalchemy import Select, select, asc, func

from src.infrastructure.database.models.user import UserDB
from src.infrastructure.database.repo.common.base_query_builder import BaseQueryBuilder


class GetUserQuery(BaseQueryBuilder):
    def get_query(
            self,
            first_name: str,
            last_name: str,
            email: str,
            limit: int,
            offset: int
    ) -> Select:
        return (
            self._select(offset, limit)
            ._with_first_name(first_name)
            ._with_last_name(last_name)
            ._with_email(email)
            ._build()
        )

    def _select(self, offset: int, limit: int):
        self._query = select(UserDB).order_by(asc(UserDB.id)).offset(offset).limit(limit)
        return self

    def _with_first_name(self, first_name: str):
        if first_name:
            self._query = self._query.where(func.lower(UserDB.first_name).like(func.lower(f"%{first_name}%")))
        return self

    def _with_email(self, email: str):
        if email:
            self._query = self._query.where(func.lower(UserDB.email).like(func.lower(f'%{email}%')))
        return self

    def _with_last_name(self, email: str):
        if email:
            self._query = self._query.where(func.lower(UserDB.email).like(func.lower(f"%{email}%")))
        return self

    def _build(self):
        return self._query

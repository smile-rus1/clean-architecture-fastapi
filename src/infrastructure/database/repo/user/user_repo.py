from fastapi import HTTPException
from sqlalchemy import insert, select, delete
from sqlalchemy.exc import IntegrityError

from src.application.common.exceptions.applications import ApplicationException
from src.application.user.dto.user import UserDTO, UserDTOs
from src.application.user.exceptions.user import UserAlreadyExist, UserNotFoundByID, UserNotFoundByEmail
from src.application.user.interfaces.repo.user_repo import IUserRepo, IUserReader
from src.domain.user.entities.user import User
from src.domain.user.value_objects.user import UserID
from src.infrastructure.database.models.user import UserDB
from src.infrastructure.database.repo.common.base_repo import SQLAlchemyRepo
from src.infrastructure.database.repo.user.user_query_builder import GetUserQuery


class UserRepo(SQLAlchemyRepo, IUserRepo):
    async def add_user(self, user: User) -> int:
        sql = insert(UserDB).values(
            first_name=user.first_name.to_string(),
            last_name=user.last_name.to_string(),
            email=user.email.to_string(),
            password=user.password
        ).returning(UserDB.id)
        try:
            result = await self._session.execute(sql)

        except IntegrityError as exc:
            # raise HTTPException(status_code=409, detail=f"User with email {user.email} already exists.")
            raise self._error_parser(user, exc)

        row_id = result.scalar()
        return row_id

    async def get_user_by_id(self, user_id: UserID) -> User:
        sql = select(UserDB).where(UserDB.id == user_id.to_id())
        result = await self._session.execute(sql)
        model = result.scalar()

        if not model:
            raise UserNotFoundByID(user_id.to_id())
        return self._mapper.load(User, model)

    async def get_user_by_email(self, email: str) -> User:
        sql = select(UserDB).where(UserDB.email == email)
        result = await self._session.execute(sql)
        model = result.scalar()

        if not model:
            raise UserNotFoundByEmail(email)
        return self._mapper.load(User, model)

    async def update_user(self, user: User) -> None:
        user_db = self._mapper.load(UserDB, user)
        try:
            await self._session.merge(user_db)
        except IntegrityError as exc:
            self._error_parser(user, exc)

    async def delete_user(self, user_id: UserID) -> None:
        sql = delete(UserDB).where(UserDB.id == user_id.to_id()).returning(UserDB.id)
        result = await self._session.execute(sql)

        deleted_row_id = result.scalar()
        if not deleted_row_id:
            raise UserNotFoundByID(user_id.to_id())

    @staticmethod
    def _error_parser(user: User, exc: IntegrityError) -> ApplicationException:
        database_column = exc.__cause__.__cause__.constraint_name
        print(database_column)
        if database_column == "users_email_key":
            return UserAlreadyExist(user.email.to_string())


class UserReader(SQLAlchemyRepo, IUserReader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._query_builder = GetUserQuery()

    async def get_user_by_id(self, user_id: int) -> UserDTO:
        self._validate_id(user_id, "user_id")
        sql = select(UserDB).where(UserDB.id == user_id)
        result = await self._session.execute(sql)
        model = result.scalar()

        if not model:
            raise UserNotFoundByID(user_id)

        return self._mapper.load(UserDTO, model)

    async def get_users(
            self,
            first_name: str,
            last_name: str,
            email: str,
            limit: int,
            offset: int
    ) -> UserDTOs:
        self._validate_limit_offset(limit, offset)
        sql = self._query_builder.get_query(
            first_name=first_name,
            last_name=last_name,
            email=email,
            offset=offset,
            limit=limit
        )
        result = await self._session.execute(sql)
        models = result.scalars().all()
        return self._mapper.load(UserDTOs, models)

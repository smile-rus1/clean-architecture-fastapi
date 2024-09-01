from typing import Protocol

from src.application.user.dto.user import UserDTO, UserDTOs
from src.domain.user.entities.user import User
from src.domain.user.value_objects.user import UserID


class IUserRepo(Protocol):
    async def get_user_by_id(self, user_id: UserID) -> User:
        raise NotImplementedError

    async def get_user_by_email(self, email: str) -> User:
        raise NotImplementedError

    async def add_user(self, user: User) -> int:
        raise NotImplementedError

    async def update_user(self, user: User) -> None:
        raise NotImplementedError

    async def delete_user(self, user_id: UserID) -> None:
        raise NotImplementedError


class IUserReader(Protocol):
    async def get_user_by_id(self, user_id: int) -> UserDTO:
        raise NotImplementedError

    async def get_users(
            self,
            first_name: str,
            last_name: str,
            email: str,
            limit: int,
            offset: int
    ) -> UserDTOs:
        raise NotImplementedError

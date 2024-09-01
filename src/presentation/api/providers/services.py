from typing import Any

from fastapi import Depends

from src.application.user.dto.user import UserDTO
from src.application.user.usecases.auth import AuthService
from src.application.user.usecases.user import UserService
from src.infrastructure.database.uow.uow import UoW
from src.infrastructure.hasher import Hasher
from src.infrastructure.mapper.mapper import Mapper
from src.presentation.api.providers.abstract.auth import optional_auth_provider, without_auth_provider, auth_provider
from src.presentation.api.providers.abstract.common import uow_provider, mapper_provider, hasher_provider


def auth_service_getter(
        uow: UoW = Depends(uow_provider),
        mapper: Mapper = Depends(mapper_provider),
        hasher: Hasher = Depends(hasher_provider)
):
    return AuthService(uow=uow, mapper=mapper, hasher=hasher)


def user_service_with_optional_getter(
        _: Any = Depends(optional_auth_provider),
        uow: UoW = Depends(uow_provider),
        mapper: Mapper = Depends(mapper_provider),
):
    return UserService(uow=uow, mapper=mapper, hasher=None, current_user=None)


def user_service_without_auth_getter(
        _: Any = Depends(without_auth_provider),
        uow: UoW = Depends(uow_provider),
        mapper: Mapper = Depends(mapper_provider),
        hasher: Hasher = Depends(hasher_provider)
):
    return UserService(uow=uow, mapper=mapper, hasher=hasher, current_user=None)


def user_service_with_auth_getter(
        user_dto: UserDTO = Depends(auth_provider),
        uow: UoW = Depends(uow_provider),
        mapper: Mapper = Depends(mapper_provider),
        hasher: Hasher = Depends(hasher_provider)
):
    return UserService(uow=uow, current_user=user_dto, mapper=mapper, hasher=hasher)

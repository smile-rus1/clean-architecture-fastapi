from abc import ABC

from src.application.common.interfaces.mapper import IMapper
from src.application.user.dto.auth import AuthUserDTO
from src.application.user.dto.user import UserDTO
from src.application.user.exceptions.auth import InvalidEmail, InvalidPassword
from src.application.user.exceptions.user import UserNotFoundByEmail
from src.application.user.interfaces.hasher.hasher import IHasher
from src.application.user.interfaces.uow.user_uow import IUserUoW


class AuthUseCase(ABC):
    def __init__(self, uow: IUserUoW, mapper: IMapper, hasher: IHasher):
        self._uow = uow
        self._mapper = mapper
        self._hasher = hasher


class AuthenticateUser(AuthUseCase):
    async def __call__(self, auth_data: AuthUserDTO) -> UserDTO:
        try:
            user = await self._uow.user_repo.get_user_by_email(auth_data.email)

        except UserNotFoundByEmail:
            raise InvalidEmail(auth_data.email)

        if not self._hasher.verify(auth_data.password, user.password):
            raise InvalidPassword()

        return self._mapper.load(UserDTO, user)


class AuthService:
    def __init__(self, uow: IUserUoW, mapper: IMapper, hasher: IHasher):
        self._uow = uow
        self._mapper = mapper
        self._hasher = hasher

    async def authenticate_user(self, auth_data: AuthUserDTO) -> UserDTO:
        return await AuthenticateUser(self._uow, self._mapper, self._hasher)(auth_data)

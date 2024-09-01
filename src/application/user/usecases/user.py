from abc import ABC
from datetime import datetime

from src.application.common.interfaces.mapper import IMapper
from src.application.user.dto.user import CreateUserDTO, UserDTO, UpdateUserDTO, SearchParametersDTO, UserDTOs
from src.application.user.exceptions.user import UserAlreadyExist, UserNotFoundByID, UserAccessError
from src.application.user.interfaces.hasher.hasher import IHasher
from src.application.user.interfaces.uow.user_uow import IUserUoW
from src.domain.user.entities.user import User
from src.domain.user.services.access_policy import UserAccessPolicy
from src.domain.user.value_objects.user import Password, Email, UserID, FirstName, LastName


class UserUseCase(ABC):
    def __init__(self, uow: IUserUoW, mapper: IMapper, hasher: IHasher):
        self._uow = uow
        self._mapper = mapper
        self._hasher = hasher


class CreateUser(UserUseCase):
    async def __call__(self, create_account_dto: CreateUserDTO) -> UserDTO:
        hashed_password = self._hasher.hash(Password(create_account_dto.password).to_string())
        user = User.create(
            email=Email(create_account_dto.email),
            first_name=FirstName(create_account_dto.first_name),
            last_name=LastName(create_account_dto.last_name),
            password=hashed_password,
            created_at=datetime.now()
        )

        try:
            user_id = await self._uow.user_repo.add_user(user)
            await self._uow.commit()

        except UserAlreadyExist:
            await self._uow.rollback()
            raise

        user.update(user_id=UserID(user_id))

        return self._mapper.load(UserDTO, user)


class UserUpdate(UserUseCase):
    async def __call__(self, update_user_dto: UpdateUserDTO) -> UserDTO:
        hashed_password = self._hasher.hash(Password(update_user_dto.password).to_string())
        user = await self._uow.user_repo.get_user_by_id(user_id=UserID(update_user_dto.id))
        user.update(
            first_name=FirstName(update_user_dto.first_name) if update_user_dto.first_name else user.first_name,
            last_name=LastName(update_user_dto.last_name) if update_user_dto.last_name else user.last_name,
            email=Email(update_user_dto.email) if update_user_dto.email else user.email,
            password=hashed_password if update_user_dto.password else user.password
        )

        try:
            await self._uow.user_repo.update_user(user)
            await self._uow.commit()
        except UserAlreadyExist:
            await self._uow.rollback()
            raise

        return self._mapper.load(UserDTO, user)


class GetUser(UserUseCase):
    async def __call__(self, user_id: int) -> UserDTO:
        return await self._uow.user_reader.get_user_by_id(user_id)


class SearchUsers(UserUseCase):
    async def __call__(self, search_user_dto: SearchParametersDTO) -> UserDTOs:
        return await self._uow.user_reader.get_users(
            first_name=search_user_dto.first_name,
            last_name=search_user_dto.last_name,
            email=search_user_dto.email,
            limit=search_user_dto.limit,
            offset=search_user_dto.offset
        )


class DeleteUser(UserUseCase):
    async def __call__(self, user_id: int) -> None:
        try:
            await self._uow.user_repo.delete_user(user_id=UserID(user_id))
            await self._uow.commit()

        except UserNotFoundByID:
            await self._uow.rollback()
            raise


class UserService:
    def __init__(self, uow: IUserUoW, mapper: IMapper, hasher: IHasher, current_user: UserDTO | None):
        self._uow = uow
        self._mapper = mapper
        self._hasher = hasher
        self._access_policy = UserAccessPolicy(mapper.load(User, current_user))

    async def create_user(self, user_dto: CreateUserDTO) -> UserDTO:
        return await CreateUser(self._uow, self._mapper, self._hasher)(user_dto)

    async def update_user(self, user_dto: UpdateUserDTO) -> UserDTO:
        if not self._access_policy.check_self(user_id=user_dto.id):
            raise UserAccessError(user_dto.id)
        return await UserUpdate(self._uow, self._mapper, self._hasher)(user_dto)

    async def get_user(self, user_id: int) -> UserDTO:
        return await GetUser(self._uow, self._mapper, self._hasher)(user_id)

    async def search_users(self, search_user_dto: SearchParametersDTO) -> UserDTOs:
        return await SearchUsers(self._uow, self._mapper, self._hasher)(search_user_dto)

    async def delete_user(self, user_id: int) -> None:
        if not self._access_policy.check_self(user_id=user_id):
            raise UserAccessError(user_id)
        await DeleteUser(self._uow, self._mapper, self._hasher)(user_id)

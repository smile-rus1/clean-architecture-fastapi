from src.application.user.dto.user import UserDTO, UserDTOs
from src.domain.user.entities.user import User
from src.domain.user.value_objects.user import UserID, FirstName, LastName, Email
from src.infrastructure.database.models.user import UserDB
from src.infrastructure.mapper.decorator import converter


def convert_to_dto(data: User | UserDB) -> UserDTO:
    return UserDTO(
        id=data.id,
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        created_at=data.created_at,
        updated_at=data.updated_at
    )


@converter(User, UserDTO)
def user_entity_to_dto_converter(data: User) -> UserDTO:
    user_ddd = UserDTO(
        id=data.id.to_id(),
        first_name=data.first_name.to_string(),
        last_name=data.last_name.to_string(),
        email=data.email.to_string(),
        created_at=data.created_at,
        updated_at=data.updated_at
    )
    return user_ddd


@converter(UserDB, UserDTO)
def user_model_to_dto_converter(data: UserDB) -> UserDTO:
    return convert_to_dto(data)


@converter(list, UserDTOs)
def user_models_to_dtos_converter(data: list[UserDB]) -> UserDTOs:
    return UserDTOs(
        users=[convert_to_dto(user_db) for user_db in data]
    )


@converter(User, UserDB)
def user_entity_to_model_converter(data: User) -> UserDB:
    return UserDB(
        id=data.id.to_id(),
        first_name=data.first_name.to_string(),
        last_name=data.last_name.to_string(),
        email=data.email.to_string(),
        password=data.password,
        created_at=data.created_at,
        updated_at=data.updated_at
    )


@converter(UserDTO, User)
def user_dto_to_entity_converter(data: UserDTO) -> User:
    return User(
        id=UserID(data.id),
        first_name=FirstName(data.first_name),
        last_name=LastName(data.last_name),
        email=Email(data.email),
        created_at=data.created_at,
        updated_at=data.updated_at,
        password=None
    )


@converter(UserDB, User)
def user_model_to_entity_converter(data: UserDB) -> User:
    return User(
        id=UserID(data.id),
        first_name=FirstName(data.first_name),
        last_name=LastName(data.last_name),
        email=Email(data.email),
        created_at=data.created_at,
        updated_at=data.updated_at,
        password=data.password
    )

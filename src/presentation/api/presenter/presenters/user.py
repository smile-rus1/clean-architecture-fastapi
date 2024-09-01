from src.application.user.dto.user import BaseUserDTO, UserDTOs, UserDTO
from src.infrastructure.mapper.decorator import converter
from src.presentation.api.handlers.user.user.responses.user import UserVM, UsersVM


def dto_to_vm(data: UserDTO) -> UserVM:
    return UserVM(
        id=data.id,
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        updated_at=data.updated_at if data.updated_at else None,
        created_at=data.created_at if data.created_at else None
    )


@converter(UserDTO, UserVM)
def convert_dto_to_vm(data: UserDTO) -> UserVM:
    return dto_to_vm(data)


@converter(UserDTOs, UsersVM)
def convert_dtos_to_vms(data: UserDTOs) -> UsersVM:
    return UsersVM(users=[dto_to_vm(vm) for vm in data.users])

from dataclasses import dataclass
from datetime import datetime

from src.application.common.dto.base import DTO


@dataclass
class BaseUserDTO(DTO):
    first_name: str
    last_name: str
    email: str
    created_at: datetime | None
    updated_at: datetime | None


@dataclass
class SearchParametersDTO(DTO):
    limit: int
    offset: int
    first_name: str
    last_name: str
    email: str


@dataclass
class CreateUserDTO(BaseUserDTO):
    password: str


@dataclass
class UpdateUserDTO(DTO):
    id: int
    first_name: str | None
    last_name: str | None
    email: str | None
    password: str | None
    created_at: datetime | None
    updated_at: datetime | None


@dataclass
class UserDTO(BaseUserDTO):
    id: int


@dataclass
class UserDTOs(DTO):
    users: list[UserDTO]

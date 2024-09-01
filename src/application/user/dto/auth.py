from dataclasses import dataclass

from src.application.common.dto.base import DTO


@dataclass
class AuthUserDTO(DTO):
    email: str
    password: str

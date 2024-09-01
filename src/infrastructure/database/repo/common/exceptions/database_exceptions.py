from dataclasses import dataclass

from src.infrastructure.database.repo.common.exceptions.base import BaseRepoException


@dataclass
class InvalidID(BaseRepoException):
    field: str

    def message(self):
        return f"Validation error: value in field {self.field} <= 0"


@dataclass
class LimitError(BaseRepoException):
    def message(self):
        return f"Validation error: size <= 0"


@dataclass
class OffSetError(BaseRepoException):
    def message(self):
        return f"Validation error: offset < 0"

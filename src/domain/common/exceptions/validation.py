from dataclasses import dataclass

from src.domain.common.exceptions.domain import DomainException


@dataclass
class BaseModelException(DomainException):
    field: str


@dataclass
class EmptyField(BaseModelException):
    def message(self):
        return f"Validation error: Value in field {self.field} is empty or content made up of spaces"


@dataclass
class EmailValidationError(BaseModelException):
    email: str

    def message(self):
        return f"Validation error: Email {self.email} in field {self.field} is not valid"


@dataclass
class EnumError(BaseModelException):
    value: str
    expected_values: list[str]

    def message(self):
        return f"Validation error: passed value {self.value} that is outside the expected {self.expected_values}"


class InvalidID(BaseModelException):

    def message(self):
        return f'Validation error: the value you passed in the field {self.field} is less than zero'

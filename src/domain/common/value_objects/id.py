from dataclasses import dataclass

from src.domain.common.exceptions.validation import InvalidID
from src.domain.common.value_objects.base import ValueObject


@dataclass
class IDVO(ValueObject):
    value: int

    def __post_init__(self):
        if isinstance(self.value, int) and self.value <= 0:
            raise InvalidID(self.__field_name__)

    def to_id(self) -> int:
        return self.value

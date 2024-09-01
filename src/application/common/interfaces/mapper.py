from typing import Protocol, Any, TypeVar


T = TypeVar("T")


class IMapper(Protocol):
    def load(self, class_: type[T], data: Any) -> T:
        raise NotImplementedError

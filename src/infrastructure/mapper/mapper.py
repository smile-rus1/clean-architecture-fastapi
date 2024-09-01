from typing import Callable, Any

from src.application.common.interfaces.mapper import IMapper, T
from src.infrastructure.mapper.converter import Converter, FromModel, ToModel


class Mapper(IMapper):
    def __init__(self):
        self._converters: list[Converter] = []

    def add(self, from_model: FromModel, to_model: ToModel, func: Callable):
        self._converters.append(
            Converter(
                from_model=from_model,
                to_model=to_model,
                func=func
            )
        )

    def load(self, class_: type[T], data: Any) -> T:
        converter = self._get_converter(from_model=type(data), to_model=class_)
        if converter:
            return converter.convert(data)

    def _get_converter(self, from_model: FromModel, to_model: ToModel) -> Converter:
        for conv in self._converters:
            if conv.check(from_model, to_model):
                return conv

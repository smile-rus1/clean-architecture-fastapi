from src.infrastructure.mapper.converters import bind_user_converters
from src.infrastructure.mapper.mapper import Mapper


def build_mapper():
    mapper = Mapper()
    bind_user_converters(mapper)

    return mapper

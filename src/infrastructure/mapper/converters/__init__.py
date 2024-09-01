from . import user
from ..mapper import Mapper


def bind_user_converters(mapper: Mapper):
    user.user_entity_to_model_converter(mapper=mapper)
    user.user_dto_to_entity_converter(mapper=mapper)
    user.user_model_to_entity_converter(mapper=mapper)
    user.user_model_to_dto_converter(mapper=mapper)
    user.user_entity_to_dto_converter(mapper=mapper)
    user.user_models_to_dtos_converter(mapper=mapper)

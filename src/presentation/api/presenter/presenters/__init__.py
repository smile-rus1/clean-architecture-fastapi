from . import user
from src.presentation.api.presenter.presenter import Presenter


def bind_user_presenter(presenter: Presenter):
    user.convert_dto_to_vm(mapper=presenter)
    user.convert_dtos_to_vms(mapper=presenter)


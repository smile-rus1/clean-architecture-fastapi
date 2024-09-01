from src.presentation.api.presenter.presenters import bind_user_presenter
from src.presentation.api.presenter.presenter import Presenter


def build_presenter():
    presenter = Presenter()
    bind_user_presenter(presenter)

    return presenter

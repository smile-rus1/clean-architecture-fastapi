from src.application.common.interfaces.uow.base import IUoW
from src.application.user.interfaces.repo.user_repo import IUserRepo, IUserReader


class IUserUoW(IUoW):
    user_repo: IUserRepo
    user_reader: IUserReader

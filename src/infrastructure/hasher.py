from passlib.context import CryptContext

from src.application.user.interfaces.hasher.hasher import IHasher


class Hasher(IHasher):
    def __init__(self):
        self.hasher = CryptContext(schemes=['bcrypt'], deprecated="auto")

    def hash(self, row: str) -> str:
        return self.hasher.hash(row)

    def verify(self, row: str, hashed_row) -> bool:
        return self.hasher.verify(row, hashed_row)

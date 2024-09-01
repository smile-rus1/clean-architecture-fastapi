from typing import Protocol


class IUoW(Protocol):
    async def commit(self):
        raise NotImplementedError

    async def rollback(self):
        raise NotImplementedError

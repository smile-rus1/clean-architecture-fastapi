from typing import Protocol

from sqlalchemy.exc import DatabaseError

from application.common.exceptions.applications import ApplicationException
from domain.common.entities.entity import Entity


class IErrorParser(Protocol):
    def parse_error(self, entity: Entity, error: DatabaseError) -> ApplicationException:
        raise NotImplementedError

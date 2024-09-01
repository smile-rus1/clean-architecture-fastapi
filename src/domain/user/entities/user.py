from dataclasses import dataclass
from datetime import datetime

from src.domain.common.entities.entity import Entity
from src.domain.common.entities.entity_merge import EntityMerge

from src.domain.common.constants.empty import Empty
from src.domain.common.utils.data_filter import data_filter

from src.domain.user.value_objects.user import (
    UserID,
    FirstName,
    LastName,
    Email
)


@dataclass
class User(Entity, EntityMerge):
    id: UserID
    first_name: FirstName
    last_name: LastName
    email: Email
    password: str
    created_at: datetime
    updated_at: None | datetime

    @staticmethod
    def create(
            first_name: FirstName,
            last_name: LastName,
            email: Email,
            password: str,
            created_at: datetime
    ):
        return User(
            id=UserID(None),
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            created_at=created_at,
            updated_at=None
        )

    def update(
            self,
            user_id: UserID | Empty = Empty.UNSET,
            first_name: FirstName | Empty = Empty.UNSET,
            last_name: LastName | Empty = Empty.UNSET,
            email: Email | Empty = Empty.UNSET,
            password: str | Empty = Empty.UNSET,
            created_at: datetime | Empty = Empty.UNSET,
    ) -> None:
        filtered_args = data_filter(
            id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            created_at=created_at
        )
        self._merge(**filtered_args)

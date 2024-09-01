from dataclasses import dataclass

from src.presentation.api.config import ApiConfig
from src.infrastructure.database.config import DBConfig


@dataclass
class Config:
    db: DBConfig
    api: ApiConfig

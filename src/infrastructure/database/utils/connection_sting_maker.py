from src.infrastructure.database.config import DBConfig


def make_connection_sting(config: DBConfig):
    return (
        f"{config.driver}://{config.user}:{config.password}@{config.host}:{config.port}/{config.db_name}"
    )

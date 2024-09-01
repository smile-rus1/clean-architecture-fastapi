import os

from dotenv import load_dotenv

from src.infrastructure.database.config import DBConfig
from src.presentation.api.config import ApiConfig
from src.presentation.config.config import Config


def config_loader():
    load_dotenv()

    return Config(
        api=ApiConfig(
            host=os.getenv("WEB_HOST"),
            port=int(os.getenv("WEB_PORT")),
            debug=bool(os.getenv("DEBUG"))
        ),

        db=DBConfig(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            db_name=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            driver=os.getenv("DB_DRIVER")
        )
    )


config = config_loader()

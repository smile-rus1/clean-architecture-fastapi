import uvicorn
from fastapi import FastAPI

# from src.presentation.api.auth import AuthorizationBasic
from src.presentation.api.main import init_app
from src.presentation.config.config_reader import config


def start_app():
    app = init_app(FastAPI(), config)

    return app


if __name__ == '__main__':
    uvicorn.run(
        app="src.main:start_app",
        host=config.api.host,
        port=config.api.port,
        reload=True,
        factory=True,
        log_level="info"
    )

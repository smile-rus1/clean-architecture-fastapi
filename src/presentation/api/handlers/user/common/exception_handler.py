from fastapi.responses import JSONResponse

from src.application.user.exceptions import user


def user_exception_handler(_, exc: user.UserIDException):
    match exc:
        case user.UserNotFoundByID():
            return JSONResponse(status_code=404, content={"message": exc.message()})

        case (user.UserAlreadyExist() | user.UserNotFoundByEmail()):
            return JSONResponse(status_code=409, content={"message": exc.message()})

        case user.UserAccessError():
            return JSONResponse(status_code=403, content={"message": exc.message()})

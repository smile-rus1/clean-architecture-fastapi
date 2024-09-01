import binascii
from base64 import b64decode

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Request, HTTPException
from fastapi.security.utils import get_authorization_scheme_param
from starlette.status import HTTP_401_UNAUTHORIZED


class AuthorizationBasic(HTTPBasic):
    async def __call__(
            self,
            request: Request
    ) -> HTTPBasicCredentials | None:
        authorization = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if self.realm:
            unauthorized_headers = {"WWW-Authenticate": f'Basic realm="{self.realm}"'}
        else:
            unauthorized_headers = {"WWW-Authenticate": "Basic"}

        invalid_user_credentials_exc = HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers=unauthorized_headers,
        )

        if not authorization or scheme.lower() != "basic":
            return None

        try:
            data = b64decode(param).decode("ascii")

        except (ValueError, UnicodeError, binascii.Error):
            raise invalid_user_credentials_exc

        username, sep, password = data.partition(":")

        if not sep:
            raise invalid_user_credentials_exc

        return HTTPBasicCredentials(username=username, password=password)

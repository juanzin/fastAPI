from starlette.middleware.base import BaseHTTPMiddleware ## the middleware was created using starlette
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse

## error managment
class HTTPErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as exp:
            content = f"exc: {str(exp)}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return JSONResponse(content=content, status_code=status_code)

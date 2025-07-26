import httpx
from typing import Any, cast
from barid.utils.session import AsyncSession
from barid.types import ErrorResponse

class EmailAPI:
    def __init__(self) -> None:
        self._session: AsyncSession = AsyncSession()
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> "EmailAPI":
        self._client = await self._session.get_client()
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self._session.close_client()
        self._client = None

    async def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response | ErrorResponse:
        if not self._client:
            raise RuntimeError("Client not initialized")

        try:
            response = await getattr(self._client, method.lower())(url, **kwargs)
            response.raise_for_status()
            return response

        except httpx.HTTPStatusError as e:
            return cast(ErrorResponse, {
                "type": "error",
                "status_code": e.response.status_code,
                "message": str(e),
                "response": e.response.text
            })

        except httpx.RequestError as e:
            return cast(ErrorResponse, {
                "type": "error",
                "status_code": 0,
                "message": f"Request error: {str(e)}",
                "response": ""
            })

        except Exception as e:
            return cast(ErrorResponse, {
                "type": "error",
                "status_code": -1,
                "message": f"Unexpected error: {str(e)}",
                "response": ""
            })

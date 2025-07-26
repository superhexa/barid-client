import httpx
from typing import Optional

class AsyncSession:
    """
    Manages a singleton Async HTTP client session.

    Methods
    -------
    get_client() -> httpx.AsyncClient
        Returns an existing or new AsyncClient instance.

    close_client() -> None
        Closes the AsyncClient if exists.
    """
    _client: Optional[httpx.AsyncClient] = None

    async def get_client(self) -> httpx.AsyncClient:
        """
        Get or create the asynchronous HTTP client.

        Returns
        -------
        httpx.AsyncClient
            The asynchronous HTTP client instance.
        """
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url="https://api.barid.site",
                timeout=15.0,
                http2=True,
            )
        return self._client

    async def close_client(self) -> None:
        """
        Close the asynchronous HTTP client.

        Returns
        -------
        None
        """
        if self._client:
            await self._client.aclose()
            self._client = None

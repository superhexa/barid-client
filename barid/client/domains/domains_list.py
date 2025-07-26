from barid.api.mailapi import EmailAPI
from barid.utils.decorators import is_not_none, type_check, trace_call
from typing import List

class DomainsList:
    """
    Client method to get list of supported domains.

    Parameters
    ----------
    api : EmailAPI
        An instance of EmailAPI to perform requests.

    Methods
    -------
    __call__() -> List[str]
        Retrieve supported domains list.
    """
    def __init__(self, api: EmailAPI):
        self._api = api

    @trace_call
    @is_not_none
    @type_check(list)
    async def __call__(self) -> List[str]:
        """
        Retrieve a list of all supported email domains.

        Returns
        -------
        List[str]
            List of domain strings.
        """
        resp = await self._api.request("GET", "/domains")
        data = resp.json()
        return data["result"]

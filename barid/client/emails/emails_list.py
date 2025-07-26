from barid.api.mailapi import EmailAPI
from barid.models.email import Email
from barid.utils.decorators import is_not_none, type_check, trace_call
from typing import List, cast
from barid.types import EmailAddress, ErrorResponse

class EmailsList:
    """
    Client method to fetch emails list for an email address.

    Parameters
    ----------
    api : EmailAPI
        An instance of EmailAPI to perform requests.

    Methods
    -------
    __call__(email: EmailAddress, limit: int = 10, offset: int = 0) -> List[Email]
        Fetch list of emails with optional pagination.
    """
    def __init__(self, api: EmailAPI):
        self._api = api

    @trace_call
    @is_not_none
    @type_check(List[Email])
    async def __call__(self, email: EmailAddress, limit: int = 10, offset: int = 0) -> List[Email]:
        """
        Retrieve emails for the specified email address.

        Parameters
        ----------
        email : EmailAddress
            The email address to fetch emails for.
        limit : int, optional
            Max number of emails to return (default is 10).
        offset : int, optional
            Number of emails to skip (default is 0).

        Returns
        -------
        List[Email]
            List of email basic information models.
        """
        params = {"limit": limit, "offset": offset}
        resp = await self._api.request("GET", f"/emails/{email}", params=params)

        if isinstance(resp, dict) and resp.get("type") == "error":
            err = cast(ErrorResponse, resp)
            raise RuntimeError(f"[{err['status_code']}] {err['message']}")

        data = resp.json()
        return [Email.parse_obj(i) for i in data["result"]]
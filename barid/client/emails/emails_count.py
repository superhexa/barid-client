from barid.api.mailapi import EmailAPI
from barid.utils.decorators import is_not_none, type_check, trace_call
from barid.types import EmailAddress

class EmailsCount:
    """
    Client method to get count of emails for an email address.

    Parameters
    ----------
    api : EmailAPI
        An instance of EmailAPI to perform requests.

    Methods
    -------
    __call__(email: EmailAddress) -> int
        Get the number of emails for the email address.
    """
    def __init__(self, api: EmailAPI):
        self._api = api

    @trace_call
    @is_not_none
    @type_check(int)
    async def __call__(self, email: EmailAddress) -> int:
        """
        Get total email count for an email address.

        Parameters
        ----------
        email : EmailAddress
            The email address.

        Returns
        -------
        int
            Total count of emails.
        """
        resp = await self._api.request("GET", f"/emails/count/{email}")
        data = resp.json()
        return data["result"]["count"]

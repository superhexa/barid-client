from barid.api.mailapi import EmailAPI
from barid.utils.decorators import is_not_none, type_check, trace_call
from barid.types import EmailAddress
from barid.models.delete import DeleteResult, DeleteError

class EmailsDelete:
    """
    Client method to delete all emails for an email address.

    Parameters
    ----------
    api : EmailAPI
        An instance of EmailAPI to perform requests.

    Methods
    -------
    __call__(email: EmailAddress) -> dict
        Delete all emails for the email address.
    """
    def __init__(self, api: EmailAPI):
        self._api = api

    @trace_call
    @is_not_none
    @type_check(DeleteResult)
    async def __call__(self, email: EmailAddress) -> dict:
        """
        Delete all emails associated with the specified email address.

        Parameters
        ----------
        email : EmailAddress
            The email address.

        Returns
        -------
        dict
            Result dictionary with deletion message and count.
        """
        try:
            resp = await self._api.request("DELETE", f"/emails/{email}")
            data = resp.json()
            if not data:
                raise ValueError
            return DeleteResult.parse_obj(resp.json())
        except Exception:
            return DeleteResult(success=False, error=DeleteError(name="ZodError", message="Invalid input."))

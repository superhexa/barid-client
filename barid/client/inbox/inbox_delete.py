from barid.api.mailapi import EmailAPI
from barid.utils.decorators import is_not_none, type_check, trace_call
from barid.types import EmailId
from barid.models.delete import DeleteResult

class InboxDelete:
    """
    Client method to delete an email inbox by ID.

    Parameters
    ----------
    api : EmailAPI
        An instance of EmailAPI to perform requests.

    Methods
    -------
    __call__(email_id: EmailId) -> dict
        Delete email by ID.
    """
    def __init__(self, api: EmailAPI):
        self._api = api

    @trace_call
    @is_not_none
    @type_check(DeleteResult)
    async def __call__(self, email_id: EmailId) -> dict:
        """
        Delete the specified email by its ID.

        Parameters
        ----------
        email_id : EmailId
            The unique email ID.

        Returns
        -------
        dict
            Result dictionary with deletion message.
        """
        resp = await self._api.request("DELETE", f"/inbox/{email_id}")
        return DeleteResult.parse_obj(resp.json())

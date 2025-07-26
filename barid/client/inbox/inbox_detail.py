from barid.api.mailapi import EmailAPI
from barid.models.details import EmailDetails
from barid.utils.decorators import is_not_none, type_check, trace_call
from barid.types import EmailId

class InboxDetail:
    """
    Client method to fetch detailed email content by email ID.

    Parameters
    ----------
    api : EmailAPI
        An instance of EmailAPI to perform requests.

    Methods
    -------
    __call__(email_id: EmailId) -> EmailDetails
        Fetch full email content.
    """
    def __init__(self, api: EmailAPI):
        self._api = api

    @trace_call
    @is_not_none
    @type_check(EmailDetails)
    async def __call__(self, email_id: EmailId) -> EmailDetails:
        """
        Retrieve full email details by email ID.

        Parameters
        ----------
        email_id : EmailId
            The unique identifier of the email.

        Returns
        -------
        EmailDetails
            Email detail (from address, subject, text_content, etc..).
        """
        resp = await self._api.request("GET", f"/inbox/{email_id}")
        data = resp.json()
        return EmailDetails.parse_obj(data["result"])

from typing import AsyncContextManager
from barid.api.mailapi import EmailAPI
from barid.client.emails.emails_list import EmailsList
from barid.client.emails.emails_count import EmailsCount
from barid.client.emails.emails_delete import EmailsDelete
from barid.client.inbox.inbox_detail import InboxDetail
from barid.client.inbox.inbox_delete import InboxDelete
from barid.client.domains.domains_list import DomainsList

class BaridClient(AsyncContextManager["BaridClient"]):
    """
    Main Barid Client for API operations.
    """

    def __init__(self):
        self._api = EmailAPI()
        self.get_domains = DomainsList(self._api)
        self.get_emails = EmailsList(self._api)
        self.count_emails = EmailsCount(self._api)
        self.delete_email = InboxDelete(self._api)
        self.delete_emails = EmailsDelete(self._api)
        self.get_email = InboxDetail(self._api)

    async def __aenter__(self):
        await self._api.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._api.__aexit__(exc_type, exc_val, exc_tb)

from typing import NewType, Annotated
from pydantic import BaseModel, Field

EmailID = Annotated[str, Field(max_length=64)]
EmailAddress = Annotated[str, Field(max_length=128)]

class Email(BaseModel):
    """
    Represents a single email message in summary form.

    Parameters:
        id (str): Unique identifier of the email.
        from_address (str): Email address of the sender.
        subject (str): Subject line of the email.
        received_at (int): Unix timestamp of when the email was received.
    """

    id: EmailID
    from_address: EmailAddress
    subject: str
    received_at: int

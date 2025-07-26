from typing import Optional
from pydantic import BaseModel

class EmailDetails(BaseModel):
    """
    Represents the full content of an email message.

    Parameters:
        id (str): Unique identifier of the email.
    
    Returns:
        subject      (Optional[str]): Email subject.
        text_content (Optional[str]): Plaintext version of the email body.
        html_content (Optional[str]): HTML version of the email body, if any.
        from_address (Optional[str]): Sender's email.
        to_address	 (Optional[str]): Recipient's Email.
        received_at  (Optional[int]): Recieved at timestamp.
    """

    id: str
    subject: Optional[str]
    from_address: str
    to_address: str
    text_content: Optional[str]
    html_content: Optional[str]
    received_at: int
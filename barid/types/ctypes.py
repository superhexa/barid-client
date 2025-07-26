from typing import NewType, Literal, TypedDict, TypeAlias

EmailAddress = NewType("EmailAddress", str)
EmailId = NewType("EmailId", str)
Timestamp = NewType("Timestamp", int)
CountInt = NewType("CountInt", int)
Message = NewType("Message", str)

ErrorType: TypeAlias = Literal["error"]
class ErrorResponse(TypedDict):
    type: ErrorType
    status_code: int
    message: str
    response: str
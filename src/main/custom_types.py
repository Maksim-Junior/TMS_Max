from typing import NamedTuple, Optional, Union

from pydantic.main import BaseModel


class ResponseT(BaseModel):
    status: Union[int, str] = 200
    content_type: str
    payload: str


class RequestT(NamedTuple):
    method: str
    path: str
    query_string: Optional[str] = None

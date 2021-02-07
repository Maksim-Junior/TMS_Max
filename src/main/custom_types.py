from http import HTTPStatus
from typing import NamedTuple, Optional, Union, Dict, Callable

from pydantic import Field
from pydantic.main import BaseModel


class ResponseT(BaseModel):
    status: Union[int, HTTPStatus] = HTTPStatus.OK
    content_type: str = "text/html"
    payload: Optional[str] = None

    class Config:
        validate_assignment = True


class RequestT(NamedTuple):
    method: str
    path: str
    query: Dict = Field(default_factory=dict)

    class Config:
        allow_mutation = False
        validate_assignment = True


HandlerT = Callable[[RequestT], ResponseT]

from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson3/lesson3.html"


def handler(_request: RequestT) -> ResponseT:
    document = render_template(TEMPLATE)

    response = ResponseT(payload=document)

    return response

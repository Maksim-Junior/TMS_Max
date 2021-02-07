import traceback
from http import HTTPStatus

from main.custom_types import ResponseT, RequestT
from main.util import render_template

TEMPLATE = "notFound.html"


def handle_404(_request: RequestT) -> ResponseT:
    payload = render_template("notFound.html")
    response = ResponseT(payload=payload, status=HTTPStatus.NOT_FOUND)

    return response


def handle_500(_request: RequestT) -> ResponseT:
    response = ResponseT(
        content_type="text/plain",
        payload=traceback.format_exc(),
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
    )

    return response

from django.http import HttpRequest, HttpResponse

from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson5/lesson5.html"


def handler(_request: RequestT) -> ResponseT:
    document = render_template(TEMPLATE)

    response = ResponseT(payload=document)

    return response


def handler_django(_request: HttpRequest) -> HttpResponse:
    document = render_template("tasks/lesson5/lesson5.html")

    response = HttpResponse(document)

    return response

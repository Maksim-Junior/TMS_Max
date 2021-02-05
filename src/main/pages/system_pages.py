import traceback
from main.custom_types import ResponseT, RequestT
from main.pages.function_for_pages import read_template


def division_zero_page(request: RequestT) -> ResponseT:
    status = "500 Internal Server Error"
    content_type = "text/html"
    payload = str(1 / 0)
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def not_found_page(request: RequestT) -> ResponseT:
    status = "404 not found"
    content_type = "text/html"
    payload = read_template("notFound.html")
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def error_500_page(request: RequestT) -> ResponseT:
    status = "500 Internal Server Error"
    content_type = "text/plain"
    payload = traceback.format_exc()
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response

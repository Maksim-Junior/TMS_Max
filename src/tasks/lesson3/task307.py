from django.http import HttpRequest, HttpResponse

from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson3/task_307.html"


def handler(request: RequestT) -> ResponseT:
    string = request.query.get("string")

    if not string:
        result = "Input string..."
    else:
        result = solution(string[0])

    context = {
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def handler_django(request: HttpRequest) -> HttpResponse:
    string = request.GET.get("string")

    if not string:
        result = "Input string..."
    else:
        result = solution(string)

    context = {
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response


def solution(string):
    if len(string) > 5:
        answer = f"{string}"
    elif len(string) < 5:
        answer = "Need more!"
    else:
        answer = "It is five"

    return answer


def main():
    string = input("Enter some string --> ")
    text = solution(string)

    return text


if __name__ == "__main__":
    print(main())

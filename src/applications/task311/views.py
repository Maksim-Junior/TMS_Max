from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task311(request: HttpRequest) -> HttpResponse:
    gmail = request.GET.get("gmail")

    if not gmail:
        result = "Input your Gmail!"
    else:
        result = solution(gmail)

    context = {
        "show_text": result,
    }

    document = render(request, "task311/index.html", context)

    response = HttpResponse(document)

    return response


def solution(gmail: str) -> str:
    if gmail[-10:] == "@gmail.com":
        address = gmail
    else:
        address = "DOMAIN NAME is not supported"

    return address

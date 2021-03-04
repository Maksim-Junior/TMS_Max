from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def lesson4(_request: HttpRequest) -> HttpResponse:
    document = render(_request, "lesson4/index.html")

    response = HttpResponse(document)

    return response

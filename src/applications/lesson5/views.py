from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def lesson5(_request: HttpRequest) -> HttpResponse:
    document = render(_request, "lesson5/index.html")

    response = HttpResponse(document)

    return response

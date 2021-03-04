from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def lesson7(_request: HttpRequest) -> HttpResponse:
    document = render(_request, "lesson7/index.html")

    response = HttpResponse(document)

    return response

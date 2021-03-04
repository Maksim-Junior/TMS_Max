from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def tasks(_request: HttpRequest) -> HttpResponse:
    document = render(_request, "tasks/index.html")

    response = HttpResponse(document)

    return response

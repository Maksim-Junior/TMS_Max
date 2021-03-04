from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(_request: HttpRequest) -> HttpResponse:
    document = render(_request, "index/index.html")

    response = HttpResponse(document)

    return response

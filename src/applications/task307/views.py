from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task307(request: HttpRequest) -> HttpResponse:
    string = request.GET.get("string")

    if not string:
        result = "Input string..."
    else:
        result = solution(string)

    context = {
        "show_text": result
    }

    document = render(request, "task307/index.html", context)

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

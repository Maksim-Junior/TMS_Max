from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task703(request: HttpRequest) -> HttpResponse:
    number = request.GET.get("number")

    if not number:
        result = "Input number for find factorial..."
    else:
        result = solution(number)

    context = {
        "show_result": result
    }

    document = render(request, "task703/index.html", context)

    response = HttpResponse(document)

    return response


def solution(number):
    if number.isdigit() and int(number) > 0:
        result = 1
        for i in range(1, int(number) + 1):
            result *= i
        result = f"{number}! = {result}"
    elif number.isdigit() and int(number) == 0:
        result = "0! = 1"
    else:
        result = "Wrong input!"

    return result

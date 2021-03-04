from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task404(request: HttpRequest) -> HttpResponse:
    integer = request.GET.get("integer")

    if not integer:
        result = "Input integer..."
    else:
        result = f"--> {solution(integer)}"

    context = {
        "show_text": result
    }

    document = render(request, "task404/index.html", context)

    response = HttpResponse(document)

    return response


def solution(integer):
    if integer.isdigit():
        integer = int(integer)
        counter = 1
        sum_cubes = 0
        while counter <= integer:
            sum_cubes += counter ** 3
            counter += 1
        answer = sum_cubes
    else:
        answer = "Wrong data"
    return answer

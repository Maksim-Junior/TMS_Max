from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task406(request: HttpRequest) -> HttpResponse:
    digit1 = request.GET.get("digit1")
    digit2 = request.GET.get("digit2")

    if not digit1 and not digit2:
        result = "Input digits..."
    elif digit1 and not digit2:
        result = "Input second digit..."
    elif not digit1 and digit2:
        result = "Input first digit..."
    else:
        result = solution(digit1, digit2)

    context = {
        "show_text": result
    }

    document = render(request, "task406/index.html", context)

    response = HttpResponse(document)

    return response


def solution(first_digit, second_digit):
    if first_digit.isdigit() and second_digit.isdigit():
        fd = int(first_digit)
        sd = int(second_digit)
        if fd > sd:
            answer = "first digit(n) should be less than second digit(m)..."
        else:
            sum_cubes = 0
            for i in range(fd, sd + 1):
                sum_cubes += i ** 3
            answer = sum_cubes
    else:
        answer = "Wrong data!"
    return answer

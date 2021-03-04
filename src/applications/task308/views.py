from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task308(request: HttpRequest) -> HttpResponse:
    digit = request.GET.get("digit")

    if not digit:
        result = "Input digit..."
    else:
        cube_digit = solution(digit)
        result = f"--> {cube_digit}"

    context = {
        "show_text": result
    }

    document = render(request, "task308/index.html", context)

    response = HttpResponse(document)

    return response


def solution(digit):
    if is_number(digit) and wrong_words(digit):
        float_digit = float(digit)
        cube_digit = float_digit ** 3
        answer = round(cube_digit, 2)
    else:
        answer = "Wrong input!"
    return answer


def wrong_words(n: str) -> bool:
    if n.lower() != "nan" and n.lower() != "inf" and n.lower() != "-inf":
        answer = True
    else:
        answer = False
    return answer


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

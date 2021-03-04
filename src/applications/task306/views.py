from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task306(request: HttpRequest) -> HttpResponse:
    age = request.GET.get("age")

    result = solution(age) if age else "Input your age!"

    context = {
        "show_text": result
    }

    document = render(request, "task306/index.html", context)

    response = HttpResponse(document)

    return response


def solution(age):
    try:
        age = int(age)
        if age < 0:
            answer = "Wrong input"
        elif age < 18:
            answer = "CocaCola"
        else:
            answer = "Beer"

        return answer

    except ValueError:
        not_digit = "Wrong input"
        return not_digit

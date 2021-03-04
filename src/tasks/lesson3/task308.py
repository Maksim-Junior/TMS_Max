from django.http import HttpRequest, HttpResponse

from main.custom_types import RequestT, ResponseT
from main.util import is_number, wrong_words, render_template

TEMPLATE = "tasks/lesson3/task_308.html"


def handler(request: RequestT) -> ResponseT:
    digit = request.query.get("digit")

    if not digit:
        result = "Input digit..."
    else:
        cube_digit = solution(digit[0])
        result = f"--> {cube_digit}"

    context = {
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def handler_django(request: HttpRequest) -> HttpResponse:
    digit = request.GET.get("digit")

    if not digit:
        result = "Input digit..."
    else:
        cube_digit = solution(digit)
        result = f"--> {cube_digit}"

    context = {
        "show_text": result
    }

    document = render_template("tasks/lesson3/task_308.html", context)

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


def main():
    digit = input("Enter digit --> ")
    done_digit = solution(digit)
    return done_digit


if __name__ == "__main__":
    print(main())

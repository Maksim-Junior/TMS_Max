from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson7/task_703.html"


def handler(request: RequestT) -> ResponseT:
    number = request.query.get("number")

    if not number:
        result = "Input number for find factorial..."
    else:
        result = solution(number[0])

    context = {
        "show_result": result
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def solution(number):
    if number.isdigit() and int(number) > 0:
        result = 1
        for i in range(1, int(number) + 1):
            result *= i
    elif number.isdigit() and int(number) == 0:
        result = 1
    else:
        result = "Wrong input!"

    return result


def main():
    number = input("Input integer --> ")
    result = solution(number)

    return result


if __name__ == "__main__":
    print(main())

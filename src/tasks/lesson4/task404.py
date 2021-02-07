from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson4/task_404.html"


def handler(request: RequestT) -> ResponseT:

    integer = request.query.get("integer")

    if not integer:
        result = "Input integer..."
    else:
        result = f"--> {solution(integer[0])}"

    context = {
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

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


def main():
    integer = input("Enter integer --> ")
    sum_cubes = solution(integer)
    return sum_cubes


if __name__ == "__main__":
    print(main())

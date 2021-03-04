from random import randint

from django.http import HttpResponse, HttpRequest

from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson5/task_501.html"


def handler(request: RequestT) -> ResponseT:

    dimension = request.query.get("dimension")

    if not dimension:
        text = "Input matrix dimension..."
        matrix = ""
    else:
        my_matrix = solution(dimension[0])
        if type(my_matrix) is list:
            matrix = ""
            text = "matrix:"
            for i in my_matrix:
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i}</h2>"
        else:
            text = my_matrix
            matrix = ""

    context = {
        "show_text": text,
        "show_matrix": matrix,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def handler_django(request: HttpRequest) -> HttpResponse:

    dimension = request.GET.get("dimension")

    if not dimension:
        text = "Input matrix dimension..."
        matrix = ""
    else:
        my_matrix = solution(dimension)
        if type(my_matrix) is list:
            matrix = ""
            text = "matrix:"
            for i in my_matrix:
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i}</h2>"
        else:
            text = my_matrix
            matrix = ""

    context = {
        "show_text": text,
        "show_matrix": matrix,
    }

    document = render_template("tasks/lesson5/task_501.html", context)

    response = HttpResponse(document)

    return response


def solution(dimension):
    if dimension.isdigit():
        dimension = int(dimension)
        matrix = []
        for i in range(dimension):
            matrix.append([])
            for j in range(dimension):
                matrix[i].append(randint(1, 9))
        return matrix
    else:
        matrix = "Wrong input!"
        return matrix


def main():
    dimension = input("Enter matrix dimension --> ")
    matrix = solution(dimension)

    return matrix


if __name__ == "__main__":
    print(main())

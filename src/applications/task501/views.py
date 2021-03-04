from random import randint

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task501(request: HttpRequest) -> HttpResponse:
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
                matrix += f" {i} "
        else:
            text = my_matrix
            matrix = ""

    context = {
        "show_text": text,
        "show_matrix": matrix,
    }

    document = render(request, "task501/index.html", context)

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

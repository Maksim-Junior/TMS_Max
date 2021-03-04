from random import randint

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task502(request: HttpRequest) -> HttpResponse:
    dimension = request.GET.get("dimension")

    if not dimension:
        text = "Input matrix dimension..."
        matrix = ""
        sum_text = ""
    else:
        my_matrix, sum_elem = solution(dimension)
        if type(my_matrix) is list:
            matrix = ""
            text = "matrix:"
            sum_text = f"Sum elements --> {sum_elem}"
            for i in my_matrix:
                matrix += f" {i} "
        else:
            text = my_matrix
            matrix = ""
            sum_text = sum_elem

    context = {
        "show_text": text,
        "show_matrix": matrix,
        "show_sum": sum_text,
    }

    document = render(request, "task502/index.html", context)

    response = HttpResponse(document)

    return response


def sum_elements(matrix: list) -> int:
    if type(matrix) == list:
        calculate = 0
        for i in matrix:
            if type(i) == list:
                for j in i:
                    if type(j) == int:
                        if j % 3 == 0:
                            calculate += j
                    else:
                        calculate = ""
            else:
                calculate = ""
    else:
        calculate = ""

    return calculate


def solution(dimension: str) -> tuple:
    if dimension.isdigit():
        dimension = int(dimension)
        matrix = []
        for i in range(dimension):
            matrix.append([])
            for j in range(dimension):
                matrix[i].append(randint(1, 9))

        sum_elem = sum_elements(matrix)
    else:
        matrix = "Wrong input!"
        sum_elem = ""

    return matrix, sum_elem

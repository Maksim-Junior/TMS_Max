from random import randint

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task702(request: HttpRequest) -> HttpResponse:

    matrix_n = request.GET.get("lines_n")
    matrix_m = request.GET.get("columns_m")

    if not matrix_n and not matrix_m:
        text = "Input dimension(n x m)..."
        matrix = ""
        sum_digits = ""
        max_digit = ""
        min_digit = ""
    elif matrix_n and not matrix_m:
        text = "Input number of columns(m)..."
        matrix = ""
        sum_digits = ""
        max_digit = ""
        min_digit = ""
    elif not matrix_n and matrix_m:
        text = "Input number of lines(n)..."
        matrix = ""
        sum_digits = ""
        max_digit = ""
        min_digit = ""
    else:
        my_matrix, sum_elem, max_elem, min_elem = solution(matrix_n, matrix_m)
        if type(my_matrix) is list:
            matrix = ""
            sum_digits = f"Sum of digits --> {sum_elem}"
            max_digit = f"Max digit --> {max_elem}"
            min_digit = f"Min digit --> {min_elem}"
            text = "matrix:"
            for i in my_matrix:
                matrix += f" {i} "
        else:
            text = my_matrix
            sum_digits = sum_elem
            max_digit = max_elem
            min_digit = min_elem
            matrix = ""

    context = {
        "show_text": text,
        "show_matrix": matrix,
        "show_sum": sum_digits,
        "show_max": max_digit,
        "show_min": min_digit,
    }

    document = render(request, "task702/index.html", context)

    response = HttpResponse(document)

    return response


def create_matrix(matrix_n, matrix_m):
    if matrix_n.isdigit() and matrix_m.isdigit():
        matrix_n = int(matrix_n)
        matrix_m = int(matrix_m)
        my_matrix = []
        for i in range(matrix_n):
            my_matrix.append([])
            for j in range(matrix_m):
                my_matrix[i].append(randint(1, 9))
    else:
        my_matrix = "Wrong input!"

    return my_matrix


def sum_elem_matrix(matrix):
    if type(matrix) == list:
        sum_elem = 0
        for i in matrix:
            if type(i) == list:
                for j in i:
                    if type(j) == int:
                        sum_elem += j
                    else:
                        sum_elem = ""
            else:
                sum_elem = ""
    else:
        sum_elem = ""

    return sum_elem


def max_elem_matrix(matrix):
    if type(matrix) == list:
        max_elem = ""
        for i in matrix:
            if type(i) == list:
                for j in i:
                    if type(j) == int:
                        max_elem = max([elem for line in matrix for elem in line])
                    else:
                        max_elem = ""
            else:
                max_elem = ""
    else:
        max_elem = ""

    return max_elem


def min_elem_matrix(matrix):
    if type(matrix) == list:
        min_elem = ""
        for i in matrix:
            if type(i) == list:
                for j in i:
                    if type(j) == int:
                        min_elem = min([elem for line in matrix for elem in line])
                    else:
                        min_elem = ""
            else:
                min_elem = ""
    else:
        min_elem = ""

    return min_elem


def solution(n, m):
    matrix = create_matrix(n, m)
    sum_elements = sum_elem_matrix(matrix)
    max_element = max_elem_matrix(matrix)
    min_element = min_elem_matrix(matrix)

    result = matrix, sum_elements, max_element, min_element

    return result

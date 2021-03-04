from random import randint

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task504(request: HttpRequest) -> HttpResponse:
    matrix_n = request.GET.get("lines_n")
    matrix_m = request.GET.get("columns_m")

    if not matrix_n and not matrix_m:
        text = "Input dimension(n x m)..."
        matrix = ""
        count_digits = ""
    elif matrix_n and not matrix_m:
        text = "Input number of columns(m)..."
        matrix = ""
        count_digits = ""
    elif not matrix_n and matrix_m:
        text = "Input number of lines(n)..."
        matrix = ""
        count_digits = ""
    else:
        my_matrix, count = solution(matrix_n, matrix_m)
        if type(my_matrix) is list:
            matrix = ""
            count_digits = f"Count of digits --> {count}"
            text = "matrix:"
            for i in my_matrix:
                matrix += f" {i} "
        else:
            text = my_matrix
            count_digits = count
            matrix = ""

    context = {
        "show_text": text,
        "show_matrix": matrix,
        "show_count": count_digits
    }

    document = render(request, "task504/index.html", context)

    response = HttpResponse(document)

    return response


def count_elements(matrix):
    if type(matrix) == list:
        calculate = 0
        counter = 0
        for i in matrix:
            if type(i) == list:
                for j in i:
                    if type(j) == int:
                        counter += j
                    else:
                        calculate = ""
            else:
                calculate = ""

        average_value = counter / (len(matrix) * len(matrix[0]))
        if type(average_value) == float and average_value >= 1:
            for line in range(len(matrix)):
                for column in range(len(matrix[0])):
                    sum_inx = line + column
                    if float(matrix[line][column]) > average_value and sum_inx > 0 and sum_inx % 2 == 0:
                        calculate += 1
    else:
        calculate = ""

    return calculate


def solution(matrix_n, matrix_m):
    if matrix_n.isdigit() and matrix_m.isdigit():
        matrix_n = int(matrix_n)
        matrix_m = int(matrix_m)
        my_matrix = []
        for i in range(matrix_n):
            my_matrix.append([])
            for j in range(matrix_m):
                my_matrix[i].append(randint(1, 9))

        count = count_elements(my_matrix)
    else:
        my_matrix = "Wrong input!"
        count = ""

    return my_matrix, count

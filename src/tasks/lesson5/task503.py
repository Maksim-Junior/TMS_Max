from random import randint

from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson5/task_503.html"


def handler(request: RequestT) -> ResponseT:

    mass_n = request.query.get("lines_n")
    mass_m = request.query.get("columns_m")

    if not mass_n and not mass_m:
        text = "Input dimension(n x m)..."
        matrix = ""
        sum_seven = ""
    elif mass_n and not mass_m:
        text = "Input number of columns(m)..."
        matrix = ""
        sum_seven = ""
    elif not mass_n and mass_m:
        text = "Input number of lines(n)..."
        matrix = ""
        sum_seven = ""
    else:
        my_matrix, count_seven = solution(mass_n[0], mass_m[0])
        if type(my_matrix) is list:
            matrix = ""
            text = "matrix:"
            sum_seven = f"Count of seven --> {count_seven}"
            for i in my_matrix:
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i}</h2>"
        else:
            text = my_matrix
            sum_seven = count_seven
            matrix = ""

    context = {
        "show_text": text,
        "show_matrix": matrix,
        "show_seven": sum_seven,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def count_of_seven(matrix: list) -> int:
    if type(matrix) == list:
        calculate = 0
        for i in matrix:
            if type(i) == list:
                for j in i:
                    if type(j) == int:
                        if j == 7:
                            calculate += 1
                    else:
                        calculate = ""
            else:
                calculate = ""
    else:
        calculate = ""

    return calculate


def solution(mass_n, mass_m):
    if mass_n.isdigit() and mass_m.isdigit():
        mass_n = int(mass_n)
        mass_m = int(mass_m)
        matrix = []
        for i in range(mass_n):
            matrix.append([])
            for j in range(mass_m):
                matrix[i].append(randint(1, 9))

        count_seven = count_of_seven(matrix)
    else:
        matrix = "Wrong input!"
        count_seven = ""

    return matrix, count_seven


def main():
    mass_n = input("Enter number of lines(n) --> ")
    mass_m = input("Enter number of columns(m) --> ")

    matrix, count_seven = solution(mass_n, mass_m)

    return matrix, count_seven


if __name__ == "__main__":
    print(main())

from random import randint
from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson5/task_502.html"


def handler(request: RequestT) -> ResponseT:

    dimension = request.query.get("dimension")

    if not dimension:
        text = "Input matrix dimension..."
        matrix = ""
        sum_text = ""
    else:
        my_matrix, sum_elem = solution(dimension[0])
        if type(my_matrix) is list:
            matrix = ""
            text = "matrix:"
            sum_text = f"Sum elements --> {sum_elem}"
            for i in my_matrix:
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i}</h2>"
        else:
            text = my_matrix
            matrix = ""
            sum_text = sum_elem

    context = {
        "show_text": text,
        "show_matrix": matrix,
        "show_sum": sum_text,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

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


def main():
    dimension = input("Enter matrix dimension --> ")
    matrix, sum_el = solution(dimension)

    return matrix, sum_el


if __name__ == "__main__":
    print(main())

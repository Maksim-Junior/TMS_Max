from random import randint


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

from random import randint


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


def main():
    dimension_n = input("Input matrix dimension n --> ")
    dimension_m = input("Input matrix dimension m --> ")
    matrix = create_matrix(dimension_n, dimension_m)
    sum_elements = sum_elem_matrix(matrix)
    max_element = max_elem_matrix(matrix)
    min_element = min_elem_matrix(matrix)
    result = matrix, sum_elements, max_element, min_element

    return result


if __name__ == "__main__":
    print(main())

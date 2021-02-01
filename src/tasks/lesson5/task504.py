from random import randint


def solution(matrix_n, matrix_m):
    try:
        matrix_n = int(matrix_n)
        matrix_m = int(matrix_m)
        web_matrix = []
        my_matrix = []
        for i in range(matrix_n):
            web_matrix.append([""])
            my_matrix.append([])
            for j in range(matrix_m):
                a = randint(1, 9)
                web_matrix[i][0] += f"{str(a)} "
                my_matrix[i].append(a)
        count = 0
        for line in my_matrix:
            for elem_line in line:
                count += elem_line
        average_value = count / (matrix_n * matrix_m)

        count_of_digits = 0
        for line_el in range(matrix_n):
            for column_el in range(matrix_m):
                if float(my_matrix[line_el][column_el]) > average_value and (line_el + column_el) % 2 == 0:
                    count_of_digits += 1
        text_digits = f"Count of elements --> {count_of_digits} "
        return web_matrix, text_digits
    except ValueError:
        web_matrix = "Wrong input!"
        text_digits = ""

        return web_matrix, text_digits


def main():
    matrix_n = input("Enter number of lines --> ")
    matrix_m = input("Enter number of columns --> ")

    web_matrix, text_digits = solution(matrix_n, matrix_m)

    return web_matrix, text_digits


if __name__ == "__main__":
    print(main())
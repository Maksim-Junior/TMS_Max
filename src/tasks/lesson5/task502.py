from random import randint


def solution(dimension):
    try:
        dimension = int(dimension)
        digits_of_matrix = []
        matrix = []
        for i in range(dimension):
            matrix.append([""])
            for j in range(dimension):
                a = randint(1, 9)
                matrix[i][0] += f"{str(a)} "
                digits_of_matrix.append(a)
        sum_digits = 0
        for elem in digits_of_matrix:
            if elem % 3 == 0:
                sum_digits += elem
        text_sum = f"Sum elements --> {sum_digits}"
        return matrix, text_sum
    except ValueError:
        matrix = "Wrong input!"
        text_sum = ""
        return matrix, text_sum


def main():
    dimension = input("Enter matrix dimension --> ")
    matrix, sum_elements = solution(dimension)

    return matrix, sum_elements


if __name__ == "__main__":
    print(main())

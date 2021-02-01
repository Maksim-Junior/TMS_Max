from random import randint


def solution(mass_n, mass_m):
    try:
        mass_n = int(mass_n)
        mass_m = int(mass_m)
        digits_of_matrix = []
        matrix = []
        for i in range(mass_n):
            matrix.append([""])
            for j in range(mass_m):
                a = randint(1, 9)
                matrix[i][0] += f"{str(a)} "
                digits_of_matrix.append(a)
        number_seven = 0
        for elem in digits_of_matrix:
            if elem == 7:
                number_seven += 1
        text_seven = f"Number of seven --> {number_seven}"
        return matrix, text_seven
    except ValueError:
        matrix = "Wrong input!"
        text_seven = ""
        return matrix, text_seven


def main():
    mass_n = input("Enter number of lines(n) --> ")
    mass_m = input("Enter number of columns(m) --> ")

    matrix, count_seven = solution(mass_n, mass_m)

    return matrix, count_seven


if __name__ == "__main__":
    print(main())

from random import randint


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

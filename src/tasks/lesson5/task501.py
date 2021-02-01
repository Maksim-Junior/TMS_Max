from random import randint


def solution(dimension):
    try:
        dimension = int(dimension)
        matrix = []
        for i in range(dimension):
            matrix.append([""])
            for j in range(dimension):
                matrix[i][0] += f"{str(randint(1, 9))} "
        return matrix
    except ValueError:
        matrix = "Wrong input!"
        return matrix


def main():
    dimension = input("Enter matrix dimension --> ")
    matrix = solution(dimension)

    return matrix


if __name__ == "__main__":
    print(main())

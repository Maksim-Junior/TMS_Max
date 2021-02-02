from random import randint


def solution(dimension):
    if dimension.isdigit():
        dimension = int(dimension)
        matrix = []
        for i in range(dimension):
            matrix.append([])
            for j in range(dimension):
                matrix[i].append(randint(1, 9))
        return matrix
    else:
        matrix = "Wrong input!"
        return matrix


def main():
    dimension = input("Enter matrix dimension --> ")
    matrix = solution(dimension)

    return matrix


if __name__ == "__main__":
    print(main())

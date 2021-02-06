def solution(number):
    if number.isdigit() and int(number) > 0:
        result = 1
        for i in range(1, int(number) + 1):
            result *= i
    elif number.isdigit() and int(number) == 0:
        result = 1
    else:
        result = "Wrong input!"

    return result


def main():
    number = input("Input integer --> ")
    result = solution(number)

    return result


if __name__ == "__main__":
    print(main())

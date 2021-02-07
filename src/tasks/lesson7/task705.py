def sum_args(*args):
    args = args[0]
    calculate_args = 0
    for i in range(len(args)):
        calculate_args += args[i] * i

    return calculate_args


def main():
    digits = [1, 2, 3, 4, 5]
    result = sum_args(digits)

    return result


if __name__ == "__main__":
    print(main())

def solution(first_digit, second_digit):
    if first_digit.isdigit() and second_digit.isdigit():
        fd = int(first_digit)
        sd = int(second_digit)
        if fd > sd:
            answer = "first digit(n) should be less than second digit(m)..."
        else:
            sum_cubes = 0
            for i in range(fd, sd + 1):
                sum_cubes += i ** 3
            answer = sum_cubes
    else:
        answer = "Wrong data!"
    return answer


def main():
    first_digit = input("Enter first digit --> ")
    second_digit = input("Enter second digit --> ")

    sum_cubes = solution(first_digit, second_digit)

    return sum_cubes


if __name__ == "__main__":
    print(main())

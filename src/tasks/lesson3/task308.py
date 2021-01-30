def solution(digit):
    try:
        float_digit = float(digit)
        cube_digit = float_digit ** 3
        str_cube = str(round(cube_digit, 2))
        answer = f"--> {str_cube}"
        return answer
    except ValueError:
        answer = "Wrong input!"
        return answer


def main():
    digit = input("Enter digit --> ")
    done_digit = solution(digit)
    return done_digit


if __name__ == "__main__":
    print(main())
def wrong_words(n: str):
    if n.lower() != "nan" and n.lower() != "inf" and n.lower() != "-inf":
        answer = True
    else:
        answer = False
    return answer


def is_number(n):
    try:
        n = float(n)
        return True
    except ValueError:
        return False


def solution(digit):
    if is_number(digit) and wrong_words(digit):
        float_digit = float(digit)
        cube_digit = float_digit ** 3
        answer = round(cube_digit, 2)
    else:
        answer = "Wrong input!"
    return answer


def main():
    digit = input("Enter digit --> ")
    done_digit = solution(digit)
    return done_digit


if __name__ == "__main__":
    print(main())

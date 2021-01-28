def solution(age):
    not_digit = "Wrong input"
    try:
        age = int(age)
    except ValueError:
        return not_digit

    if age < 0:
        answer = "Wrong input"
    elif age < 18:
        answer = "CocaCola"
    else:
        answer = "Beer"

    return answer


def main():
    age = input("Enter your age --> ")
    control = solution(age)

    return control


if __name__ == "__main__":
    print(main())

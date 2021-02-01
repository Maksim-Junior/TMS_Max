def solution(age):
    try:
        age = int(age)
        if age < 0:
            answer = "Wrong input"
        elif age < 18:
            answer = "CocaCola"
        else:
            answer = "Beer"

        return answer

    except ValueError:
        not_digit = "Wrong input"
        return not_digit


def main():
    age = input("Enter your age --> ")
    control = solution(age)

    return control


if __name__ == "__main__":
    print(main())

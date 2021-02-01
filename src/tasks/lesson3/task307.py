def solution(string):
    if len(string) > 5:
        answer = f'"{string}"'
    elif len(string) < 5:
        answer = "Need more!"
    else:
        answer = "It is five"

    return answer


def main():
    string = input("Enter some string --> ")
    text = solution(string)

    return text


if __name__ == "__main__":
    print(main())

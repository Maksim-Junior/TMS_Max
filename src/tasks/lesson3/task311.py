def solution(gmail: str) -> bool:
    if gmail[-10:] == "@gmail.com":
        address = True
    else:
        address = False

    return address


def main():
    gmail = input("Enter your gmail address --> ")
    done_address = solution(gmail)
    if done_address:
        text = gmail
    else:
        text = "DOMAIN NAME is not supported"

    return text


if __name__ == "__main__":
    print(main())

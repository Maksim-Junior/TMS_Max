def solution(gmail: str) -> str:
    if gmail[-10:] == "@gmail.com":
        address = gmail
    else:
        address = "DOMAIN NAME is not supported"

    return address


def main():
    gmail = input("Enter your gmail address --> ")
    done_address = solution(gmail)

    return done_address


if __name__ == "__main__":
    print(main())

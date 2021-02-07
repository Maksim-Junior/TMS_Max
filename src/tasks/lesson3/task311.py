from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson3/task_311.html"


def handler(request: RequestT) -> ResponseT:

    gmail = request.query.get("gmail")

    if not gmail:
        result = "Input your Gmail!"
    else:
        result = solution(gmail[0])

    context ={
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


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

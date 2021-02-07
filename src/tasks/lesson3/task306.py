from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson3/task_306.html"


def handler(request: RequestT) -> ResponseT:

    age = request.query.get("age")

    result = solution(age[0]) if age else "Input your age!"

    context = {
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


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

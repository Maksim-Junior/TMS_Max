from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson4/task_407.html"


def handler(request: RequestT) -> ResponseT:

    integer1 = request.query.get("integer1")
    integer2 = request.query.get("integer2")

    if not integer1 and not integer2:
        text = "Input integers..."
        show_count = ""
    elif integer1 and not integer2:
        text = "Input second integer..."
        show_count = ""
    elif not integer1 and integer2:
        text = "Input first integer..."
        show_count = ""
    else:
        numbers, count = solution(integer1[0], integer2[0])
        if type(numbers) is list:
            text = "--> "
            for i in numbers:
                text += f"{i} "
            show_count = f"Count of numbers --> {count}"
        else:
            text = numbers
            show_count = count

    context = {
        "show_text": text,
        "show_count": show_count,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def solution(fst_int, scd_int):
    if fst_int.isdigit() and scd_int.isdigit():
        fst_int = int(fst_int)
        scd_int = int(scd_int)
        if fst_int >= scd_int:
            answer = "first integer(A) should be less than second integer(B)..."
            count = ""
        else:
            answer = []
            for i in range(fst_int, scd_int + 1):
                answer.append(i)
            count = len(answer)
    else:
        answer = "Wrong data!"
        count = ""
    return answer, count


def main():
    first_integer = input("Enter first integer --> ")
    second_integer = input("enter second integer --> ")

    answer, count = solution(first_integer, second_integer)

    return answer, count


if __name__ == "__main__":
    print(main())

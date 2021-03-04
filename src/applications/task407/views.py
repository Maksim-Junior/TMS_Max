from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task407(request: HttpRequest) -> HttpResponse:
    integer1 = request.GET.get("integer1")
    integer2 = request.GET.get("integer2")

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
        numbers, count = solution(integer1, integer2)
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

    document = render(request, "task407/index.html", context)

    response = HttpResponse(document)

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

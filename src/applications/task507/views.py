import os
from random import randint
from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def task507(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()

    get_client(request, response)

    from_n = request.POST.get("from_n")
    to_m = request.POST.get("to_m")
    number = request.POST.get("number")

    if request.session["task507_from"] == 0 and request.session["task507_to"] == 0:
        if not from_n and not to_m:
            result = "Input range!"
        elif not from_n and to_m:
            result = "Input from what number"
        elif from_n and not to_m:
            result = "Input until which number"
        else:
            if from_n.isdigit() and to_m.isdigit() and int(from_n) <= int(to_m):
                request.session["task507_from"] = int(from_n)
                request.session["task507_to"] = int(to_m)
                result = "You have three attempts. Input your answer..."
            else:
                result = "Wrong input..."
    else:
        if not number:
            result = "Input your answer"
        else:
            if number.isdigit():
                rand_number = randint(request.session["task507_from"], request.session["task507_to"])
                if request.session["task507_attempts"] > 1:
                    if int(number) > rand_number:
                        result = f'Your number is greater. Attempts: {request.session["task507_attempts"] - 1}'
                        request.session["task507_attempts"] -= 1
                    elif int(number) < rand_number:
                        result = f'Your number is lower. Attempts: {request.session["task507_attempts"] - 1}'
                        request.session["task507_attempts"] -= 1
                    else:
                        request.session["task507_from"] = 0
                        request.session["task507_to"] = 0
                        request.session["task507_attempts"] = 3
                        result = f"You are the winner! --> {rand_number}"
                else:
                    request.session["task507_from"] = 0
                    request.session["task507_to"] = 0
                    request.session["task507_attempts"] = 3
                    result = f"You are the loser! --> {rand_number}"

            else:
                result = "Wrong input!"

    context = {
        "show_text": result
    }

    document = render(request, "task507/index.html", context)

    response.content = document

    return response


def get_client(request: HttpRequest, response: HttpResponse) -> Optional[str]:
    def client():
        cn = f"{os.urandom(8).hex()}_django"
        response.cookies["session"] = cn
        response.cookies["session"]["path"] = "/"
        return cn

    morsel = request.COOKIES.get("session")
    if not morsel:
        request.session["task507_from"] = 0
        request.session["task507_to"] = 0
        request.session["task507_attempts"] = 0
        client_name = client()
    else:
        request.session["task507_from"] = 0 if not request.session["task507_from"] else request.session["task507_from"]
        request.session["task507_to"] = 0 if not request.session["task507_to"] else request.session["task507_to"]
        request.session["task507_attempts"] = 3 if not request.session["task507_attempts"]\
            else request.session["task507_attempts"]
        client_name = morsel

    return client_name

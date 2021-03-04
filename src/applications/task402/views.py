import os
from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def task402(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    get_client(request, response)

    client_data = request.POST.get("number")

    if not client_data:
        result = "Input number..."
    else:
        if client_data == "stop":
            numbers = request.session["task402"]
            result = f"Answer: {numbers}"
            request.session["task402"] = 0
        elif client_data.isnumeric():
            number = int(client_data)
            request.session["task402"] += number
            result = f"The number {number} was written down..."
        else:
            result = "Wrong input!"

    context = {
        "show_text": result
    }

    document = render(request, "task402/index.html", context)

    response.content = document

    return response


def get_client(request: HttpRequest, response: HttpResponse) -> Optional[str]:
    def client():
        request.session["task402"] = 0
        cn = f"{os.urandom(8).hex()}_django"
        response.cookies["session"] = cn
        response.cookies["session"]["path"] = "/"
        return cn

    morsel = request.COOKIES.get("session")
    if not morsel:
        client_name = client()
    else:
        client_name = morsel

    return client_name

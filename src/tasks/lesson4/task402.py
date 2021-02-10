import os
from typing import Optional

from framework.dirs import DIR_STORAGE
from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson4/task_402.html"


def handler(request: RequestT) -> ResponseT:
    client_data = request.query.get("number")

    client_name = get_client(request) or create_new_client()
    if not client_data:
        result = "Input number..."
    else:
        if client_data[0] == "stop":
            sum_numbers = calc_sum(client_name)
            clear_file = document_cleaning(client_name)
            result = f"Answer: {sum_numbers}. {clear_file}"
        elif client_data[0].isnumeric():
            number = int(client_data[0])
            result = f"The number {add_number(client_name, number)} was written down..."
        else:
            result = "Wrong input!"

    headers = {
        "Set-Cookie": f"name={client_name}"
    }

    context = {
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(headers=headers, payload=document)

    return response


def create_new_client() -> str:
    return os.urandom(8).hex()


def calc_sum(client_name: str) -> int:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    with user_data_file.open("r") as src:
        result = sum(int(line.strip()) for line in src.readlines())

    return result


def document_cleaning(client_name: str) -> str:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    with user_data_file.open("w") as file:
        file.close()
    answer = "The file has been cleared..."

    return answer


def add_number(client_name: str, number: int) -> int:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    with user_data_file.open("a") as dst:
        dst.write(f"{number}\n")

    return number


def get_client(request: RequestT) -> Optional[str]:
    cookies = request.headers.get("Cookie")
    if not cookies:
        return None

    cookie_name, cookie_value = cookies.split("=")
    assert cookie_name == "name"
    if not cookie_value:
        return None
    return cookie_value

import os
from typing import Optional

from framework.dirs import DIR_STORAGE
from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson4/task_402.html"


def handler(request: RequestT) -> ResponseT:
    client_data = request.post_req.get("number")

    response = ResponseT()

    client_name = get_client(request)
    if not client_name:
        client_name = os.urandom(8).hex()
        response.cookies["session"] = client_name
        response.cookies["session"]["path"] = "/"
    if not find_task(client_name):
        add_task(client_name)
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

    context = {
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    response.payload = document

    return response


def calc_sum(client_name: str) -> int:
    dict_task = user_tasks_dict(client_name)
    result = dict_task["task402"]

    return result


def document_cleaning(client_name: str) -> str:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    dict_task = user_tasks_dict(client_name)
    dict_task["task402"] = 0
    with user_data_file.open("w") as file:
        for key, value in dict_task.items():
            file.write(f"{key}={value}\n")
    answer = "The file has been cleared..."

    return answer


def add_number(client_name: str, number: int) -> int:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    dict_task = user_tasks_dict(client_name)
    dict_task["task402"] = int(dict_task["task402"]) + int(number)

    with user_data_file.open("w") as dst:
        for key, value in dict_task.items():
            dst.write(f"{key}={value}\n")

    return number


def add_task(client_name: str) -> bool:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    with user_data_file.open("a") as new_task:
        new_task.write("task402=0\n")

    return True


def user_tasks_dict(client_name: str) -> dict:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"

    with user_data_file.open("a"):
        pass

    with user_data_file.open("r") as dst:
        list_tasks = (line.strip() for line in dst.readlines())
        dict_task = {}
        for tasks in list_tasks:
            key, value = tasks.split("=")
            dict_task[key] = int(value)

    return dict_task


def find_task(client_name: str) -> bool:
    dict_tasks = user_tasks_dict(client_name)
    task = dict_tasks.get("task402", "")
    if task == "":
        answer = False
    else:
        answer = True

    return answer


def get_client(request: RequestT) -> Optional[str]:
    if not request.cookies:
        return None

    morsel = request.cookies.get("session")
    if not morsel:
        return None

    return morsel.value or None

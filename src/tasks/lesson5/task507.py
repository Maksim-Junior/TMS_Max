import os
from http.cookies import SimpleCookie
from random import randint
from typing import Optional

from framework.dirs import DIR_STORAGE
from main.custom_types import RequestT, ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson5/task_507.html"


def handler(request: RequestT) -> ResponseT:
    from_n = request.post_req.get("from_n")
    to_m = request.post_req.get("to_m")
    number = request.post_req.get("number")

    response = ResponseT()

    client_name = get_client(request)
    if not client_name:
        client_name = os.urandom(8).hex()
        response.cookies["session"] = client_name
        response.cookies["session"]["path"] = "/"

    if not find_task(client_name):
        add_task(client_name)

    dict_tasks = user_tasks_dict(client_name)

    if dict_tasks["task507"] == "0":
        if not from_n and not to_m:
            result = "Input range!"
        elif not from_n and to_m:
            result = "Input from what number"
        elif from_n and not to_m:
            result = "Input until which number"
        else:
            if from_n[0].isdigit() and to_m[0].isdigit() and int(from_n[0]) <= int(to_m[0]):
                rand_number = randint(int(from_n[0]), int(to_m[0]))
                add_number(client_name, rand_number)
                result = "You have three attempts. Input your answer..."
            else:
                result = "Wrong input..."
    else:
        if not number:
            result = "Input your answer"
        else:
            if number[0].isdigit():
                result = compare_numbers(client_name, int(number[0]))
            else:
                result = "Wrong input!"

    context = {
        "show_text": result
    }

    document = render_template(TEMPLATE, context)

    cookie = SimpleCookie()
    cookie["name"] = client_name

    response = ResponseT(payload=document, cookie=cookie)

    return response


def document_cleaning(client_name: str) -> str:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    dict_task = user_tasks_dict(client_name)
    dict_task["task507"] = 0
    with user_data_file.open("w") as file:
        for key, value in dict_task.items():
            file.write(f"{key}={value}\n")
    answer = ""

    return answer


def add_number(client_name: str, number: int) -> int:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    dict_task = user_tasks_dict(client_name)
    dict_task["task507"] = f"{number}-3"

    with user_data_file.open("w") as dst:
        for key, value in dict_task.items():
            dst.write(f"{key}={value}\n")

    return number


def add_task(client_name: str) -> bool:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"
    with user_data_file.open("a") as new_task:
        new_task.write("task507=0\n")

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
            dict_task[key] = value

    return dict_task


def find_task(client_name: str) -> bool:
    dict_tasks = user_tasks_dict(client_name)
    task = dict_tasks.get("task507", "")
    if task == "":
        answer = False
    else:
        answer = True

    return answer


def compare_numbers(client_name: str, number: int) -> str:
    dict_tasks = user_tasks_dict(client_name)
    this_task = dict_tasks["task507"]
    digit, attempts = this_task.split("-")
    if int(digit) == number:
        answer = f"You are the winner! ({digit})"
        document_cleaning(client_name)
    elif int(digit) > number:
        attempts = decrease_attempts(client_name)
        if attempts > 0:
            answer = f"Wrong! Your digit is less. You have {attempts} attempt(s)"
        else:
            answer = f"You are the loser! -> ({digit})"
            document_cleaning(client_name)
    else:
        attempts = decrease_attempts(client_name)
        if attempts > 0:
            answer = f"Wrong! Your digit is greater. You have {attempts} attempt(s)"
        else:
            answer = f"You are the loser! -> ({digit})"
            document_cleaning(client_name)

    return answer


def get_client(request: RequestT) -> Optional[str]:
    if not request.cookies:
        return None

    morsel = request.cookies.get("session")
    if not morsel:
        return None

    return morsel.value or None


def decrease_attempts(client_name: str) -> int:
    user_data_file = DIR_STORAGE / f"{client_name}.txt"

    dict_tasks = user_tasks_dict(client_name)
    this_task = dict_tasks["task507"]
    digit, attempts = this_task.split("-")
    attempts = int(attempts) - 1
    dict_tasks["task507"] = f"{digit}-{attempts}"

    with user_data_file.open("w") as dst:
        for key, value in dict_tasks.items():
            dst.write(f"{key}={value}\n")

    return attempts

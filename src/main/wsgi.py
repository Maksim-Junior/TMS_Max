from typing import Tuple
from urllib.parse import parse_qs

import sentry_sdk

from framework.dirs import DIR_SRC, DIR_TASKS
from framework.util.settings import get_setting
from tasks.lesson3 import task310, task311, task306, task307, task308
from tasks.lesson4 import task404, task406, task407
from tasks.lesson5 import task501

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

ResponseT = Tuple[str, str, str]


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def tasks_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("tasks.html")
    return status, content_type, payload


def lesson3_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("lesson3/lesson3.html")
    return status, content_type, payload


def task_306_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson3/task_306.html")
    age = qsi.get("age")

    if not age:
        age_control = "Input your age!"
    else:
        age_control = task306.solution(age[0])

    payload = task.format(show_text=age_control)

    return status, content_type, payload


def task_307_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson3/task_307.html")
    string = qsi.get("string")

    if not string:
        text = "Input string..."
    else:
        text = task307.solution(string[0])

    payload = task.format(show_text=text)

    return status, content_type, payload


def task_308_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson3/task_308.html")
    digit = qsi.get("digit")

    if not digit:
        text = "Input digit..."
    else:
        cube_digit = task308.solution(digit[0])
        if cube_digit[-1] == "0":
            text = cube_digit[:-2]
        else:
            text = cube_digit

    payload = task.format(show_text=text)

    return status, content_type, payload


def task_310_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson3/task_310.html")
    money = qsi.get("money")

    show_rubles = ""
    show_penny = ""
    show_text = ""

    wrong_words = {
        "nan": "nan",
        "Nan": "Nan",
        "nAn": "nAn",
        "naN": "naN",
        "NAn": "NAn",
        "NaN": "NaN",
        "nAN": "nAN",
        "NAN": "NAN",
        "-inf": "-inf",
    }

    if not money:
        show_rubles = ""
        show_penny = ""
        show_text = "Input count of money!"
    elif money[0] != wrong_words.get(money[0], False) and is_number(money[0]) or money[0].isdigit():
        money = money[0]
        text, rubles, penny = task310.solution(money)
        for i in rubles:
            show_rubles += f"<h2><p style = 'color:#E6E6FA'>{i}</p></h2>"

        for j in penny:
            show_penny += f"<h2><p style = 'color:#E6E6FA'>{j}</p></h2>"

        show_text += text
    else:
        show_rubles = ""
        show_penny = ""
        show_text = "Wrong data!"

    payload = task.format(show_text=show_text, show_rubles=show_rubles, show_penny=show_penny)

    return status, content_type, payload


def task_311_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson3/task_311.html")
    gmail = qsi.get("gmail")

    if not gmail:
        show_text = "Input your Gmail!"
    else:
        gmail = gmail[0]
        done_address = task311.solution(gmail)
        if done_address:
            show_text = gmail
        else:
            show_text = "DOMAIN NAME is not supported"
    payload = task.format(show_text=show_text)

    return status, content_type, payload


def lesson4_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("lesson4/lesson4.html")
    return status, content_type, payload


def task_404_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson4/task_404.html")
    integer = qsi.get("integer")

    if not integer:
        text = "Input integer..."
    else:
        text = task404.solution(integer[0])

    payload = task.format(show_text=text)

    return status, content_type, payload


def task_406_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson4/task_406.html")
    digit1 = qsi.get("digit1")
    digit2 = qsi.get("digit2")

    if not digit1 and not digit2:
        text = "Input digits..."
    elif digit1 and not digit2:
        text = "Input second digit..."
    elif not digit1 and digit2:
        text = "Input first digit..."
    else:
        text = task406.solution(digit1[0], digit2[0])
    payload = task.format(show_text=text)

    return status, content_type, payload


def task_407_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson4/task_407.html")
    integer1 = qsi.get("integer1")
    integer2 = qsi.get("integer2")

    if not integer1 and not integer2:
        text = "Input integers..."
        count = ""
    elif integer1 and not integer2:
        text = "Input second integer..."
        count = ""
    elif not integer1 and integer2:
        text = "Input first integer..."
        count = ""
    else:
        text, count = task407.solution(integer1[0], integer2[0])

    payload = task.format(show_text=text, show_count=count)

    return status, content_type, payload


def lesson5_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("lesson5/lesson5.html")
    return status, content_type, payload


def task_501_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson5/task_501.html")
    dimension = qsi.get("dimension")

    if not dimension:
        text = "Input matrix dimension..."
        matrix = ""
    else:
        my_matrix = task501.solution(dimension[0])
        if type(my_matrix) is list:
            matrix = ""
            text = "matrix:"
            for i in my_matrix:
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i[0]}</h2>"
        else:
            text = my_matrix
            matrix = ""
    payload = task.format(show_text=text, show_matrix=matrix)

    return status, content_type, payload


def division_zero_page(method: str, path: str, qs: str) -> ResponseT:
    status = "500 Internal Server Error"
    content_type = "text/html"
    payload = str(1 / 0)
    return status, content_type, payload


def not_found_page(method: str, path: str, qs: str) -> ResponseT:
    status = "404 not found"
    content_type = "text/html"
    payload = read_template("notFound.html")
    return status, content_type, payload


def index_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_template("index.html")
    return status, content_type, payload


def environ_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_template("environ.html")
    return status, content_type, payload


HANDLERS = {
    '/': index_page,
    '/environ/': environ_page,
    '/e/': division_zero_page,
    '/tasks/': tasks_page,
    '/tasks/lesson3/': lesson3_page,
    '/tasks/lesson3/task306/': task_306_page,
    '/tasks/lesson3/task307/': task_307_page,
    '/tasks/lesson3/task308/': task_308_page,
    '/tasks/lesson3/task310/': task_310_page,
    '/tasks/lesson3/task311/': task_311_page,
    '/tasks/lesson4/': lesson4_page,
    '/tasks/lesson4/task404/': task_404_page,
    '/tasks/lesson4/task406/': task_406_page,
    '/tasks/lesson4/task407/': task_407_page,
    '/tasks/lesson5/': lesson5_page,
    '/tasks/lesson5/task501/': task_501_page,
}


def application(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    query_string = environ["QUERY_STRING"]

    headers = {
        "Content-type": "text/html",
    }

    web_page = HANDLERS.get(path, not_found_page)

    status, content_type, payload = web_page(method, path, query_string)

    show_environ = environ_formation(environ)

    start_response(status, list(headers.items()))

    show_web_page = payload.format(environ=show_environ).encode()

    yield show_web_page


def environ_formation(environ: dict) -> str:
    show_environ = ""
    for key, value in environ.items():
        show_environ += (f"<p style = 'color:#E6E6FA'>{key}:"
                         "<span style = 'color:#FFA07A;font-family: courier, monospace;'>"
                         f" {value}</span></p>"
                         )
    return show_environ


def read_tasks(task_name: str) -> str:
    task = DIR_TASKS / task_name

    assert task.is_file()

    with task.open("r") as tsk:
        content_task = tsk.read()

    return content_task


def read_template(template_name: str) -> str:
    dir_templates = DIR_SRC / "main" / "templates"
    template = dir_templates / template_name

    assert template.is_file()

    with template.open("r") as fd:
        content = fd.read()

    return content

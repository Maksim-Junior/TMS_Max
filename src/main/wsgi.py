from typing import Tuple, Callable
from urllib.parse import parse_qs

import sentry_sdk

from framework.dirs import DIR_SRC, DIR_TASKS
from framework.util.settings import get_setting
from tasks.lesson3 import task310, task311

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

ResponseT = Tuple[str, str, str]


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def task_310_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    task = read_tasks("lesson3/task_310.html")
    money = qsi.get("money")

    show_rubles = ""
    show_penny = ""
    show_text = ""

    if not money:
        show_rubles = ""
        show_penny = ""
        show_text = "Input count of money!"
    elif is_number(money[0]) or money[0].isdigit():
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


def tasks_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("tasks.html")
    return status, content_type, payload


def lesson3_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("lesson3.html")
    return status, content_type, payload


HANDLERS = {
    '/': index_page,
    '/environ/': environ_page,
    '/e/': division_zero_page,
    '/tasks/': tasks_page,
    '/tasks/lesson3/': lesson3_page,
    '/tasks/lesson3/task310/': task_310_page,
    '/tasks/lesson3/task311/': task_311_page,
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

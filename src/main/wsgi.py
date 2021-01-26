import sentry_sdk

from framework.dirs import DIR_SRC
from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)


def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }

    path = extract_path(environ)

    handlers = {
        '/': index_page,
        '/environ/': environ_page
    }

    web_page = handlers[path]

    show_environ = environ_formation(environ)

    start_response(status, list(headers.items()))

    yield web_page().format(environ=show_environ).encode()


def environ_formation(environ):
    show_environ = ""
    for key, value in environ.items():
        show_environ += (f"<p style = 'color:#E6E6FA'>{key}:"
                         "<span style = 'color:#FFA07A;font-family: courier, monospace;'>"
                         f" {value}</span></p>"
                         )
    return show_environ


def extract_path(environ) -> str:
    return environ["PATH_INFO"]


def index_page() -> str:
    return read_template("index.html")


def environ_page() -> str:
    return read_template("environ.html")


def read_template(template_name: str) -> str:
    dir_templates = DIR_SRC / "main" / "templates"
    template = dir_templates / template_name

    assert template.is_file()

    with template.open("r") as fd:
        content = fd.read()

    return content

from pathlib import Path
from typing import Union, Optional, Dict
from urllib.parse import parse_qs

from framework.dirs import DIR_TEMPLATES
from main.custom_types import RequestT


def wrong_words(n: str) -> bool:
    if n.lower() != "nan" and n.lower() != "inf" and n.lower() != "-inf":
        answer = True
    else:
        answer = False
    return answer


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


def environ_formation(environ: dict) -> str:
    show_environ = ""
    for key, value in environ.items():
        show_environ += (f"<p style = 'color:#E6E6FA'>{key}:"
                         "<span style = 'color:#FFA07A;font-family: courier, monospace;'>"
                         f" {value}</span></p>"
                         )
    return show_environ


def render_template(template_path: Union[str, Path], context: Optional[Dict] = None) -> str:
    template = read_template(template_path)
    context = context or {}
    document = template.format(**context)
    return document


def read_template(template_path: Union[str, Path]) -> str:
    template = DIR_TEMPLATES / template_path

    assert template.is_file(), f"template {template_path!r} is not a file"

    with template.open("r") as fd:
        content = fd.read()

    return content


def build_request(environ: Dict) -> RequestT:
    qs = environ["QUERY_STRING"]
    query = parse_qs(qs)

    headers = {
        "-".join(w.capitalize() for w in h[5:].split("_")): v
        for h, v in environ.items()
        if h.startswith("HTTP_")
    }

    request = RequestT(
        method=environ["REQUEST_METHOD"],
        path=environ["PATH_INFO"],
        query=query,
        headers=headers
    )

    return request

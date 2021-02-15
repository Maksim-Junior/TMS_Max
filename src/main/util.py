from pathlib import Path
from string import Template
from typing import Union, Optional, Dict

from framework.dirs import DIR_TEMPLATES


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


def render_template(
    template_path: Union[str, Path],
    context: Optional[Dict] = None,
    *,
    engine: str = "{",
) -> str:
    template = read_template(template_path)
    context = context or {}

    engines = {
        "{": lambda _ctx: template.format(**_ctx),
        "$": Template(template).safe_substitute,
    }

    renderer = engines[engine]
    document = renderer(context)

    return document


def read_template(template_path: Union[str, Path]) -> str:
    template = DIR_TEMPLATES / template_path

    assert template.is_file(), f"template {template_path!r} is not a file"

    with template.open("r") as fd:
        content = fd.read()

    return content

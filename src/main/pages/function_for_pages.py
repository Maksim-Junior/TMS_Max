from framework.dirs import DIR_TASKS, DIR_SRC


def wrong_words(n: str):
    if n.lower() != "nan" and n.lower() != "inf" and n.lower() != "-inf":
        answer = True
    else:
        answer = False
    return answer


def is_number(s):
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
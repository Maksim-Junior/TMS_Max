from urllib.parse import parse_qs

from main.custom_types import ResponseT, RequestT
from main.pages.function_for_pages import wrong_words, is_number, read_tasks, read_template
from tasks.lesson3 import task306, task307, task308, task310, task311
from tasks.lesson4 import task404, task406, task407
from tasks.lesson5 import task501, task502, task503, task504


def index_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_template("index.html")
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def environ_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_template("environ.html")
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def tasks_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("tasks.html")
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def lesson3_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("lesson3/lesson3.html")
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_306_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson3/task_306.html")
    age = qsi.get("age")

    if not age:
        age_control = "Input your age!"
    else:
        age_control = task306.solution(age[0])

    payload = task.format(show_text=age_control)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_307_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson3/task_307.html")
    string = qsi.get("string")

    if not string:
        text = "Input string..."
    else:
        text = task307.solution(string[0])

    payload = task.format(show_text=text)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_308_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson3/task_308.html")
    digit = qsi.get("digit")

    if not digit:
        text = "Input digit..."
    else:
        cube_digit = task308.solution(digit[0])
        text = f"--> {cube_digit}"

    payload = task.format(show_text=text)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_310_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson3/task_310.html")
    money = qsi.get("money")

    show_rubles = ""
    show_penny = ""
    show_text = ""

    if not money:
        show_rubles = ""
        show_penny = ""
        show_text = "Input count of money!"
    elif wrong_words(money[0]) and is_number(money[0]) or money[0].isdigit():
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

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_311_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

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

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def lesson4_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("lesson4/lesson4.html")
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_404_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson4/task_404.html")
    integer = qsi.get("integer")

    if not integer:
        text = "Input integer..."
    else:
        text = task404.solution(integer[0])

    payload = task.format(show_text=text)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_406_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

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

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_407_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson4/task_407.html")
    integer1 = qsi.get("integer1")
    integer2 = qsi.get("integer2")

    if not integer1 and not integer2:
        text = "Input integers..."
        show_count = ""
    elif integer1 and not integer2:
        text = "Input second integer..."
        show_count = ""
    elif not integer1 and integer2:
        text = "Input first integer..."
        show_count = ""
    else:
        numbers, count = task407.solution(integer1[0], integer2[0])
        if type(numbers) is list:
            text = ""
            for i in numbers:
                text += f"{i} "
            show_count = f"Count of numbers --> {count}"
        else:
            text = numbers
            show_count = count

    payload = task.format(show_text=text, show_count=show_count)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def lesson5_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_tasks("lesson5/lesson5.html")
    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_501_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

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
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i}</h2>"
        else:
            text = my_matrix
            matrix = ""
    payload = task.format(show_text=text, show_matrix=matrix)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_502_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson5/task_502.html")
    dimension = qsi.get("dimension")

    if not dimension:
        text = "Input matrix dimension..."
        matrix = ""
        sum_text = ""
    else:
        my_matrix, sum_elem = task502.solution(dimension[0])
        if type(my_matrix) is list:
            matrix = ""
            text = "matrix:"
            sum_text = f"Sum elements --> {sum_elem}"
            for i in my_matrix:
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i}</h2>"
        else:
            text = my_matrix
            matrix = ""
            sum_text = sum_elem
    payload = task.format(show_text=text, show_matrix=matrix, show_sum=sum_text)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_503_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson5/task_503.html")

    mass_n = qsi.get("lines_n")
    mass_m = qsi.get("columns_m")

    if not mass_n and not mass_m:
        text = "Input dimension(n x m)..."
        matrix = ""
        sum_seven = ""
    elif mass_n and not mass_m:
        text = "Input number of columns(m)..."
        matrix = ""
        sum_seven = ""
    elif not mass_n and mass_m:
        text = "Input number of lines(n)..."
        matrix = ""
        sum_seven = ""
    else:
        my_matrix, count_seven = task503.solution(mass_n[0], mass_m[0])
        if type(my_matrix) is list:
            matrix = ""
            text = "matrix:"
            sum_seven = f"Count of seven --> {count_seven}"
            for i in my_matrix:
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i}</h2>"
        else:
            text = my_matrix
            sum_seven = count_seven
            matrix = ""
    payload = task.format(show_text=text, show_matrix=matrix, show_seven=sum_seven)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response


def task_504_page(request: RequestT) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(request.query_string)

    task = read_tasks("lesson5/task_504.html")

    matrix_n = qsi.get("lines_n")
    matrix_m = qsi.get("columns_m")

    if not matrix_n and not matrix_m:
        text = "Input dimension(n x m)..."
        matrix = ""
        count_digits = ""
    elif matrix_n and not matrix_m:
        text = "Input number of columns(m)..."
        matrix = ""
        count_digits = ""
    elif not matrix_n and matrix_m:
        text = "Input number of lines(n)..."
        matrix = ""
        count_digits = ""
    else:
        my_matrix, count = task504.solution(matrix_n[0], matrix_m[0])
        if type(my_matrix) is list:
            matrix = ""
            count_digits = f"Count of digits --> {count}"
            text = "matrix:"
            for i in my_matrix:
                matrix += f"<h2 style = 'color:#FFA07A;font-family: courier, monospace;'>{i}</h2>"
        else:
            text = my_matrix
            count_digits = count
            matrix = ""
    payload = task.format(show_text=text, show_matrix=matrix, show_count=count_digits)

    response = ResponseT(status=status, content_type=content_type, payload=payload)

    return response

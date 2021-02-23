from django.http import HttpRequest, HttpResponse

from main.custom_types import RequestT, ResponseT
from main.util import wrong_words, is_number, render_template

TEMPLATE = "tasks/lesson3/task_310.html"


def handler(request: RequestT) -> ResponseT:

    money = request.query.get("money")

    if not money:
        show_rubles = ""
        show_penny = ""
        show_text = "Input count of money!"
    elif wrong_words(money[0]) and is_number(money[0]) or money[0].isdigit():
        text, rubles, penny = solution(money[0])
        show_rubles = ""
        show_penny = ""
        for i in rubles:
            show_rubles += f"<h2><p style = 'color:#E6E6FA'>{i}</p></h2>"

        for j in penny:
            show_penny += f"<h2><p style = 'color:#E6E6FA'>{j}</p></h2>"

        show_text = text
    else:
        show_rubles = ""
        show_penny = ""
        show_text = "Wrong data!"

    context = {
        "show_rubles": show_rubles,
        "show_penny": show_penny,
        "show_text": show_text
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def handler_django(request: HttpRequest) -> HttpResponse:

    money = request.GET.get("money")

    if not money:
        show_rubles = ""
        show_penny = ""
        show_text = "Input count of money!"
    elif wrong_words(money) and is_number(money) or money.isdigit():
        text, rubles, penny = solution(money)
        show_rubles = ""
        show_penny = ""
        for i in rubles:
            show_rubles += f"<h2><p style = 'color:#E6E6FA'>{i}</p></h2>"

        for j in penny:
            show_penny += f"<h2><p style = 'color:#E6E6FA'>{j}</p></h2>"

        show_text = text
    else:
        show_rubles = ""
        show_penny = ""
        show_text = "Wrong data!"

    context = {
        "show_rubles": show_rubles,
        "show_penny": show_penny,
        "show_text": show_text
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response


def divide_into_rubles_and_penny(count_of_money):
    count_of_rubles = []
    count_of_penny = []
    rubles = {
        500: "💸 500 rubles --> ",
        200: "💸 200 rubles --> ",
        100: "💸 100 rubles --> ",
        50: "💸 50 rubles --> ",
        20: "💸 20 rubles --> ",
        10: "💸 10 rubles --> ",
        5: "💸 5 rubles --> ",
        2: "💰 2 rubles --> ",
        1: "💰 1 ruble --> ",
    }
    penny = {
        50: "💰 50 penny --> ",
        20: "💰 20 penny --> ",
        10: "💰 10 penny --> ",
        5: "💰 5 penny --> ",
        2: "💰 2 penny --> ",
        1: "💰 1 penny --> ",
    }
    if "." not in count_of_money:
        count_of_money += ".0"
    result_count_of_many = ""
    for i in count_of_money:
        if i == ",":
            i = "."
        result_count_of_many += i
    count_of_money = result_count_of_many

    rubles_and_penny = count_of_money.split(".")

    if rubles_and_penny[0][0] == "0":
        while rubles_and_penny[0][0] != "0":
            rubles_and_penny[0] = rubles_and_penny[0][1:]

    if len(rubles_and_penny[1]) == 1:
        rubles_and_penny[1] += "0"
    elif len(rubles_and_penny[1]) == 2 and rubles_and_penny[1][0] == "0" and rubles_and_penny[1][1] != 0:
        rubles_and_penny[1] = rubles_and_penny[1][1]

    rub = int(rubles_and_penny[0])
    pen = rubles_and_penny[1]

    if len(pen) > 2:
        rub += int(pen[:-2])
        pen = pen[-2:]

    pen = int(pen)
    your_money = f"{rub} rubles and {pen} penny!"

    for key in rubles:
        if rub // key > 0:
            count_of_rubles.append(rubles[key] + str(rub // key))
            rub -= key * (rub // key)

    for key in penny:
        if pen // key > 0:
            count_of_penny.append(penny[key] + str(pen // key))
            pen -= key * (pen // key)

    return your_money, count_of_rubles, count_of_penny


def solution(count_of_money: str):
    text, rubles, penny = divide_into_rubles_and_penny(count_of_money)

    return text, rubles, penny


def main():
    count_of_money = (input("Enter count of many --> "))
    done, b, f = divide_into_rubles_and_penny(count_of_money)

    for i in done[1]:
        print(i)

    for j in done[2]:
        print(j)

    return done, b, f


if __name__ == "__main__":
    print(main())

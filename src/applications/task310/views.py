from django.views.generic import TemplateView


class Task310View(TemplateView):
    template_name = "task310/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.GET.get("money")
        text, rubles, penny = solution(data) if data else "Input count of money!", "", ""

        show_rubles = ""
        for i in rubles:
            show_rubles += f" {i} "

        show_penny = ""
        for i in penny:
            show_penny += f" {i} "

        context["show_rubles"] = show_rubles
        context["show_penny"] = show_penny
        context["show_text"] = text

        return context


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
    if wrong_words(count_of_money) and is_number(count_of_money) or count_of_money.isdigit():
        text, rubles, penny = divide_into_rubles_and_penny(count_of_money)
    else:
        text = "Wrong data!"
        rubles = ""
        penny = ""

    return text, rubles, penny


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

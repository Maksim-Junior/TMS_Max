def divide_into_rubles_and_penny(count_of_many):
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
    if "." not in count_of_many:
        count_of_many += ".0"

    rubles_and_penny = count_of_many.split(".")

    if len(rubles_and_penny[1]) == 1:
        rubles_and_penny[1] += "0"
    elif rubles_and_penny[1][0] == "0" and rubles_and_penny[1][1] != 0:
        rubles_and_penny[1] = rubles_and_penny[1][1]

    rub = int(rubles_and_penny[0])
    pen = int(rubles_and_penny[1])
    your_many = f"{rub} rubles and {pen} penny!"

    for key in rubles:
        if rub // key > 0:
            count_of_rubles.append(rubles[key] + str(rub // key))
            rub -= key * (rub // key)

    for key in penny:
        if pen // key > 0:
            count_of_penny.append(penny[key] + str(pen // key))
            pen -= key * (pen // key)

    return your_many, count_of_rubles, count_of_penny


def main():
    count_of_many = (input("Enter count of many --> "))
    done = divide_into_rubles_and_penny(count_of_many)

    for i in done[1]:
        print(i)

    for j in done[2]:
        print(j)

    return done[0]


if __name__ == "__main__":
    print(main())

# 2 Практическая работа
weather = {
    'Зима':"За окном падал белый снег",
    'Весна':"Птицы пели прекрасные песни",
    "Лето":"Солнце светило ярче чем когда-либо",
    "Осень":"Урожай был невероятным"
}

months_names = {
    "Январь": "Зима",
    "Февраль": "Зима",
    "Март": "Весна",
    "Апрель": "Весна",
    "Май": "Весна",
    "Июнь": "Лето",
    "Июль": "Лето",
    "Август": "Лето",
    "Сентябрь": "Осень",
    "Октябрь": "Осень",
    "Ноябрь": "Осень",
    "Декабрь": "Зима"
}

months_numbers = {
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима"
}

def onlyNumber(text):
    mas = list(text)
    for symbol in text:
        if symbol in "1234567890":
            mas.remove(symbol)
    return len(mas) == 0


while True:
    inputer = "12"
    if not onlyNumber(inputer):
        word = months_names.get(inputer)
        if word is not None:
            print(weather[word])
    else:
        inputer = int(inputer)
        word = months_numbers.get(inputer)
        if word is not None:
            print(weather[word])
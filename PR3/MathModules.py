def discriminant(a, b, c):
    return b**2 - 4*a*c

def probability(m, n):
    return m/n

def calculate_probability(event1, event2, joint=True):
    """
    Рассчитывает вероятность совместных или несовместных событий.

    :param event1: вероятность первого события
    :param event2: вероятность второго события
    :param joint: если True, то рассчитывается вероятность совместных событий,
                  если False, то вероятность несовместных событий
    :return: вероятность совместных или несовместных событий
    """
    if joint:
        return event1 * event2
    else:
        return event1 + event2 - event1 * event2

D = discriminant(1, -5, 6)
print(D)  # Вывод: 1

first_event = calculate_probability(probability(3, 10), probability(5, 10), joint=True)
print(f"Рассчитывает вероятность совместных {first_event}")
second_event = calculate_probability(probability(3, 10), probability(5, 20), joint=False)
print(f"Рассчитывает вероятность несовместных {second_event}")
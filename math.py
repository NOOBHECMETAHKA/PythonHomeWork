# 1 Практическая работа
import math


def calculate_square_area(side_length):
    return side_length ** 2


def calculate_rectangle_area(length, width):
    return length * width


def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_circle_area(radius):
    return math.pi * (radius ** 2)


def calculate_right_triangle_area(base, height):
    return 0.5 * base * height


def calculate_cuboid_area(length, width, height):
    return 2 * (length * width + length * height + width * height)


def calculate_cone_area(radius, height):
    base_area = math.pi * (radius ** 2)
    side_area = math.pi * radius * math.sqrt(radius ** 2 + height ** 2)
    return base_area + side_area


def calculate_cylinder_area(radius, height):
    base_area = math.pi * (radius ** 2)
    side_area = 2 * math.pi * radius * height
    return 2 * base_area + side_area


while True:
    print("Выберите фигуру для расчета площади:")
    print("1. Квадрат")
    print("2. Прямоугольник")
    print("3. Треугольник")
    print("4. Круг")
    print("5. Прямоугольный треугольник")
    print("6. Параллелепипед")
    print("7. Конус")
    print("8. Цилиндр")
    print("9. Выйти")

    choice = input("Введите номер фигуры или 9 для выхода: ")

    if choice == '9':
        break

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
        if choice == '1':
            side_length = float(input("Введите длину стороны квадрата: "))
            result = calculate_square_area(side_length)
        elif choice == '2':
            length = float(input("Введите длину прямоугольника: "))
            width = float(input("Введите ширину прямоугольника: "))
            result = calculate_rectangle_area(length, width)
        elif choice == '3':
            base = float(input("Введите длину основания треугольника: "))
            height = float(input("Введите высоту треугольника: "))
            result = calculate_triangle_area(base, height)
        elif choice == '4':
            radius = float(input("Введите радиус круга: "))
            result = calculate_circle_area(radius)
        elif choice == '5':
            base = float(input("Введите длину основания прямоугольного треугольника: "))
            height = float(input("Введите высоту прямоугольного треугольника: "))
            result = calculate_right_triangle_area(base, height)
        elif choice == '6':
            length = float(input("Введите длину параллелепипеда: "))
            width = float(input("Введите ширину параллелепипеда: "))
            height = float(input("Введите высоту параллелепипеда: "))
            result = calculate_cuboid_area(length, width, height)
        elif choice == '7':
            radius = float(input("Введите радиус конуса: "))
            height = float(input("Введите высоту конуса: "))
            result = calculate_cone_area(radius, height)
        elif choice == '8':
            radius = float(input("Введите радиус цилиндра: "))
            height = float(input("Введите высоту цилиндра: "))
            result = calculate_cylinder_area(radius, height)

        print(f"Площадь выбранной фигуры: {result}")
    else:
        print("Неверный выбор. Пожалуйста, введите номер от 1 до 9.")

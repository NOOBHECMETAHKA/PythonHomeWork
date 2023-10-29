# Мотор
class Engine:
    def __init__(self, weight, max_speed, fuel_consumption):
        self.weight = weight
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption

    def display(self):
        print(f"Мотор: вес:{self.weight};"
              f" максимальная скорость:{self.max_speed};"
              f" потребление топлива:{self.fuel_consumption}")


# Бак
class Tank:
    def __init__(self, weight, volume):
        self.weight = weight
        self.volume = volume

    def display(self):
        print(f"Бак: вес:{self.weight};"
              f"объём:{self.volume};")


# Тормоза
class Brakes:
    def __init__(self, weight, brake_efficiency):
        self.weight = weight
        self.brake_efficiency = brake_efficiency

    def display(self):
        print(f"Тормоза: вес:{self.weight};"
              f"Эффективность тормазов:{self.brake_efficiency};")


# Кузов
class Body:
    def __init__(self, weight):
        self.weight = weight

    def display(self):
        print(f"Кузов: вес:{self.weight}")


# Машина
class Car:
    def __init__(self, name, weight, maximum_full_tank, braking_distance):
        self.name = name
        self.weight = weight
        self.maximum_full_tank = maximum_full_tank
        self.braking_distance = braking_distance

    def display(self):
        print(f"Машина: {self.name}")
        print(f"Общий вес: {self.weight}")
        print(f"Максимальное количество топлива: {self.maximum_full_tank}")
        print(f"Тормозное расстояние: {self.braking_distance}")


class CarBuilder:
    def build_car(self, name, engine_data, tank_data, brakes_data, body_data):
        engine = Engine(**engine_data)
        tank = Tank(**tank_data)
        brakes = Brakes(**brakes_data)
        body = Body(**body_data)

        weight = engine.weight + tank.weight + brakes.weight + body.weight
        max_speed = engine.max_speed
        fuel_consumption = engine.fuel_consumption
        tank_volume = tank.volume
        brake_efficiency = brakes.brake_efficiency

        max_distance = max_speed * tank_volume / fuel_consumption
        braking_distance = (weight / 9.8) * brake_efficiency

        car = Car(name, weight, tank_volume, braking_distance)

        return car


carBuilder = CarBuilder()
car_data = {
    "name": "Красная феррари",
    "engine_data": {"weight": 200, "max_speed": 200, "fuel_consumption": 10},
    "tank_data": {"weight": 100, "volume": 50},
    "brakes_data": {"weight": 50, "brake_efficiency": 0.7},
    "body_data": {"weight": 500}
}
my_car = carBuilder.build_car(**car_data)

print(f"Наименование машины: {my_car.name}")
print(f"Вес машины: {my_car.weight} килограмм")
print(f"Максимальный бак: {my_car.maximum_full_tank} литров")
print(f"Максимальная дистанция: {my_car.braking_distance} метров")
import requests
import json

responseAvailableDocumentation = requests.get("https://catfact.ninja/docs/api-docs.json").content
AvailableDocumentation = json.loads(responseAvailableDocumentation)

print("Доступные маршруты: ")
for route in dict.keys(AvailableDocumentation['paths']):
    print(route.replace('/', ''))

path = str(input("Введите маршруты: "))

response = requests.get(f"https://catfact.ninja/{path}")

if 200 <= response.status_code <= 299:
    AvailableObject = json.loads(response.content)
    print(AvailableObject)
elif 400 <= response.status_code <= 499:
    print("Страница не найдена или у вас нету к ней доступа!")
elif 500 <= response.status_code <= 599:
    print("Сервер не может обработать ваш запрос в текущий момент!")






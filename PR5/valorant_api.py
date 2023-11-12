import requests
import json
from types import SimpleNamespace

themes = {
    1:"weapons",
    2:"maps",
    3:"gear",
    4:"agents"
}

print("По какому объекту хотите получить инфомацию?")
for key, theme in themes.items():
    print(f"{key}. {theme}")

id = int(input("Ваш ответ: "))

responseAvailable = requests.get(f"https://valorant-api.com/v1/{themes.get(id)}/").content
info = json.loads(responseAvailable, object_hook=lambda d: SimpleNamespace(**d))

print("Вся инфа тут: " + str(info))



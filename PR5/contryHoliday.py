import requests
import json
from types import SimpleNamespace


responseAvailableCountries = requests.get("https://date.nager.at/api/v3/AvailableCountries").content
AvailableCountries = json.loads(responseAvailableCountries, object_hook=lambda d: SimpleNamespace(**d))

for idx, country in enumerate(AvailableCountries):
    print(f'{idx + 1}. Название страны: {country.name}. Код страны: {country.countryCode}')

id = int(input("Введите номер пункта страны праздники которой хотите узнать: "))

responseCountry = requests.get(f"https://date.nager.at/api/v3/NextPublicHolidays/{AvailableCountries[id - 1].countryCode}").content
AvailableCountry = json.loads(responseCountry, object_hook=lambda d: SimpleNamespace(**d))

for event in AvailableCountry:
    print(f"Дата: {event.date}")
    print(f"Наименование праздника: {event.localName}")
    print(f"Код страны: {event.countryCode}")
    print(f"Не изменный: {event.fixed}")








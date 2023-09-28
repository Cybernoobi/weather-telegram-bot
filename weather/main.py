import requests
import config
from .utils import convert_seconds_to_date


def get_weather(text):
    city = text

    config.parameters["q"] = city

    resp = requests.get(config.url, params=config.parameters).json()
    tz = resp["timezone"]
    name = resp["name"]
    sunrise = convert_seconds_to_date(seconds=resp["sys"]["sunrise"], timezone=tz)
    sunset = convert_seconds_to_date(seconds=resp["sys"]["sunset"], timezone=tz)
    dt = convert_seconds_to_date(seconds=resp["dt"], timezone=tz)
    description = resp["weather"][0]["description"]
    speed = resp["wind"]["speed"]
    temp = resp["main"]["temp"]

    return f"""
==================================
В городе {name} сейчас {description}
Температура: {temp}
Скорость ветра: {speed}
Восход солнца: {sunrise}
Закат солнца: {sunset}
Время отправки запроса: {dt}
=================================="""

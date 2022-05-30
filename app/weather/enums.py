from enum import Enum

class WeatherForecast:
    bulutlu = 1
    günesli = 2
    yagmurlu = 3
    parcalı_bulutlu = 4
    CHOICES = (
        (bulutlu, 'bulutlu'),
        (günesli, 'günesli'),
        (yagmurlu, 'yagmurlu'),
        (parcalı_bulutlu, 'parcalı_bulutlu'),
    )
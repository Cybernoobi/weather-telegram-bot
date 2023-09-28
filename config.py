from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')
TGAPI = os.getenv('TGAPI')
url = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "appid": API_KEY,
    "units": "metric",
    "lang": "ru"
}

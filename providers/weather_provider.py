import requests
from dotenv import load_dotenv
import os

load_dotenv()


class WeatherProvider:
    API_BASE_URL = "https://api.weatherapi.com/v1/forecast.json"
    API_KEY = os.getenv("WEATHER_API_KEY")
    LOCATION = os.getenv("WEATHER_LOCATION", "South Salem, York")

    def fetch(self):
        try:
            res = requests.get(self.API_BASE_URL, params=self.params())
            res.raise_for_status()
            return res.json()
        except Exception as e:
            print(f"Error fetching weather data:-> {e}")
            return None

    def params(self):
        return {
            "key": self.API_KEY,
            "q": self.LOCATION,
            "days": 5,
            "aqi": "no",
            "alerts": "no",
            "hour": 24,
        }

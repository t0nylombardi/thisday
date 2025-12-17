from datetime import datetime
from dotenv import load_dotenv
import os
import math

load_dotenv()


class Weather:
    def __init__(self, date, temperature, text, icon, location):
        self.date = date
        self.temperature = temperature
        self.text = text
        self.icon = icon
        self.location = location or os.getenv("WEATHER_LOCATION", "South Salem, York")

    def formatted(self):
        return f"{self.location}:  {self.text} {math.floor((self.temperature))}°F\n\n"

    def format_forecast(self):
        date = datetime.strptime(self.date, "%Y-%m-%d").date()
        return (
            f"{date.strftime('%A')}:\t {self.text}\t {math.floor((self.temperature))}°F"
        )

    def __str__(self):
        return self.formatted()

    def __repr__(self):
        return f"Weather(date={self.date}, temperature={self.temperature}, text='{self.text}', icon='{self.icon}', location='{self.location}')"

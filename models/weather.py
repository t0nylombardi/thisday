from dotenv import load_dotenv
import os
import math

load_dotenv()


class Weather:
    def __init__(self, temperature, text, icon, location):
        self.temperature = temperature
        self.text = text
        self.icon = icon
        self.location = location or os.getenv("WEATHER_LOCATION", "South Salem, York")

    def formatted(self):
        return f"{self.location}:  {self.text} {math.floor((self.temperature))}°F\n\n"

from providers.weather_provider import WeatherProvider
from models.weather import Weather
from utils.weather_icons import weather_icon


class WeatherService:
    def __init__(self, provider=None):
        self.provider = provider or WeatherProvider()

    def current_weather(self):
        try:
            data = self.provider.fetch()
            cond = data["current"]["condition"]

            return Weather(
                date=data["location"]["localtime"],
                temperature=data["current"]["temp_f"],
                text=cond["text"].strip(),
                icon=weather_icon(cond["code"]),
                location=data["location"]["name"],
            )
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return None

    def forecast(self):
        try:
            data = self.provider.fetch()
            forecast_days = data["forecast"]["forecastday"]
            forecast_list = []

            for day in forecast_days:
                date = day["date"]
                day_info = day["day"]
                cond = day_info["condition"]

                forecast_list.append(
                    Weather(
                        temperature=day_info["avgtemp_f"],
                        text=cond["text"].strip(),
                        icon=weather_icon(cond["code"]),
                        location=data["location"]["name"],
                        date=date,
                    )
                )

            return forecast_list
        except Exception as e:
            print(f"Error fetching forecast data: {e}")
            return []

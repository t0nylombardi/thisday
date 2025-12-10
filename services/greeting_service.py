from core.time_of_day import get_time_of_day
from services.weather_service import WeatherService
from rich.console import Console

console = Console()


def generate_header_greeting(name: str = "friend") -> str:
    time = get_time_of_day()
    time_cap = time.capitalize()

    return f"\n\nGood {time_cap}\n{name}!\n\n"


def generate_sub_header_greeting() -> str:
    time = get_time_of_day()
    time_cap = time.capitalize()
    title_line = "=" * (len(time_cap) + 19)

    return f"\n\n{title_line}\nYour {time_cap} briefing\n{title_line}\n\n"


def generate_weather_greeting() -> str:
    weather = WeatherService().current_weather()

    console.print(f"🌦️ [bold yellow]WEATHER[/bold yellow]:", highlight=True)
    console.print(f"  {weather.formatted()}")

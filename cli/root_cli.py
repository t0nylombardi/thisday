from rich.console import Console
from cli.layout import build_dashboard
from cli.panels import (
    greeting_panel,
    weather_panel,
    news_panel,
    history_panel,
    calendar_panel,
    log_panel,
    footer_panel,
)

from services.greeting_service import generate_header_greeting
from services.weather_service import WeatherService
from services.news_service import NewsService
from services.history_service import HistoryService
from core.time_of_day import get_time_of_day

console = Console()


def run_cli():
    # Fetch all service data FIRST
    time_of_day = get_time_of_day()
    greeting_text = generate_header_greeting("T0ny")
    weather = WeatherService().current_weather()
    news_items = NewsService().latest_headlines()
    history_items = HistoryService().today()
    calendar_items = ["12pm Lunch", "3pm Guitar", "7pm Relax"]  # placeholder

    # Build panels using MODELS, not raw calls
    greeting_p = greeting_panel(greeting_text, time_of_day)
    weather_p = weather_panel(weather)
    news_p = news_panel(news_items)
    history_p = history_panel(history_items)
    calendar_p = calendar_panel(calendar_items)
    log_p = log_panel()
    footer_p = footer_panel()

    # Build dashboard
    layout = build_dashboard(
        greeting_p,
        weather_p,
        news_p,
        history_p,
        calendar_p,
        log_p,
        footer_p,
    )

    console.print(layout)

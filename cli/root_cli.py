from email.header import Header
import select
import sys
import termios
import tty
from time import sleep
from rich.console import Console
from cli.layout import build_dashboard
from rich.live import Live
from cli.panels import (
    weather_panel,
    news_panel,
    history_panel,
    calendar_panel,
    # log_panel,
    footer_panel,
)

from services.greeting_service import generate_header_greeting
from services.weather_service import WeatherService
from services.news_service import NewsService
from services.history_service import HistoryService
from core.time_of_day import get_time_of_day

console = Console()


def read_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def run_cli():
    # Fetch service data
    time_of_day = get_time_of_day()
    greeting_text = generate_header_greeting("T0ny")
    current = WeatherService().current_weather()
    forecast = WeatherService().forecast()
    news_items = NewsService().latest_headlines()
    history_items = HistoryService().today()
    calendar_items = ["12pm Lunch", "3pm Guitar", "7pm Relax"]

    layout = build_dashboard(
        Header(),
        weather_panel(current, forecast),
        news_panel(news_items),
        history_panel(history_items),
        calendar_panel(calendar_items),
        # log_panel(),
        footer_panel(),
    )

    with Live(layout, refresh_per_second=30, screen=True):
        while True:
            input, _, _ = select.select([sys.stdin], [], [], 0.2)
            if input:
                key = read_key()
                print(f"Key pressed: {key}")
                if key.lower() == "q" or key == "\x03":
                    break
                else:
                    console.log(f"Pressed key: {key}")
            sleep(0.1)

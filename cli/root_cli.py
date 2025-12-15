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
    weather = WeatherService().current_weather()
    news_items = NewsService().latest_headlines()
    history_items = HistoryService().today()
    calendar_items = ["12pm Lunch", "3pm Guitar", "7pm Relax"]

    layout = build_dashboard(
        Header(),
        weather_panel(weather),
        news_panel(news_items),
        history_panel(history_items),
        calendar_panel(calendar_items),
        # log_panel(),
        footer_panel(),
    )

    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            sleep(0.1)
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                key = read_key()
                if key.lower() == "q":
                    break

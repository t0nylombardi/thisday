from datetime import datetime
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.table import Table
from services.news_service import NewsItem


class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Rich[/b] Layout application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")


def weather_panel(weather):
    """WeatherService returns a Weather model."""
    if weather is None:
        return Panel("Weather unavailable", title="Weather", border_style="cyan")

    body = f"{weather.icon}  {weather.text} " f"{weather.temperature}°F"
    return Panel(body, title="Weather", border_style="cyan", padding=(0, 1))


def news_panel(news_items: list[NewsItem]) -> Panel:
    """NewsService returns a list of NewsItem models."""
    if not news_items:
        return Panel("No news", title="News", border_style="magenta", padding=0)

    text = "\n".join(f"• {item.title}" for item in news_items[:5])
    return Panel(text, title="News", border_style="magenta", padding=(0, 1))


def history_panel(events):
    """HistoryService returns a list of HistoryItem models."""
    if not events:
        return Panel("No history available", title="On This Day", border_style="yellow")

    text = "\n".join(f"{event.year}: {event.event}" for event in events[:4])
    return Panel(text, title="On This Day", border_style="yellow", padding=(0, 1))


def calendar_panel(events):
    """CalendarService returns a list of agenda strings."""
    text = "\n".join(events) if events else "No events today"
    return Panel(text, title="Today's Calendar", border_style="blue", padding=(0, 1))


def log_panel(message="Press Q to exit • Press R to refresh"):
    return Panel(
        message,
        title="Command Log",
        border_style="green",
        padding=(0, 1),
    )


def footer_panel(version="0.1.0"):
    msg = f"This.Day v{version}"
    return Panel(
        msg,
        border_style="dim",
        padding=(0, 1),
    )

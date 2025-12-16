from datetime import datetime
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.table import Table


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


def weather_panel(current, forecast) -> Panel:
    """WeatherService returns a Weather model."""
    if current is None:
        return Panel("Weather unavailable", title="Weather", border_style="cyan")

    weather_table = Table.grid(expand=True)
    body = f"{current.icon}  {current.text} " f"{current.temperature}°F\n"

    weather_table.add_row(body)
    weather_table.add_row(Text("Forecast:", style="bold underline"))
    if forecast:
        for day in forecast:
            weather_table.add_row(f"{day.date}: {day.text} {day.temperature}°F")

    return Panel(
        weather_table, title="Weather", border_style="cyan", padding=(0, 1), expand=True
    )


def news_panel(news_items) -> Panel:
    if not news_items:
        return Panel("No news available", title="News", border_style="magenta")

    table = Table.grid(expand=True)
    table.add_column()

    for item in news_items[:5]:
        bullet = "•"
        text = Text.assemble(
            (bullet + " ", "bold magenta"),
            (item.title, f"link {item.url} underline white"),
        )
        table.add_row(text)

    return Panel(
        table, title="News", border_style="magenta", padding=(0, 1), expand=True
    )


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

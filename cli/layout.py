from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console
from rich.text import Text


def make_layout():
    layout = Layout(name="root")

    # Top-level vertical split
    layout.split_column(
        Layout(name="main", ratio=3),
        Layout(name="log", ratio=1),
        Layout(name="footer", size=7),
    )

    # Now split "main" into greeting and body
    layout["main"].split(
        Layout(name="greeting", ratio=1, size=5),
        Layout(name="body", ratio=2),
    )

    # Body splits left and right
    layout["body"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=2),
    )

    # Left column auto-expanding stack
    layout["left"].split(
        Layout(name="weather", ratio=3),
        Layout(name="news", ratio=1),
        Layout(name="history", ratio=2),
    )

    # Right side = calendar
    layout["right"].split(Layout(name="calendar", ratio=1))

    return layout


def build_dashboard(
    greeting_panel,
    weather_panel,
    news_panel,
    history_panel,
    calendar_panel,
    log_panel,
    footer_panel,
):
    layout = make_layout()

    layout["greeting"].update(greeting_panel)
    layout["weather"].update(weather_panel)
    layout["news"].update(news_panel)
    layout["history"].update(history_panel)
    layout["calendar"].update(calendar_panel)
    layout["log"].update(log_panel)
    layout["footer"].update(footer_panel)

    return layout

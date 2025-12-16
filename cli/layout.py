from rich.layout import Layout
from rich.panel import Panel

from cli.panels import Header


def make_layout() -> Layout:
    """Create a layout visually similar to lazydocker/lazygit."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        # Layout(name="log", size=5),
        Layout(name="footer", size=3),
    )

    layout["main"].split_row(
        Layout(name="left"),
        Layout(name="body", ratio=1, minimum_size=20),
    )

    layout["body"].split(Layout(name="calendar", ratio=1))

    layout["left"].split(
        Layout(name="weather", size=8),
        Layout(name="news"),
        Layout(name="history", size=5),
    )

    return layout


def build_dashboard(
    header,
    weather_panel,
    news_panel,
    history_panel,
    calendar_panel,
    # log_panel,
    footer_panel,
):
    """Attach panels to the appropriate layout regions."""
    layout = make_layout()

    layout["header"].update(Header())
    layout["weather"].update(weather_panel)
    layout["news"].update(news_panel)
    layout["history"].update(history_panel)
    layout["calendar"].update(calendar_panel)
    # layout["log"].update(log_panel)
    layout["footer"].update(footer_panel)

    return layout

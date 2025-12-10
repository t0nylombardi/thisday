from rich_pyfiglet import RichFiglet
from utils.themes import CATPPUCCIN


def banner(text: str, time_of_day: str) -> RichFiglet:

    theme = CATPPUCCIN[time_of_day]  # latte, frappe, macchiato, mocha

    return RichFiglet(
        text,
        font="ansi_shadow",
        colors=[value for value in theme.values()],
        horizontal=False,
        remove_blank_lines=True,
    )

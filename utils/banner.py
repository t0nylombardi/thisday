from rich_pyfiglet import RichFiglet
from utils.themes import CATPPUCCIN


def banner(text: str, time_of_day: str) -> RichFiglet:

    theme = CATPPUCCIN[time_of_day]  # latte, frappe, macchiato, mocha
    print(f"\n\nUsing theme for {time_of_day}: {theme}\n\n")

    return RichFiglet(
        text,
        font="ansi_shadow",
        colors=[
            theme["first"],
            theme["second"],
            theme["third"],
        ],
        animation="gradient_down",
        horizontal=True,
        fps=15,
        remove_blank_lines=False,
    )

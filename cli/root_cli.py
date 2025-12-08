from rich.console import Console
from core.time_of_day import get_time_of_day
from services.greeting_service import generate_greeting
from utils.banner import banner

console = Console()


def run_cli():
    time = get_time_of_day()
    greeting = generate_greeting("T0ny")

    console.print(banner(greeting, time))
    console.print("The rest of your Rich script")

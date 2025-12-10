import os
import subprocess
from rich.console import Console
from core.time_of_day import get_time_of_day
from services.greeting_service import generate_greeting
from services.greeting_service import generate_sub_greeting
from utils.banner import banner

console = Console()


def run_cli():
    time = get_time_of_day()
    greeting = generate_greeting("T0ny")

    subprocess.run(["clear"] if os.name != "nt" else ["cls"])
    console.print(banner(greeting, time), new_line_start=True, justify="left")
    print(generate_sub_greeting())

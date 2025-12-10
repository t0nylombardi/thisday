import os
import subprocess
from time import sleep
from rich.console import Console
from core.time_of_day import get_time_of_day
from services.greeting_service import generate_greeting
from utils.banner import banner

console = Console()


def run_cli():
    time = get_time_of_day()
    greeting = generate_greeting("T0ny")
    subprocess.run(["clear"] if os.name != "nt" else ["cls"])

    print("\n\n")
    console.print(banner(greeting, time))
    print("\n\n")

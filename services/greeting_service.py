from core.time_of_day import get_time_of_day


def generate_greeting(name: str = "friend") -> str:
    time = get_time_of_day()
    time_cap = time.capitalize()

    return f"\n\nGood {time_cap}\n{name}!\n\n"


def generate_sub_greeting() -> str:
    time = get_time_of_day()
    time_cap = time.capitalize()
    title_line = "=" * (len(time_cap) + 19)

    return f"\n\n{title_line}\nYour {time_cap} briefing\n{title_line}\n\n"

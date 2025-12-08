from core.clock import get_time_of_day


def generate_greeting(name="friend"):
    mode = get_time_of_day()

    if mode == "morning":
        return f"Good morning, {name}!"
    if mode == "afternoon":
        return f"Good afternoon, {name}."
    if mode == "evening":
        return f"Good evening, {name}."
    return f"{name}… it's late. Maybe log off soon?"

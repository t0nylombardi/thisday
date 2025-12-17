from datetime import datetime


def get_time_of_day() -> str:
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 24:
        return "evening"
    else:
        return "night"

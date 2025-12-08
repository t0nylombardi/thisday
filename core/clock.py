from datetime import datetime
from utils.ascii import BANNER_MORNING, BANNER_AFTERNOON, BANNER_EVENING, BANNER_NIGHT


def get_time_of_day():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return BANNER_MORNING
    elif 12 <= hour < 17:
        return BANNER_AFTERNOON
    elif 17 <= hour < 22:
        return BANNER_EVENING
    else:
        return BANNER_NIGHT

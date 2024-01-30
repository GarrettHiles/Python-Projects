from datetime import datetime
import pytz


def is_open(time_zone):
    current_time = datetime.now(pytz.timezone(time_zone))
    open_hours_start = current_time.replace(hour=9, minute=0, second=0, microsecond=0)
    open_hours_end = current_time.replace(hour=17, minute=0, second=0, microsecond=0)

    return open_hours_start <= current_time <= open_hours_end

time_zones = ['US/Pacific', 'Europe/London', 'US/Eastern']

for zone in time_zones:
    status = "open" if is_open(zone) else "closed"
    print(f"{zone} is currently {status}.")

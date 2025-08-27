import sys
import os
from datetime import datetime, timedelta
from pytz import timezone, utc

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from print_with_color import print_blue

def produce_case_day_strings(case_day: datetime):
    case_day_end_datetime = case_day + timedelta(minutes=30)

    # String on "My Sessions" dashboard
    my_session_string = f"{case_day.strftime('%a, %b %-d @ %-I:%M')}-{case_day_end_datetime.strftime('%-I:%M%p')}"  # Output: Ddd, Mmm d @ h:mm-h:mmAM

    # Formatting the start and end times for "+ Add Session" workflow
    add_session_start_time = case_day.strftime("%I:%M %p")  # Output: hh:mm PM
    add_session_end_time = case_day_end_datetime.strftime("%I:%M %p")  # Output: hh:mm PM

    # Date string for registering in bubble or list mode - e.g. '1:45P'
    hmmAP  = case_day.strftime("%-I:%M%p")[:-1]
    for_registering_bubble_mode = "4.0-5.0 " + hmmAP
    # for_registering_list_mode = hmmAP + " : Bedford - John Glenn Middle School – 4.0-5.0"
    for_registering_list_mode = "6:00P : Bedford - John Glenn Middle School – 4.0-5.0"

    return {
        'case_day': case_day,
        'add_session_start_time': add_session_start_time,
        'add_session_end_time': add_session_end_time,
        'my_session_string': my_session_string,
        'for_registering_bubble_mode': for_registering_bubble_mode,
        'for_registering_list_mode': for_registering_list_mode
    }

def day_next_sign_up_opp_24_hours() -> datetime:
    ny_tz = timezone("America/New_York")
    now = datetime.now(ny_tz)  # Use New York timezone
    tomorrow = now + timedelta(days=1)
    minutes = now.minute
    next_interval = (minutes // 15 + 1) * 15
    if next_interval == 60:
        return tomorrow.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    else:
        return tomorrow.replace(minute=next_interval, second=0, microsecond=0)

def sign_up_today_for_session_in_24_hours() -> datetime:
    return day_next_sign_up_opp_24_hours() - timedelta(days=1)

def get_url_for_session_on(datetime_input: datetime):
    url_base = "https://playtimescheduler.com/index.php?go=next&startDate="
    date_one_week_before_date_input = datetime_input - timedelta(weeks=1)
    date_one_week_before_input_formatted = date_one_week_before_date_input.strftime("%Y-%m-%d")
    full_url = url_base + date_one_week_before_input_formatted
    return full_url

if __name__ == "__main__":
    ny_tz = timezone("America/New_York")

    print_blue("FOR RIGHT NOW")
    case_day = datetime.now(ny_tz)
    case_day_strings = produce_case_day_strings(case_day)
    print(f"case_day_strings['my_session_string']--------------------{case_day_strings['my_session_string']}")
    print(f"case_day_strings['add_session_start_time']---------------{case_day_strings['add_session_start_time']}")
    print(f"case_day_strings['add_session_end_time']-----------------{case_day_strings['add_session_end_time']}")
    print(f"case_day_strings['for_registering_bubble_mode']----------{case_day_strings['for_registering_bubble_mode']}")
    print(f"case_day_strings['for_registering_list_mode']------------{case_day_strings['for_registering_list_mode']}")
    print(f"get_url_for_session_on(case_day)-------------------------{get_url_for_session_on(case_day)}")
    print(f"UTC version of right now---------------------------------{case_day.astimezone(utc)}")
    print("")

    # print_blue("FOR A CASE DAY IN THE PAST:")
    # case_day = datetime(1015, 10, 4, 13, 45)
    # case_day_strings = produce_case_day_strings(case_day)
    # print(f"case_day_strings['my_session_string']--------------------{case_day_strings['my_session_string']}")
    # print(f"case_day_strings['add_session_start_time']---------------{case_day_strings['add_session_start_time']}")
    # print(f"case_day_strings['add_session_end_time']-----------------{case_day_strings['add_session_end_time']}")
    # print(f"case_day_strings['for_registering_bubble_mode']----------{case_day_strings['for_registering_bubble_mode']}")
    # print(f"case_day_strings['for_registering_list_mode']------------{case_day_strings['for_registering_list_mode']}")
    # print(f"get_url_for_session_on(case_day)-------------------------{get_url_for_session_on(case_day)}")
    # print("")

    # print_blue("NEXT 24-HR SIGN UP SESSION:")
    # case_day = day_next_sign_up_opp_24_hours()
    # case_day_strings = produce_case_day_strings(case_day)
    # print(f"case_day_strings['my_session_string']--------------------{case_day_strings['my_session_string']}")
    # print(f"case_day_strings['add_session_start_time']---------------{case_day_strings['add_session_start_time']}")
    # print(f"case_day_strings['add_session_end_time']-----------------{case_day_strings['add_session_end_time']}")
    # print(f"case_day_strings['for_registering_bubble_mode']----------{case_day_strings['for_registering_bubble_mode']}")
    # print(f"case_day_strings['for_registering_list_mode']------------{case_day_strings['for_registering_list_mode']}")
    # print(f"get_url_for_session_on(case_day)-------------------------{get_url_for_session_on(case_day)}")
    # print("")

    # print_blue("MOMENT TO SIGN UP FOR TOMORROW'S 24-HR SIGN UP SESSION:")
    # case_day = sign_up_today_for_session_in_24_hours()
    # case_day_strings = produce_case_day_strings(case_day)
    # print(f"case_day_strings['my_session_string']--------------------{case_day_strings['my_session_string']}")
    # print(f"case_day_strings['add_session_start_time']---------------{case_day_strings['add_session_start_time']}")
    # print(f"case_day_strings['add_session_end_time']-----------------{case_day_strings['add_session_end_time']}")
    # print(f"case_day_strings['for_registering_bubble_mode']----------{case_day_strings['for_registering_bubble_mode']}")
    # print(f"case_day_strings['for_registering_list_mode']------------{case_day_strings['for_registering_list_mode']}")
    # print(f"get_url_for_session_on(case_day)-------------------------{get_url_for_session_on(case_day)}")
    # print("")

    print_blue("UTC TIME FOR NEXT SIGN UP OPPORTUNITY:")
    # case_day = sign_up_today_for_session_in_24_hours() - timedelta(days=1) - timedelta(minutes=5)
    case_day = datetime.now().astimezone(ny_tz)
    print_blue(f"Local time where")
    utc_time = case_day.astimezone(utc)
    my_utc_string_understandable = utc_time.strftime('%a, %b %-d @ %-I:%M')
    my_utc_string_cron = utc_time.strftime('%-M %-H * * *')
    print(f"UTC time for next sign up opp:---------------------------{my_utc_string_understandable}")
    print(f"UTC time in cron format:---------------------------------{my_utc_string_cron}")

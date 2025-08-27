from datetime import datetime, timedelta
from pytz import timezone, utc
from case_register import case_register
from case_deregister import case_deregister
from date_variables import day_next_sign_up_opp_24_hours, sign_up_today_for_session_in_24_hours
from wait_until_sign_up_moment import wait_until_sign_up_moment

if __name__ == "__main__":

    # case_day = datetime(2025, 8, 25, 21, 45)
    # case_day = day_next_sign_up_opp_24_hours()
    # headless = True
    # sign_up_moment = sign_up_today_for_session_in_24_hours()

    # sign_up_moment = datetime(2025, 8, 24, 21, 45)

    # case_day = datetime(2025, 8, 25, 9, 15)
    # headless = True
    # sign_up_moment = datetime.now() + timedelta(seconds=30)
    # ny_tz = timezone(utc)
    # case_day = datetime(2025, 8, 27, 19, 45).astimezone(utc) # WE'RE GOING TO LEAVE THIS AS UTC FOR NOW
    ny_timezone = timezone("America/New_York")
    case_day = ny_timezone.localize(datetime(2025, 8, 27, 19, 45))
    # utc_timezone = timezone("UTC")
    # case_day()
    user_type = "registrant"
    headless = True
    # sign_up_moment = case_day - timedelta(days=1)
    sign_up_moment = ny_timezone.localize(datetime(2025, 8, 27, 0, 5))
    # sign_up_moment = utc_timezone.localize(datetime(2025, 8, 26, 21, 30))
    print("I'm expecting this script to start running immediately and wait until 12:05 AM NY time on 8/27/2025, which is UTC: 4:05 AM on 8/27/2025, to send me a message that it's the sign up moment.")
    print(f"case_day          {case_day}")
    print(f"sign_up_moment:   {sign_up_moment}")
    wait_until_sign_up_moment(sign_up_moment)
    case_register(case_day_input = case_day, user_type = user_type, headless = headless, sign_up_moment = sign_up_moment)
    # case_deregister(case_day, "registrant", headless)

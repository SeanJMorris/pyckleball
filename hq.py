from datetime import datetime, timedelta
from pytz import timezone
from case_register import case_register
from case_deregister import case_deregister
from date_variables import day_next_sign_up_opp_24_hours, sign_up_today_for_session_in_24_hours

if __name__ == "__main__":

    # case_day = datetime(2025, 8, 25, 21, 45)
    # case_day = day_next_sign_up_opp_24_hours()
    # headless = True
    # sign_up_moment = sign_up_today_for_session_in_24_hours()

    # sign_up_moment = datetime(2025, 8, 24, 21, 45)

    # case_day = datetime(2025, 8, 25, 9, 15)
    # headless = True
    # sign_up_moment = datetime.now() + timedelta(seconds=30)
    ny_tz = timezone("America/New_York")
    case_day = datetime(2024, 8, 27, 19, 45).astimezone(ny_tz)
    user_type = "registrant"
    headless = True
    # sign_up_moment = case_day - timedelta(days=1)
    sign_up_moment = datetime(2025, 8, 26, 21, 30).astimezone(ny_tz)

    case_register(case_day, user_type, headless, sign_up_moment)
    # case_deregister(case_day, "registrant", headless)

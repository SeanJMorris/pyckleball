from datetime import datetime, timedelta
from case_register import case_register
from case_deregister import case_deregister
from date_variables import day_next_sign_up_opp_24_hours, sign_up_today_for_session_in_24_hours

if __name__ == "__main__":

    case_day = datetime(2025, 8, 25, 21, 30)
    # case_day = day_next_sign_up_opp_24_hours()
    headless = True
    # sign_up_moment = sign_up_today_for_session_in_24_hours()

    sign_up_moment = datetime(2025, 8, 24, 21, 00)

    # case_day = datetime(2025, 8, 25, 9, 15)
    # headless = True
    # sign_up_moment = datetime.now() + timedelta(seconds=30)

    case_register(case_day, "registrant", headless, sign_up_moment)
    # case_deregister(case_day, "registrant", headless)

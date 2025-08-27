from datetime import datetime, timedelta
from pytz import timezone, utc
from case_register import case_register
from case_deregister import case_deregister
from date_variables import day_next_sign_up_opp_24_hours, sign_up_today_for_session_in_24_hours
from wait_until_sign_up_moment import wait_until_sign_up_moment
from utilities.logger import logger

if __name__ == "__main__":

    ny_timezone = timezone("America/New_York")
    # case_day = ny_timezone.localize(datetime(2025, 8, 27, 19, 45))
    case_day = ny_timezone.localize(datetime(2025, 8, 28, 15, 0))
    user_type = "registrant"
    headless = True
    sign_up_moment = ny_timezone.localize(datetime(2025, 8, 27, 8, 40)) - timedelta(days=1)
    # sign_up_moment = ny_timezone.localize(datetime.now() + timedelta(seconds=10)) # GITHUB ACTIONS DIDN'T LIKE THIS

    # print("I'm expecting this script to start running immediately and wait until 12:05 AM NY time on 8/27/2025, which is UTC: 4:05 AM on 8/27/2025, to send me a message that it's the sign up moment.")
    logger.info(f"case_day          {case_day}")
    logger.info(f"sign_up_moment:   {sign_up_moment}")

    # wait_until_sign_up_moment(sign_up_moment)
    case_register(case_day_input = case_day,
                  user_type = user_type,
                  headless = headless,
                  sign_up_moment = sign_up_moment)

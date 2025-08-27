from datetime import datetime, timedelta
from pytz import timezone, utc
from case_register import case_register
from case_deregister import case_deregister
from date_variables import one_week_from_today_at_6pm
from wait_until_sign_up_moment import wait_until_sign_up_moment
from utilities.logger import logger

if __name__ == "__main__":

    # ny_timezone = timezone("America/New_York")
    # case_day = ny_timezone.localize(datetime(2025, 8, 28, 17, 15))
    # case_day = ny_timezone.localize(datetime(2025, 8, 27, 17, 15))
    case_day = one_week_from_today_at_6pm()
    user_type = "pro"
    headless = True
    sign_up_moment = case_day - timedelta(days=7)

    logger.info(f"case_day          {case_day}")
    logger.info(f"sign_up_moment:   {sign_up_moment}")

    # wait_until_sign_up_moment(sign_up_moment)
    case_register(case_day_input = case_day,
                  user_type = user_type,
                  headless = headless,
                  sign_up_moment = sign_up_moment)

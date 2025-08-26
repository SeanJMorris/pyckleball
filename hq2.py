from datetime import datetime
from case_create import case_create
from date_variables import day_next_sign_up_opp_24_hours

if __name__ == "__main__":

    # case_day = datetime(2025, 8, 25, 21, 45)
    # case_day = day_next_sign_up_opp_24_hours()
    case_day = datetime(2024, 8, 26, 21, 45)
    headless = True
    sign_up_24_hr_advance = True

    case_create(case_day, "pro", headless, sign_up_24_hr_advance)

from datetime import datetime


from initialize_case import initialize_case
from print_with_color import print_success, print_blue
from date_variables import produce_case_day_strings
from timer import Timer
from date_picker_handler import date_picker_handler
from utilities.logger import logger

def case_create(case_day_input: datetime,
                user_type: str,
                headless: bool,
                sign_up_24_hr_advance: bool = False):

    yes_pause = not(headless)
    case_day_strings = produce_case_day_strings(case_day_input)
    notification_input = case_day_strings["my_session_string"]
    logger.debug(f"ATTEMPT: Case_create.py is creating pro session for {notification_input}.")

    with Timer() as timer:
        page = initialize_case("pro", headless)
        page.get_by_role("button", name="+ Add Session").click()

        page.locator("#session_location").select_option("1082") # Woburn Racquet Club
        date_picker_handler(page, page.click("#session_date"), case_day_input)
        page.locator("#session_time").click()
        page.locator("#session_time").select_option(case_day_strings["add_session_start_time"])
        page.locator("#session_time_end").click()
        page.locator("#session_time_end").select_option(case_day_strings["add_session_end_time"])
        page.locator("#session_waitlist").select_option("0")
        page.locator("#session_title").click()
        page.locator("#session_title").fill("SINGLES MATCH")

        if sign_up_24_hr_advance:
            page.locator("#session_release").select_option("1") # option to open the session for sign ups 24 hours in advance
        elif not sign_up_24_hr_advance:
            page.locator("#session_release").select_option("0") # option to open the session for sign ups immediately

        page.get_by_role("radio", name="No").check()
        page.get_by_role("textbox").nth(2).click()
        page.get_by_role("textbox").nth(2).fill("Singles session.")
        page.get_by_role("checkbox", name="I acknowledge that a play").check()
        if yes_pause: page.pause()
        page.get_by_role("button", name="Add Session").click()
    logger.debug(f"SUCCESS: Case_create.py created session for {notification_input}.")

if __name__ == "__main__":
    case_day = datetime(2025, 8, 28, 15, 0)
    user_type = "pro"
    headless = True
    sign_up_24_hr_advance = True
    case_create(case_day, user_type, headless, sign_up_24_hr_advance)

from datetime import datetime
from playwright.sync_api import expect

from initialize_case import initialize_case
from print_with_color import print_success, print_blue, print_yellow, print_red
from date_variables import produce_case_day_strings, get_url_for_session_on
from timer import Timer
from datetime import datetime, timedelta
from pytz import timezone
from wait_until_sign_up_moment import wait_until_sign_up_moment
from screenshots.screenshot_util import take_screenshot

def case_register(case_day_input: datetime,
                  user_type: str,
                  headless: bool,
                  sign_up_moment: datetime = None):

    yes_pause = not(headless)
    case_day_strings = produce_case_day_strings(case_day_input)
    notification_input = case_day_strings["my_session_string"]
    print_blue(f"ATTEMPT: Case_register.py is adding user to session on {notification_input}.")

    with Timer() as timer:
        page = initialize_case(user_type, headless)
        page.goto(get_url_for_session_on(case_day_input))
        # if yes_pause: page.pause()

        if sign_up_moment is not None:
            timer.split()
            wait_until_sign_up_moment(sign_up_moment)

        # page.screenshot(path=f"screenshots/{datetime.now()}.png")
        take_screenshot(page)

        if user_type == "pro":
            page.get_by_role("button", name=case_day_strings["for_registering_list_mode"]).first.click()
        elif user_type == "registrant":
            page.get_by_role("button", name=case_day_strings['for_registering_bubble_mode']).first.click()

        # if yes_pause: page.pause()

        page.get_by_role("button", name="+ Add My Name").click()

        if yes_pause: page.pause()

        if user_type == "pro":
            is_registered = page.locator("text=Sean Morris (4.0)").is_visible()
        elif user_type == "registrant":
            is_registered = page.locator("text=Mobley Hesperweld (4.0)").is_visible()

        if is_registered:
            print_success(f"SUCCESS: User was added to the session on {notification_input}.")
        else:
            raise Exception(f"FAILURE: User was NOT added to the session on {notification_input}.")

        take_screenshot(page)

if __name__ == "__main__":
    ny_tz = timezone("America/New_York")
    case_day = datetime(2025, 9, 2, 18, 25).astimezone(ny_tz)
    user_type = "pro"
    headless = False
    # sign_up_moment = case_day - timedelta(days=7)
    sign_up_moment = datetime(2025, 8, 26, 21, 0).astimezone(ny_tz)
    # case_register(case_day, user_type, headless)
    case_register(case_day, user_type, headless, sign_up_moment)

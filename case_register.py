from datetime import datetime
from playwright.sync_api import expect
import time

from initialize_case import initialize_case
from print_with_color import print_success, print_blue, print_yellow, print_red
from date_variables import produce_case_day_strings, get_url_for_session_on
from timer import Timer
from wait_until_sign_up_moment import wait_until_sign_up_moment


def case_register(case_day_input: datetime,
                  user_type: str,
                  headless: bool,
                  sign_up_moment: datetime = None,
                  record_video: bool = False) -> None:

    yes_pause = not(headless)
    case_day_strings = produce_case_day_strings(case_day_input)
    notification_input = case_day_strings["my_session_string"]
    print_blue(f"ATTEMPT: Case_register.py is adding user to session on {notification_input}.")

    with Timer() as timer:
        page = initialize_case(user_type, headless)
        page.goto(get_url_for_session_on(case_day_input))
        # if yes_pause: page.pause()

        if user_type == "pro":
            page.get_by_role("button", name=case_day_strings["for_registering_list_mode"]).first.click()
        elif user_type == "registrant":
            page.get_by_role("button", name=case_day_strings['for_registering_bubble_mode']).first.click()

        if sign_up_moment is not None:
            timer.split()
            wait_until_sign_up_moment(sign_up_moment)

        if yes_pause: page.pause()

        page.get_by_role("button", name="+ Add My Name").click()
        time.sleep(2)
        is_registered = page.locator("text=Mobley Hesperweld (4.0)").is_visible()

        if is_registered:
            print_success(f"SUCCESS: User was added to the session on {notification_input}.")
        else:
            print_red(f"FAILURE: User was NOT added to the session on {notification_input}.")

if __name__ == "__main__":
    case_day = datetime(2025, 8, 25, 11, 15)
    user_type = "registrant"
    headless_mode = True
    case_register(case_day, user_type, headless_mode)
    # sign_up_moment = datetime(2025, 8, 23, 22, 16)
    # case_register(case_day, yes_pause, user_type, headless_mode, sign_up_moment)

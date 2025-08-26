from datetime import datetime
import time
from playwright.sync_api import expect

from initialize_case import initialize_case
from print_with_color import print_success, print_blue, print_yellow, print_red
from date_variables import produce_case_day_strings, get_url_for_session_on
from timer import Timer



def case_deregister(case_day_input: datetime,
                    user_type: str,
                    headless: bool):

    yes_pause = not(headless)
    case_day_strings = produce_case_day_strings(case_day_input)
    notification_input = case_day_strings["my_session_string"]
    print_blue(f"ATTEMPT: Removing registrant from session on {notification_input}....")

    with Timer() as timer:
        page = initialize_case(user_type, headless)
        page.goto(get_url_for_session_on(case_day_input))
        if yes_pause: page.pause()

        if user_type == "pro":
            page.get_by_role("button", name=case_day_strings["for_registering_list_mode"]).first.click()
        elif user_type == "registrant":
            page.get_by_role("button", name=case_day_strings['for_registering_bubble_mode']).first.click()

        if yes_pause: page.pause()
        time.sleep(1)
        is_registered = page.locator("text=Mobley Hesperweld (4.0)").is_visible()

        if is_registered:
            page.get_by_role("row", name="Mobley Hesperweld (4.0)").get_by_role("img").click()
            page.get_by_role("button", name="Remove").click()
            print_success(f"SUCCESS: Registrant was removed from session on {notification_input}.")
        else:
            print_red(f"Registrant was NOT removed for session on {notification_input}. No action taken.")

if __name__ == "__main__":
    case_day = datetime(2025, 8, 24, 20, 15)
    user_type = "registrant"
    headless_mode = True
    case_deregister(case_day, user_type, headless_mode)

from datetime import datetime
from playwright.sync_api import Page, expect
import time

from utilities.logger import logger
from initialize_case import initialize_case
from print_with_color import print_success, print_blue, print_yellow, print_red
from date_variables import produce_case_day_strings, get_url_for_session_on, today_at_given_time
from timer import Timer
from datetime import datetime, timedelta
from pytz import timezone
from wait_until_sign_up_moment import wait_until_sign_up_moment
from screenshots.screenshot_util import take_screenshot


def access_session_to_sign_up(page: Page, user_type, case_day_strings):
    if user_type == "pro":
        # page.get_by_role("button", name=case_day_strings["for_registering_list_mode"]).first.click()
        page.locator("button", has_text="Bedford - John Glenn Middle School – 4.0-").first.click()
    elif user_type == "registrant":
        # page.pause()
        page.get_by_role("button", name=case_day_strings["for_registering_bubble_mode"]).first.click()
        # target_buttons = page.locator('button:has-text("4.0-5.0")')
        # final_locator = target_buttons.filter(has_text="6:")
        # final_locator.first.click()

def validate_user_added(page: Page, user_type: str) -> bool:
    if user_type == "pro":
        is_registered = "Sean Morris (4.0)" in page.get_by_role("rowgroup").inner_text()
    elif user_type == "registrant":
        is_registered = "Mobley Hesperweld (4.0)" in page.get_by_role("rowgroup").inner_text()
    # return is_registered
    # time.sleep(1)
    if is_registered:
        logger.debug(f"SUCCESS: User was added to the session.")
    else:
        logger.error(f"FAILURE: User was NOT added to the session.")

def case_register(case_day_input: datetime,
                  user_type: str,
                  headless: bool,
                  sign_up_moment: datetime = None):

    yes_pause = not(headless)
    case_day_strings = produce_case_day_strings(case_day_input)
    notification_input = case_day_strings["my_session_string"]
    logger.debug(f"ATTEMPT: Case_register.py is adding user to session on {notification_input}.")

    with Timer() as timer:
        page = initialize_case(user_type, headless)
        page.goto(get_url_for_session_on(case_day_input))
        # if yes_pause: page.pause()

        # Determine the sign-up time

        # Click on the first element containing the desired text
        # page.get_by_role("button", name="\" / \" 6:45P : Bedford - John Glenn Middle School – 4.0-").click()

        if user_type == "pro":
            parent_locator = page.locator("button", has_text="Bedford - John Glenn Middle School – 4.0-").first
            strong_element_locator = parent_locator.locator("strong")
            strong_tag_text = strong_element_locator.inner_text()
            strong_tag_text_clean = strong_tag_text[:-1]
            print(strong_tag_text)
            print(strong_tag_text_clean)
            hour_string = strong_tag_text_clean.split(":")[0]
            minute_string = strong_tag_text_clean.split(":")[1]
            if "P" in strong_tag_text:
                hour_integer_24 = int(hour_string) + 12
            else:
                hour_integer_24 = int(hour_string)

            minute_integer = int(minute_string)
            print(f"Hour (24 hr): {hour_integer_24}, Minute: {minute_integer}")

            sign_up_moment = today_at_given_time(hour_integer_24, minute_integer)
            page.pause()
        elif user_type == "registrant":
            sign_up_moment = today_at_given_time(18, 0)


        if sign_up_moment is not None:
            timer.split()
            wait_until_sign_up_moment(sign_up_moment)

        # page.screenshot(path=f"screenshots/{datetime.now()}.png")
        # take_screenshot(page)

        access_session_to_sign_up(page, user_type, case_day_strings)

        if yes_pause: page.pause()

        page.get_by_role("button", name="+ Add My Name").click()

        # if yes_pause: page.pause()

        # time.sleep(1)
        # page.get_by_role("rowgroup").wait_for(timeout=5000)
        # logger.debug(f"Rowgroup inner text: " + page.get_by_role("rowgroup").inner_text())

        #Verify user has been added by closing the session and opening it again
        page.get_by_role("button", name="Close").click()
        access_session_to_sign_up(page, user_type, case_day_strings)
        validate_user_added(page, user_type)

        # take_screenshot(page)

if __name__ == "__main__":
    ny_timezone = timezone("America/New_York")
    case_day = ny_timezone.localize(datetime(2025, 11, 4, 18, 0))
    user_type = "pro"
    headless = False
    case_register(case_day, user_type, headless)

    # user_type = "registrant"
    # headless = False
    # case_register(case_day, user_type, headless)

from datetime import datetime


from initialize_case import initialize_case
from print_with_color import print_success, print_blue
from date_variables import produce_case_day_strings
from timer import Timer


def case_delete(case_day_input: datetime,
                yes_pause: bool,
                user_type: str,
                headless: bool):

    yes_pause = not(headless)
    case_day_strings = produce_case_day_strings(case_day_input)
    notification_input = case_day_strings["my_session_string"]
    print_blue(f"ATTEMPT: Case_delete.py is deleting pro session for {notification_input}.")

    with Timer() as timer:
        page = initialize_case(user_type, headless)
        page.get_by_role("button", name="My Sessions").click()
        if yes_pause: page.pause()
        page.get_by_role("link", name=case_day_strings['my_session_string']).nth(0).click()
        page.get_by_role("link", name="Edit/Cancel Session...").click()
        page.get_by_role("button", name="CANCEL SESSION").click()
        if yes_pause: page.pause()
        page.get_by_role("button", name="Cancel Session", exact=True).click()

    print_success(f"SUCCESS: Case_delete.py deleted session for {notification_input}.")

if __name__ == "__main__":
    case_day = datetime(2025, 10, 5, 13, 45)
    yes_pause = True
    user_type = "pro"
    headless_mode = False
    case_delete(case_day, yes_pause, user_type, headless_mode)

import sys
import os
from datetime import datetime

from playwright.sync_api import sync_playwright, Page, TimeoutError, expect  # type: ignore

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from date_variables import get_url_for_session_on, produce_case_day_strings

class Dashboard():
    def __init__(self, page: Page):
        self.page = page

    def exit_modal_of_ad_if_applicable(self):

        try:
            close_button1 = self.page.get_by_role("button", name="CLOSE", exact=True)
            close_button1.click()
            # print("Successfully closed the ad modal...")
        except TimeoutError:
            print("The ad modal did not appear or was not interactable - exiting function to address it...")
        except Exception as e:
            print(f"An unexpected error occurred with the ad modal: {e}")

    def deal_with_modal_popups(self):
        self.exit_modal_of_ad_if_applicable()

    def go_to_session_on(self, case_day_input: datetime):
        self.page.goto(get_url_for_session_on(case_day_input))
        case_day_strings = produce_case_day_strings(case_day_input)
        expect(self.page.get_byText(case_day_strings["for_registering_list_mode"])).to_be_visible()

    def select_session(self,
                                   case_day_input: datetime,
                                   user_type: str):
        case_day_strings = produce_case_day_strings(case_day_input)

        if user_type == "pro":
            string_to_find = case_day_strings["for_registering_list_mode"]
        elif user_type == "registrant":
            string_to_find = case_day_strings['for_registering_bubble_mode']

        session_button = self.page.get_by_role("button", name=string_to_find).first
        session_button.click()

    def click_first_shown_session(self):
        page.pause()
        first_button = self.page.locator("button.session-button").first
        first_button.click()

    def session_modal_is_present(self):
        # expect(self.page.get_byRole("button", name="+ Add My Name")).to_be_visible()
        pass

if __name__ == "__main__":
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playtimescheduler.com/index.php")

        # dashboard = Login(page)
        # dashboard.deal_with_modal_popups()
        # dashboard.select_session(datetime(2023, 10, 5, 19, 30), "pro")
        # dashboard.session_modal_is_present()
        # dashboard.click_first_shown_session()
        # Keep the browser open for a while to observe the result
        # page.wait_for_timeout(5000)
        # browser.close()

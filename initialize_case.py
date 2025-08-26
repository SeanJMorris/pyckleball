import os
from typing import Literal
from playwright.sync_api import sync_playwright, Page
from dotenv import load_dotenv, find_dotenv

from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard


def initialize_case(user_type: Literal["pro", "registrant"],
                    headless: bool) -> Page:

    load_dotenv(find_dotenv(), override=True)
    if user_type == "pro":
        username = os.getenv("PRO_USER_NAME")
        password = os.getenv("PRO_USER_PASSWORD")
    elif user_type == "registrant":
        username = os.getenv("REGISTRANT_USER_NAME")
        password = os.getenv("REGISTRANT_USER_PASSWORD")

    if not username or not password:
        raise ValueError(f"Environment variables {username} and/or {password} are not set.")

    playwright = sync_playwright().start()
    if headless:
        browser = playwright.chromium.launch(headless=True)
    else:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)

    page = browser.new_page()

    # Login workflow
    login_page = LoginPage(page)
    login_page.login_workflow(username, password)

    # Initialize the dashboard
    dashboard = Dashboard(page)
    dashboard.deal_with_modal_popups()

    return page


if __name__ == "__main__":
    headless = False
    page = initialize_case("pro", headless)
    page.pause()

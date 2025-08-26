import time
import os
from dotenv import load_dotenv, find_dotenv
from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page) -> None:
        self.page = page
        self.page.goto("https://playtimescheduler.com/login.php")

    def populate_email(self, email: str) -> None:
        # self.page.locator('input[name="email"]').fill(email)
        email_textbox = self.page.locator('input[name="email"]')
        email_textbox.fill(email)
        email_textbox.press("Enter")

    # def click_login_after_entering_email(self) -> None:
    #     self.page.get_by_role("button", name="Login").click()

    def populate_password(self, password: str) -> None:
        self.page.locator("#password").fill(password)

    def click_login_after_entering_password(self):
        self.page.get_by_role("button", name="Login").click()
        # self.page.wait_for_url("https://playtimescheduler.com/index.php?l=1")  # Wait for navigation to complete
        self.page.wait_for_url("https://playtimescheduler.com/index.php")  # Wait for navigation to complete

    def login_workflow(self, username: str, password: str) -> None:
        self.populate_email(username)
        # self.click_login_after_entering_email()
        self.populate_password(password)
        self.click_login_after_entering_password()

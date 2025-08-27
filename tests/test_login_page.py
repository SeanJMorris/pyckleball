import os
import sys

from playwright.sync_api import sync_playwright, expect # type: ignore

# sys.path.append('/home/scjmorris/projects/pickleball/pycleball')
# print(os.environ.get("PYTHONPATH"))

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from page_objects.login_page import LoginPage

# print("login_page loaded successfully")

# sys.path.append('/home/scjmorris/projects/pickleball/pycleball/')

def test_login_page():
    my_page = LoginPage()
    print(type(my_page))

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         login_page = LoginPage(page)
#         # login_page.pause()
#         # page.pause()
#         expect(page.get_by_role("button", name="Login")).to_be_visible()

#         # login_page.populate_email(os.getenv("PRO_USER_NAME"))
#         # login_page.click_login_after_entering_email()
#         # login_page.populate_password(os.getenv("NORMAL_USER_PASSWORD"))
#         # login_page.click_login_after_entering_password()

if __name__ == "__main__":
    # test_login_page()
    print(test_login_page)

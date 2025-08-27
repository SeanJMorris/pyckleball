from datetime import datetime
from playwright.sync_api import Page

def take_screenshot(page: Page):

    path = "screenshots/"
    screenshot_timestamp = datetime.now().strftime("%Y.%m.%d_%H%M%S")
    full_path = f"{path}{screenshot_timestamp}.png"
    full_page = False

    page.screenshot(path=full_path, full_page=full_page)

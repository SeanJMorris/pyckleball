from contextlib import contextmanager
import time
from playwright.sync_api import sync_playwright, Page, Playwright, BrowserContext

class PlaywrightContextManager:
    """
    A context manager to handle the synchronous lifecycle of Playwright, a browser, and a context.

    This ensures that resources are properly opened and closed, even if errors occur.
    """

    def __init__(self,
                 headless: bool = True,
                 with_video: bool = False):
        """
        Initialize the context manager.

        :param headless: Whether to run the browser in headless mode. Defaults to True.
        """
        self.playwright: Playwright | None = None
        self.browser = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None
        self.headless = headless
        self.with_video = with_video
        self.slow_mo = 500 if not headless else None

    def __enter__(self):
        """
        Synchronously enters the context, setting up Playwright and a new page.
        """
        print("Starting Playwright and setting up browser...")
        self.playwright = sync_playwright().start()
        # You can choose 'chromium', 'firefox', or 'webkit'
        self.browser = self.playwright.chromium.launch(headless=self.headless, slow_mo=self.slow_mo)
        if self.with_video:
            self.context = self.browser.new_context(record_video_dir="videos/")
        else:
            self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Synchronously exits the context, cleaning up all resources.
        """
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        print("Playwright browser and context closed.")
        # Propagate any exceptions that occurred within the 'with' block
        return False

# class PlaywrightContextManagerWithVideo(PlaywrightContextManager):
#     """
#     A context manager to handle the synchronous lifecycle of Playwright, a browser, and a context,
#     with video recording enabled.
#     """

#     def __enter__(self):
#         """
#         Synchronously enters the context, setting up Playwright and a new page with video recording.
#         """
#         print("Starting Playwright and setting up browser with video recording...")
#         self.playwright = sync_playwright().start()
#         self.browser = self.playwright.chromium.launch(headless=False)
#         self.context = self.browser.new_context(record_video_dir="videos/")  # Enable video recording
#         self.page = self.context.new_page()
#         return self.page

@contextmanager
def start_playwright(headless: bool = False,
                     with_video: bool = False) -> Page:
    # Create an instance of the context manager.
    # The 'with' statement will handle the setup and teardown automatically.
    # The 'page' variable will be the object returned by __enter__.
    # with PlaywrightContextManager(headless=headless, with_video=with_video) as page:
    with PlaywrightContextManager(headless=headless, with_video=with_video) as page:
        url = "https://playtimescheduler.com/login.php"
        page.goto(url)
        page.wait_for_url(url)
        yield page

if __name__ == "__main__":
    page = start_playwright(headless=False, with_video=False)
    print(f"Navigated to: {page.url}")
    # print("Filler for doing stuff.")
    time.sleep(5)
    # page.pause()

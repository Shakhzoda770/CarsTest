# pages.py
import re
import time

from utils.plywright_utils import PlaywrightUtils
from playwright.sync_api import expect


class LoginPage(PlaywrightUtils):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        hamburger = "//div[@class='navSlideOutTab']//i"

    def navigate_to_login(self):
        self.page.goto("https://example.com/login")

    def login(self, username, password):
        self.take_screenshot("screenshots/screenshot_after_login.png")

    # Add other methods as needed

    def navigate_to_login_cars(self):
        self.page.goto("https://cars3test.awninc.com/accounts/login/")

    def do_login_car(self, credentials):
        self.page.get_by_placeholder("Enter email").click()
        self.page.get_by_placeholder("Enter email").fill(credentials["username"])
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill(credentials["password"])
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_load_state()
        expect(self.page.locator("//div[@class='navSlideOutTab']//i")).to_be_visible()

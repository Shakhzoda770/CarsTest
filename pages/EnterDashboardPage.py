import re

from playwright.sync_api import expect

from utils.plywright_utils import PlaywrightUtils


class EnterDashboardPage(PlaywrightUtils):
    def __init__(self, page):
        self.page = page
        self.hamburger = self.page.locator("//div[@class='navSlideOutTab']//i")

    def navigate_to_dashboard_page(self):
        self.page.wait_for_load_state()
        expect(self.hamburger).to_be_visible()
        self.hamburger.click()
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Enterprise Dashboard").click()
        self.page.get_by_role("button", name="").click()
        self.page.get_by_label("Ro number*").click()
        self.page.get_by_label("Ro number*").fill("1")
        self.page.get_by_label("Line").click()
        self.page.get_by_label("Line").press("CapsLock")
        self.page.get_by_label("Line").fill("A")
        self.page.get_by_label("Status amount*").click()
        self.page.get_by_label("Status amount*").fill("346")
        self.page.locator("#complianceCodeSelect").select_option("1")
        self.page.get_by_label("Service advisor").click()
        self.page.get_by_label("Service advisor").fill("1")
        self.page.get_by_label("Tech number").click()
        self.page.get_by_label("Tech number").fill("1")
        self.page.get_by_label("First Comment*").click()
        self.page.get_by_label("First Comment*").fill("test")
        self.page.get_by_role("button", name="Finish & Close").click()




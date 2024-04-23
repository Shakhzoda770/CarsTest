import re
import time

from utils.plywright_utils import PlaywrightUtils
from playwright.sync_api import expect


class HomePage(PlaywrightUtils):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.hamburger = self.page.locator("//div[@class='navSlideOutTab']//i")
        self.coverageTitle = self.page.locator("//span[contains(text(),'Coverages')]")

    TEXT_INPUT = "//textarea[@name='q']"

    def navigate_to_home(self, test_browser_url):
        self.page.goto(test_browser_url)

    def enter_input(self):
        self.fill_input(self.TEXT_INPUT, "playwright")
        self.press_key("Enter")
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(5000)
        print(self.page.url)
        search_results_title = self.get_page_title()
        return search_results_title

    def perform_search(self, query):
        self.page.fill(self.TEXT_INPUT, query)
        self.page.press(self.TEXT_INPUT, 'Enter')

    def click_search_result(self, result_index):
        selector = f'//h3[{result_index + 1}]'
        self.page.click(selector)

    def check_if_links_are_clickable(self):
        self.page.wait_for_load_state()
        # expect(self.page.locator("//div[@class='navSlideOutTab']//i")).to_be_visible()
        self.hamburger.click()
        self.coverageTitle.click()
        expect(self.page).to_have_url(re.compile(".*/coverages/"))
        expect(self.page.get_by_role("heading", name="Dealer Coverages")).to_be_visible()

        self.page.locator("//div[@class='navSlideOutTab']//i").click()
        self.page.locator("//span[contains(text(),'Users')]").click()
        expect(self.page).to_have_url(re.compile(".*/users/"))
        expect(self.page.get_by_role("heading", name="Users")).to_be_visible()

        self.page.locator("//div[@class='navSlideOutTab']//i").click()
        self.page.locator("//span[contains(text(),'Schedules')]").click()
        expect(self.page).to_have_url(re.compile(".*/schedules/"))
        expect(self.page.get_by_role("heading", name="Schedules")).to_be_visible()

        self.page.locator("//div[@class='navSlideOutTab']//i").click()
        self.page.get_by_role("link", name=" Audits").click()
        self.page.get_by_role("link", name="Dealer Audits").click()
        expect(self.page.get_by_role("heading", name="Audits")).to_be_visible()

        self.page.get_by_role("link", name=" Billings").click()
        self.page.get_by_role("link", name="Hours").click()
        self.page.get_by_role("heading", name="OEM Audits").click()
        expect(self.page).to_have_url(re.compile(".*/billings/hours-view/"))
        expect(self.page.locator("//label[contains(text(),'Hours Period')]")).to_be_visible()

import re

from playwright.sync_api import expect

from utils.plywright_utils import PlaywrightUtils


class AuditPage():
    def __init__(self, page):
        self.page = page
        self.hamburger = self.page.locator("//div[@class='navSlideOutTab']//i")
        self.audit_link = self.page.get_by_role("link", name=" Audits")
        self.dealer_audit_link = self.page.get_by_role("link", name="Dealer Audits")

    def navigate_to_dealer_audit(self):
        self.page.wait_for_load_state()
        expect(self.hamburger).to_be_visible()
        self.hamburger.click()
        self.audit_link.click()
        self.dealer_audit_link.click()

    def create_dealer_audit(self):
        self.page.wait_for_load_state()
        self.page.locator("//button[@data-target='#newAuditModal']").click()
        self.page.get_by_label("Date*").fill("2024-03-17")
        self.page.get_by_label("Claims reviewed*").click()
        self.page.get_by_label("Claims reviewed*").fill("1")
        self.page.get_by_label("Note", exact=True).click()
        self.page.get_by_label("Note", exact=True).fill("test")
        self.page.get_by_role("button", name="Create").click()

    def navigate_to_internal_audit(self):
        self.page.wait_for_load_state()
        expect(self.page.locator(".fas").first).to_be_visible()
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Audits").click()
        self.page.get_by_role("link", name="Internal Audits").click()
        expect(self.page.get_by_role("heading", name="Internal audits")).to_be_visible()

    def search_internal_audit(self):
        self.page.get_by_role("searchbox", name="Search:").click()
        self.page.get_by_role("searchbox", name="Search:").fill("291")
        self.page.get_by_role("gridcell", name="291").click()
        expect(self.page.get_by_role("heading", name="Internal Audits for: Christy Pearson")).to_be_visible()
        self.page.get_by_role("button", name="Close").click()

    def verify_internal_audit_details(self):
        self.page.get_by_role("searchbox", name="Search:").click()
        self.page.get_by_role("searchbox", name="Search:").fill("291")
        self.page.get_by_role("gridcell", name="291").click()
        self.page.get_by_role("gridcell", name="26").click()
        expect(self.page.get_by_role("cell", name="Score: / 53")).to_be_visible()
        self.page.locator("//ul[@id='dealerTabs']//a[contains(text(),'Johnson LLC641')]").click()
        expect(self.page.get_by_role("cell", name="Score: / 53")).to_be_visible()
        self.page.locator("//ul[@id='dealerTabs']//a[contains(text(),'Wilson, Brown and Mitchell2356')]").click()
        expect(self.page.get_by_role("cell", name="Score: / 53")).to_be_visible()
        self.page.get_by_role("button", name="Close").click()

    def navigate_to_oem_audit(self):
        self.page.wait_for_load_state()
        expect(self.page.locator(".fas").first).to_be_visible()
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Audits").click()
        self.page.get_by_role("link", name="OEM Audits").click()
        expect(self.page.get_by_role("heading", name="OEM Audits")).to_be_visible()

    def create_oem_audit(self):
        self.page.wait_for_load_state()
        self.page.locator("// button[ @ title = 'New OEM Audit']").click()
        expect(self.page.get_by_role("heading", name="Create OEM Audit")).to_be_visible()
        self.page.get_by_role("combobox", name="Dealer*").select_option("1487")
        self.page.get_by_label("Audit date*").click()
        self.page.get_by_label("Audit date*").fill("03/17/2024")
        self.page.get_by_label("Chargeback amount*").click()
        self.page.get_by_label("Chargeback amount*").fill("30")
        self.page.get_by_label("Awn responsibility amount*").click()
        self.page.get_by_label("Awn responsibility amount*").fill("10")
        self.page.get_by_role("button", name="Create OEM Audit").click()
        self.page.get_by_role("searchbox", name="Search:").click()
        self.page.get_by_role("searchbox", name="Search:").fill("Abbott-Ray702")
        expect(self.page.get_by_role("gridcell", name="Abbott-Ray702")).to_be_visible()
        self.page.get_by_role("gridcell", name="Abbott-Ray702").click()
        self.page.get_by_role("button", name="Delete OEM Audit").click()
        self.page.get_by_role("button", name="Confirm").click()
import random
import re

from playwright.sync_api import expect

from utils.plywright_utils import PlaywrightUtils


class CompliancePage(PlaywrightUtils):
    random_number = str(random.randint(1, 10000))
    compliance_comment = "test" + random_number

    def create_compliance(self):
        self.page.locator("//button[@id='newComplianceButton']").click()
        self.page.get_by_label("Ro number*").click()
        self.page.get_by_label("Ro number*").fill(self.random_number)
        self.page.get_by_label("Status amount*").click()
        self.page.get_by_label("Status amount*").fill("3")
        self.page.locator("#complianceCodeSelect").select_option("1")
        self.page.locator("//form[@id='manualRoComplianceNewModalForm']//div[@class='richText-editor']").click()
        self.page.locator("//form[@id='manualRoComplianceNewModalForm']//div[@class='richText-editor']").fill(
            self.compliance_comment)
        self.page.get_by_role("button", name="Finish & Close").click()

    def verify_compliance_created(self):
        self.page.get_by_role("searchbox", name="Search:").click()
        self.page.get_by_role("searchbox", name="Search:").fill(self.compliance_comment)
        self.page.get_by_role("searchbox", name="Search:").press("Enter")
        self.page.get_by_role("gridcell", name=self.random_number).click()
        self.page.get_by_text(self.compliance_comment, exact=True).click()
        self.page.get_by_role("button", name="Close Compliance").click()
        self.page.get_by_role("combobox", name="Status:").select_option("4")
        self.page.get_by_role("button", name="Save").click()
        self.page.get_by_text("Status Updated").click()

    def verify_questions(self):
        self.page.get_by_role("link", name="Claim Accountability and").click()
        self.page.get_by_text("Questions (17)").click()
        self.page.get_by_role("gridcell", name="751382").click()
        self.page.get_by_text("Close Sidebar").click()
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Sign Out").click()
        self.page.get_by_role("button", name="Sign Out").click()

    def verify_closed_compliance(self):
        self.page.get_by_text("Closed", exact=True).click()
        self.page.get_by_role("gridcell", name="783116").click()
        self.page.get_by_text("Close Sidebar").click()
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Sign Out").click()
        self.page.get_by_role("button", name="Sign Out").click()

    def verify_enterprise_dashboard_page(self):
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Enterprise Dashboard").click()
        self.page.get_by_role("button", name=" Disable Weekly Report").click()
        self.page.get_by_role("button", name=" Enable Weekly Report").click()

    def verify_dealer_name(self):
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Sign Out").click()

    def verify_search_box(self):
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Enterprise Dashboard").click()
        self.page.get_by_role("searchbox", name="Search:").click()
        self.page.get_by_role("searchbox", name="Search:").fill("harris")
        self.page.get_by_role("gridcell", name="Harris PLC2578").click()
        self.page.get_by_role("row", name="  147 256113 E - - 07/10/23").get_by_role("paragraph").click()
        self.page.get_by_text("Close Sidebar").click()
        self.page.get_by_role("row", name="  142 258774 C - - 07/05/23").get_by_role("paragraph").click()
        self.page.get_by_text("Close Sidebar").click()
        self.page.get_by_role("gridcell", name=" 141").nth(1).click()
        self.page.locator("#slideOut div").filter(has_text="Close Sidebar").first.click()
        self.page.get_by_text("Harris PLC2578 (Lake Danny,HI)").click()
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Sign Out").click()
        self.page.get_by_role("button", name="Sign Out").click()
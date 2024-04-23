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

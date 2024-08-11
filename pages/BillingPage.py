from playwright.sync_api import expect

from utils.plywright_utils import PlaywrightUtils


class BillingPage(PlaywrightUtils):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def navigate_to_dealer_billing_hours(self):
        self.page.wait_for_load_state()
        expect(self.page.locator(".fas").first).to_be_visible()
        self.page.locator(".fas").first.click()
        self.page.get_by_role('link', name=' Billings').click()
        self.page.get_by_role('link', name='Hours').click()

    def create_new_hourly_pay(self):
        self.page.get_by_role('button', name=' New Hourly Pay').click()
        self.page.get_by_role('spinbutton', name='Hours Worked*:').click()
        self.page.get_by_role('spinbutton', name='Hours Worked*:').fill('2')
        self.page.get_by_role('textbox', name='Dealership...').click()
        self.page.get_by_role('textbox', name='Dealership...').fill('Test')
        self.page.locator('#dealershipInputautocomplete-list div').click()
        self.page.get_by_label('Comment:').click()
        self.page.get_by_label('Comment:').fill('test')
        self.page.get_by_role('button', name=' Save & Close').click()

    def verify_new_created_hourly_pay(self):
        expect(self.page.get_by_role("cell", name="Test", exact=True)).to_be_visible()

    def edit_new_hourly_pay(self):
        self.page.get_by_role("cell", name="Test", exact=True).click()
        self.page.get_by_label('Comment (Dealer name, etc.):').click()
        self.page.get_by_label('Comment (Dealer name, etc.):').fill('test123')
        self.page.get_by_role('button', name=' Update').click()

    def delete_new_hourly_pay(self):
        self.page.locator("//button[contains(@onclick,'deleteHourlyPay')]").click()
        expect(self.page.get_by_text('Are you sure you want to'))
        self.page.get_by_role('button', name='Confirm').click()

    def navigate_to_Invoices(self):
        self.page.wait_for_load_state()
        expect(self.page.locator(".fas").first).to_be_visible()
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Billings").click()
        self.page.get_by_role("link", name="Invoices").click()

    def search_invoices(self):
        self.page.wait_for_load_state()
        self.page.locator("//div[@id='inputGroupView']").click()
        self.page.get_by_placeholder("Search...").click()
        self.page.get_by_placeholder("Search...").fill("Allen Ltd780")
        self.page.get_by_role("link", name="Allen Ltd780 ").click()
        expect(self.page.get_by_role("heading", name="Invoices for Allen Ltd780")).to_be_visible()
        self.page.get_by_role("searchbox", name="Search:").click()
        self.page.get_by_role("searchbox", name="Search:").fill("148960")

    def verify_search_invoices(self):
        expect(self.page.get_by_role("gridcell", name="148960")).to_be_visible()

    def navigate_to_payroll(self):
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Billings").click()
        self.page.get_by_role("link", name="Payroll").click()

    def navigate_to_memos(self):
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Billings").click()
        self.page.get_by_role("link", name="Memos").click()

    def search_payroll(self, month, year, search_text):
        self.page.get_by_role("combobox", name="Payroll Period").select_option(month)
        self.page.locator("#year").select_option(year)
        self.page.get_by_role("searchbox", name="Search:").click()
        self.page.get_by_role("searchbox", name="Search:").fill(search_text)
        expect(self.page.get_by_role("gridcell", name=search_text)).to_be_visible()

    def create_memo(self):
        self.page.get_by_role("button", name=" New Memo Note").click()
        self.page.get_by_label("Date*").click()
        self.page.get_by_role("link", name="13").click()
        self.page.get_by_label("Number*", exact=True).click()
        self.page.get_by_label("Number*", exact=True).fill("4")
        self.page.get_by_role("dialog", name="New Memo").get_by_placeholder("Amount*").click()
        self.page.get_by_role("dialog", name="New Memo").get_by_placeholder("Amount*").fill("4")
        self.page.get_by_role("combobox", name="Warranty Administrator*").select_option("9688")
        self.page.get_by_label("Comment*").fill("test")
        self.page.get_by_role("button", name=" Save & Close").click()
        self.page.get_by_role("tab", name="Files").click()
        self.page.get_by_role("textbox", name=" ADD FILES").click()
        self.page.get_by_role("textbox", name=" ADD FILES").set_input_files("data.xlsx")
        self.page.get_by_role("button", name="Upload").click()

    def close_billing(self):
        self.page.get_by_role("button", name="Close Billing").click()
        self.page.get_by_text("Billing closed").click()

    def operations_on_approval_page(self):
        self.page.locator(".fas").first.click()
        self.page.get_by_role("link", name=" Billings").click()
        self.page.get_by_role("link", name="Approval").click()

    def close_to_approve_billing(self):
        expect(self.page.get_by_role("button", name="Closed (1)").get_by_text("Closed")).to_be_visible()
        self.page.get_by_role("button", name="Closed (1)").get_by_text("Closed").click()
        self.page.locator(".odd > .select-checkbox").click()
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Approve Billing", exact=True).click()

    def approve_to_create_selected_invoices(self):
        self.page.get_by_role("button", name="Approved (1)").click()
        self.page.locator(".odd > .select-checkbox").click()
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Create Selected Invoices").click()
        expect(self.page.get_by_role("button", name="Invoices (1)")).to_be_visible()

    def create_invoices_to_send_invoices(self):
        self.page.get_by_role("button", name="Invoices (1)").click()
        self.page.locator(".odd > .select-checkbox").click()
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Send Invoices To Selected Dealers").click()

    def send_invoices_to_download_invoices(self):
        self.page.get_by_role("button", name="Sent (1)").click()
        self.page.locator(".odd > .select-checkbox").click()
        with self.page.expect_download() as download_info:
            self.page.get_by_role("button", name="Download Invoice Sheet(s)").click()
        download = download_info.value

        self.page.get_by_role("gridcell", name="Allen Ltd780").click()
        self.page.get_by_role("button", name="Delete Billing").click()
        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="Ok").click()
        expect(self.page.get_by_role("gridcell", name="No data available in table")).to_be_visible()

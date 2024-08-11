def test_create_dealer_audit(login_page, billing_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    billing_page.navigate_to_dealer_billing_hours()
    billing_page.create_new_hourly_pay()
    billing_page.verify_new_created_hourly_pay()
    billing_page.edit_new_hourly_pay()
    billing_page.delete_new_hourly_pay()


def test_search_invoices(login_page, billing_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    billing_page.navigate_to_Invoices()
    billing_page.search_invoices()
    billing_page.verify_search_invoices()


def test_search_payroll(login_page, billing_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    billing_page.navigate_to_payroll()
    billing_page.search_payroll("3", "2023", "Katie Martinez")


def test_memo(login_page, billing_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    billing_page.navigate_to_memos()
    billing_page.create_memo()
    billing_page.close_billing()


def test_approvalPage_memo(login_page, billing_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    billing_page.operations_on_approval_page()
    billing_page.close_to_approve_billing()
    billing_page.approve_to_create_selected_invoices()
    billing_page.create_invoices_to_send_invoices()
    billing_page.send_invoices_to_download_invoices()

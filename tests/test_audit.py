def test_create_dealer_audit(login_page, audit_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    audit_page.navigate_to_dealer_audit()
    # audit_page.create_dealer_audit()


def test_create_internal_audit(login_page, audit_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    audit_page.navigate_to_internal_audit()
    audit_page.search_internal_audit()
    audit_page.verify_internal_audit_details()


def test_create_oem_audit(login_page, audit_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    audit_page.navigate_to_oem_audit()
    audit_page.create_oem_audit()

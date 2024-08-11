def test_compliance(login_page, compliance_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    compliance_page.create_compliance()


def test_verify_page(login_page, compliance_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    compliance_page.verify_compliance_created()


def test_compliance_questions(login_page, compliance_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    compliance_page.verify_questions()


def test_closed_compliance(login_page, compliance_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    compliance_page.verify_closed_compliance()


def test_enterprise_dashboard(login_page, compliance_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    compliance_page.verify_enterprise_dashboard_page()


def test_verify_search_in_dashboard(login_page, compliance_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    compliance_page.verify_search_box()

def test_compliance(login_page, compliance_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    compliance_page.create_compliance()
    compliance_page.verify_compliance_created()
def enterprise_dashboard(login_page, enterdashboard_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    enterdashboard_page.navigate_to_dashboard_page()

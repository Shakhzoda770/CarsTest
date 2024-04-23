from tests.conftest import login_page, home_page


def test_login_and_navigate_home(login_page, home_page, schedules_page):
    login_page.navigate_to_login_cars()
    login_page.do_login_car("atoshmatova@awninc.com", "test12345")
    home_page.check_if_links_are_clickable()
    schedules_page.name()

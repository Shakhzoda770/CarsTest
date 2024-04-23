# test_navigation.py
import pytest

from config.config import BROWSER_URL
from tests.conftest import login_page, home_page


@pytest.fixture(scope="function")
def test_browser_url():
    return BROWSER_URL


def test_login_and_navigate_home(login_page, home_page):
    login_page.navigate_to_login()
    login_page.login("username", "password")


def test_sample(login_page, home_page, test_browser_url):
    home_page.navigate_to_home(test_browser_url)
    print(home_page.get_page_title())
    expectedTitle = home_page.enter_input()
    print(expectedTitle)
    assert "playwright" in expectedTitle


def test_another_search(common_actions, home_page, test_browser_url):
    # Navigate to Google
    home_page.navigate_to_home(test_browser_url)

    # Perform another search
    home_page.perform_search("Playwright vs Selenium")

    # Take a screenshot of the new search results
    common_actions.take_screenshot("screenshots/screenshot_another_search_results.png")


def test_login_and_navigate_home(login_page):
    login_page.navigate_to_login_cars()
    login_page.do_login("atoshmatova@awninc.com", "test12345")
    login_page.check_if_links_are_clickable()

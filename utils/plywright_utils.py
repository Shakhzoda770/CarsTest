
class PlaywrightUtils:
    def __init__(self, page):
        self.page = page

    def click_element(self, selector):
        self.page.click(selector)

    def get_page_title(self):
        return self.page.title()

    def fill_input(self, selector, text):
        self.page.fill(selector, text)

    def navigate_to(self, url):
        self.page.goto(url)

    def select_dropdown_value(self, selector, value):
        self.page.select_option(selector, value)

    def press_key(self, key):
        self.page.keyboard.press(key)

    def clear_input(self, selector):
        self.page.fill(selector, '')

    def take_screenshot(self, file_path):
        self.page.screenshot(path=file_path)

    # Add more common functions as needed

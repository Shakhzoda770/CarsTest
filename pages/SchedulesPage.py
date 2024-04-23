import re
import time

from utils.plywright_utils import PlaywrightUtils
from playwright.sync_api import expect


class SchedulesPage(PlaywrightUtils):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
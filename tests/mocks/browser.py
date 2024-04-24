from unittest.mock import patch

from selenium.webdriver.remote.webdriver import WebDriver

from speed_sleuth.browser import BrowserInterface


@BrowserInterface.register
class MockBrowser:
    def load_driver(self) -> WebDriver:
        patcher = patch("selenium.webdriver.remote.webdriver.WebDriver")
        return patcher.start()

import unittest
import unittest.mock
from unittest.mock import MagicMock, patch

from speed_sleuth.browser.chromium import ChromiumBrowser


class TestChromiumBrowser(unittest.TestCase):
    @patch("selenium.webdriver.Chrome")
    @patch("selenium.webdriver.chromium.options.ChromiumOptions")
    @patch("selenium.webdriver.chromium.service.ChromiumService")
    def test_load_driver_initialization(
        self, mock_service, mock_options, mock_chrome
    ):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        options_instance = MagicMock()
        mock_options.return_value = options_instance
        service_instance = MagicMock()
        mock_service.return_value = service_instance

        browser = ChromiumBrowser()
        browser.load_driver()

        mock_service.assert_called_once()
        mock_options.assert_called_once()
        options_instance.add_argument.assert_any_call("--window-size=1400x900")
        options_instance.add_argument.assert_any_call("--disable-gpu")
        options_instance.add_argument.assert_any_call("--lang=en_US")

        mock_chrome.assert_called_once_with(
            service=service_instance, options=options_instance
        )

        browser = None

        # Assert that binary path is correct when initializing
        browser = ChromiumBrowser("/mock/browser/binary/path")
        browser.load_driver()

        self.assertEqual("/mock/browser/binary/path", browser.binary_path)

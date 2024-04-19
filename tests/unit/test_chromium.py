import unittest
import unittest.mock
from unittest.mock import MagicMock, PropertyMock, call, patch

from speed_sleuth.browser.chromium import ChromiumBrowser


class TestChromiumBrowser(unittest.TestCase):
    def setUp(self):
        self.chromium_instance = ChromiumBrowser(
            binary_path="/mock/browser/binary/path", headless=True
        )

    @patch("selenium.webdriver.Chrome")
    @patch("selenium.webdriver.chromium.options.ChromiumOptions")
    @patch("selenium.webdriver.chromium.service.ChromiumService")
    def test_load_driver_initialization(
        self, mock_service, mock_options, mock_chrome
    ):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        options_instance = MagicMock()
        binary_location_mock = PropertyMock()
        type(options_instance).binary_location = binary_location_mock
        mock_options.return_value = options_instance
        service_instance = MagicMock()
        mock_service.return_value = service_instance

        self.chromium_instance.load_driver()

        mock_service.assert_called_once()
        mock_options.assert_called_once()
        binary_location_mock.assert_called_once_with(
            "/mock/browser/binary/path"
        )
        options_instance.add_argument.assert_has_calls(
            [
                call("--headless"),
                call("--window-size=1400x900"),
                call("--disable-gpu"),
                call("--lang=en_US"),
            ],
            any_order=True,
        )

        mock_chrome.assert_called_once_with(
            service=service_instance, options=options_instance
        )

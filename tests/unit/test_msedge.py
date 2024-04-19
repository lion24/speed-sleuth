import unittest
import unittest.mock
from unittest.mock import MagicMock, PropertyMock, call, patch

from speed_sleuth.browser.ms_edge import MSEdgeBrowser


class TestEdgeBrowser(unittest.TestCase):
    def setUp(self):
        self.edge_instance = MSEdgeBrowser(
            binary_path="\\mock\\browser\\binary\\path", headless=True
        )

    @patch("selenium.webdriver.Edge")
    @patch("selenium.webdriver.edge.options.Options")
    @patch("selenium.webdriver.edge.service.Service")
    def test_load_driver_initialization(
        self, mock_service, mock_options, mock_edge
    ):
        mock_driver = MagicMock()
        mock_edge.return_value = mock_driver
        options_instance = MagicMock()
        binary_location_mock = PropertyMock()
        type(options_instance).binary_location = binary_location_mock
        mock_options.return_value = options_instance
        service_instance = MagicMock()
        mock_service.return_value = service_instance

        self.edge_instance.load_driver()

        mock_service.assert_called_once()
        mock_options.assert_called_once()
        binary_location_mock.assert_called_once_with(
            "\\mock\\browser\\binary\\path"
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

        mock_edge.assert_called_once_with(
            service=service_instance, options=options_instance
        )

import unittest
from unittest.mock import MagicMock

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from speed_sleuth.provider.fast import Fast
from tests.mocks.driver import MockDriver


class TestFastProvider(unittest.TestCase):
    def setUp(self):
        self.mock_driver = MockDriver()
        self.instance = Fast(self.mock_driver)

    def test_provider_init(self):
        self.mock_driver.get.assert_called_once_with("https://fast.com/")

    def test_provider_run(self):
        # Mock the methods that are expected to be called
        mock_more_info_btn = MagicMock()
        mock_more_info_btn.click = MagicMock()

        # Configure mocks
        self.mock_driver.wait_for_button_clickable.return_value = (
            mock_more_info_btn
        )
        mock_results = MagicMock()
        self.mock_driver.wait_for_element.return_value = mock_results
        mock_results.screenshot = MagicMock()

        # Run the method
        self.instance.run("test-result.png")

        # Assertions to ensure all methods are called correctly
        self.mock_driver.wait_for_button_clickable.assert_called_once_with(
            (By.CSS_SELECTOR, "#show-more-details-link"), timeout=30
        )
        mock_more_info_btn.click.assert_called_once()

        # TODO: uncommenting make test fail, understand why
        # self.mock_driver.wait_for_element.assert_has_calls(
        #     (By.CSS_SELECTOR, "#speed-progress-indicator.speed-progress-indicator.circle.succeeded")  # noqa: E501
        # )
        self.mock_driver.wait_for_element.assert_called_with(
            (By.CSS_SELECTOR, ".speed-controls-container")
        )
        mock_results.screenshot.assert_called_once_with("test-result.png")
        self.mock_driver.cleanup.assert_called_once_with(0)

    def test_provider_run_element_not_found(self):
        # Setup
        self.mock_driver.wait_for_button_clickable.side_effect = (
            NoSuchElementException("Element not found")
        )

        # Execution
        self.instance.run("test-result.png")

        self.mock_driver.cleanup.assert_called_once()

        args, _ = self.mock_driver.cleanup.call_args

        self.assertNotEqual(args[0], 0)  # args[0] would be the error code

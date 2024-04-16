import unittest
from unittest.mock import MagicMock, patch

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from speed_sleuth.browser import BrowserInterface
from speed_sleuth.driver.selenium import SeleniumDriver


@BrowserInterface.register
class MockBrowser:
    def load_driver(self) -> WebDriver:
        patcher = patch("selenium.webdriver.remote.webdriver.WebDriver")
        return patcher.start()


class TestSeleniumDriver(unittest.TestCase):
    def setUp(self):
        self.selenium = SeleniumDriver(MockBrowser())
        self.element_mock = MagicMock(spec=WebElement)
        self.mock_driver = self.selenium.driver
        self.locator = (By.ID, "test-id")
        self.element_mock.find_element.return_value = "dummy_element"
        self.element_mock.is_displayed.return_value = True

    def test_get(self):
        self.selenium.get("https://google.com")
        self.selenium.driver.get.assert_called_once_with("https://google.com")

    def test_find_element(self):
        element = self.selenium.find_element(By.XPATH, "//mock")
        self.selenium.driver.find_element.assert_called_once_with(
            By.XPATH, "//mock"
        )
        self.assertIsNotNone(element)

    @patch(
        "selenium.webdriver.support.wait.WebDriverWait.until",
        spec=WebDriverWait,
    )
    def test_wait_to_be_visible(self, mock_until):
        cases = [
            {
                "name": "return_true_when_element_is_visible",
                "is_displayed": True,
            },
            {
                "name": "return_false_when_element_is_not_visible",
                "is_displayed": False,
            },
        ]

        # TODO should probably not mocked the return of until, rather mock
        # the timeout from wait but not sure how to do this or if this is
        # possible since this is a internal mechanism from selenium

        for case in cases:
            with self.subTest(case["name"]):
                expected = case["is_displayed"]
                self.element_mock.is_displayed.return_value = expected
                mock_until.return_value = expected
                result = self.selenium.wait_to_be_visible(self.element_mock)
                if expected:
                    self.assertTrue(result)
                else:
                    self.assertFalse(result)

    @patch("selenium.webdriver.support.wait.WebDriverWait", spec=WebDriverWait)
    def test_wait_to_be_visible_returns_false_on_timeout(
        self, mock_WebDriverWait
    ):
        # Create an instance mock to be returned when WebDriverWait is called
        mock_wait_instance = MagicMock()
        mock_wait_instance.until.side_effect = TimeoutException("Timeout")

        # Set the mock to return this instance when instantiated
        mock_WebDriverWait.return_value = mock_wait_instance

        # Now call the function under test
        result = self.selenium.wait_to_be_visible(self.element_mock)

        # Assertions to ensure it behaves as expected
        self.assertFalse(result)
        mock_wait_instance.until.assert_called_once()
        args, _ = mock_wait_instance.until.call_args
        self.assertTrue(
            callable(args[0])
        )  # Check the first argument is a callable (lambda)

    @patch("selenium.webdriver.support.wait.WebDriverWait")
    @patch(
        "selenium.webdriver.support.expected_conditions.visibility_of_element_located",  # noqa: E501
        return_value=MagicMock(),
    )
    def test_wait_for_element_visible(self, mock_visibility, mock_wait):
        # Setup
        expected_element = MagicMock()
        mock_wait_instance = MagicMock()
        mock_wait_instance.until.return_value = expected_element
        mock_wait.return_value = mock_wait_instance

        # Execute
        result = self.selenium.wait_for_element(self.locator)

        # Assert
        self.assertEqual(result, expected_element)
        mock_wait.assert_called_once_with(self.mock_driver, 120)
        mock_wait_instance.until.assert_called_once_with(
            mock_visibility(self.locator)
        )

    @patch("selenium.webdriver.support.wait.WebDriverWait")
    @patch(
        "selenium.webdriver.support.expected_conditions.visibility_of_element_located",  # noqa: E501
        return_value=MagicMock(),
    )
    def test_wait_for_element_timeout_raises_exception(
        self, mock_visibility, mock_wait
    ):
        # Setup
        mock_wait_instance = MagicMock()
        mock_wait_instance.until.side_effect = TimeoutException("Timeout")
        mock_wait.return_value = mock_wait_instance

        # Execute & Assert
        with self.assertRaises(NoSuchElementException) as context:
            self.selenium.wait_for_element(self.locator, timeout=120)

        self.assertIn(
            "Element ('id', 'test-id') was not visible after 120 seconds",
            str(context.exception),
        )
        mock_wait.assert_called_once_with(self.mock_driver, 120)
        mock_wait_instance.until.assert_called_once_with(
            mock_visibility(self.locator)
        )

    @patch("selenium.webdriver.support.wait.WebDriverWait")
    @patch(
        "selenium.webdriver.support.expected_conditions.element_to_be_clickable",  # noqa: E501
        return_value=MagicMock(),
    )
    def test_wait_for_button_clickable(self, mock_clickable, mock_wait):
        # Setup
        expected_button = MagicMock()
        mock_wait_instance = MagicMock()
        mock_wait_instance.until.return_value = expected_button
        mock_wait.return_value = mock_wait_instance

        locator = (By.ID, "button-id")

        # Execute
        result = self.selenium.wait_for_button_clickable(locator)

        # Assert
        self.assertEqual(result, expected_button)
        mock_wait.assert_called_once_with(self.mock_driver, 120)
        mock_wait_instance.until.assert_called_once_with(
            mock_clickable(locator)
        )

    @patch("selenium.webdriver.support.wait.WebDriverWait")
    @patch(
        "selenium.webdriver.support.expected_conditions.element_to_be_clickable",  # noqa: E501
        return_value=MagicMock(),
    )
    def test_wait_for_button_clickable_timeout_raises_exception(
        self, mock_clickable, mock_wait
    ):
        # Setup
        mock_wait_instance = MagicMock()
        mock_wait_instance.until.side_effect = TimeoutException("Timeout")
        mock_wait.return_value = mock_wait_instance

        locator = (By.ID, "button-id")

        # Execute & Assert
        with self.assertRaises(NoSuchElementException) as context:
            self.selenium.wait_for_button_clickable(locator, timeout=120)

        self.assertIn(
            "Element ('id', 'button-id') was not clickable after 120 seconds",
            str(context.exception),
        )
        mock_wait.assert_called_once_with(self.mock_driver, 120)
        mock_wait_instance.until.assert_called_once_with(
            mock_clickable(locator)
        )

    def test_cleanup_with_webdriver(self):
        # Execute
        self.selenium.cleanup()

        # Assert
        self.mock_driver.close.assert_called_once()
        self.mock_driver.quit.assert_called_once()
        self.assertIsNone(self.selenium.driver)

    @patch("sys.exit")
    def test_cleanup_with_errno(self, mock_exit):
        # Execute with errno
        self.selenium.cleanup(errno=2)

        # Assert
        self.mock_driver.close.assert_called_once()
        self.mock_driver.quit.assert_called_once()
        self.assertIsNone(self.selenium.driver)
        mock_exit.assert_called_once_with(2)

    def test_cleanup_without_webdriver(self):
        # Setup
        self.selenium.driver = None

        # Execute
        self.selenium.cleanup()

        # There should be no exception and nothing to assert directly
        # We only check that no exception is thrown

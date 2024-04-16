import sys

from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait

from speed_sleuth.browser import BrowserInterface
from speed_sleuth.driver import DriverInterface


@DriverInterface.register
class SeleniumDriver:
    def __init__(self, browser: BrowserInterface):
        self.webdriver = browser.load_driver()

    @property
    def driver(self) -> WebDriver:
        return self.webdriver

    @driver.setter
    def driver(self, driver: WebDriver):
        self.webdriver = driver

    def get(self, url: str):
        self.webdriver.get(url)

    def find_element(self, by="id", value: str | None = None) -> WebElement:
        return self.webdriver.find_element(by, value)

    def wait_to_be_visible(
        self, element: WebElement, timeout: int = 90
    ) -> bool:
        """Waits for the given element to become visible and interactable on
        the page.

        Args:
            element: The WebElement object representing the
                element to wait for.
            timeout: Maximum time to wait for the element to
                become visible, in seconds. Defaults to 90.

        Returns:
            bool: True if the element becomes visible within the specified
                timeout, False otherwise.
        """
        errors = [NoSuchElementException, ElementNotInteractableException]

        try:
            return wait.WebDriverWait(
                self.webdriver,
                timeout=timeout,
                poll_frequency=0.2,
                ignored_exceptions=errors,
            ).until(lambda d: element.is_displayed() or False)
        except TimeoutException as e:
            print("wait_for_clickable timed out waiting: ", e)
            return False

    def wait_for_element(
        self, locator: tuple[str, str], timeout: int = 120
    ) -> WebElement:
        """Wait for an element to be visible and returns it If not found,
        NoSuchElementException is raised.

        Args:
            locator: A tuple of (By, locator) to find the element.
            timeout: The amount for time to wait for the element pointed
                by the locator to be visible. Default to 120.

        Returns:
            WebElement: The element identified by locator

        Raises:
            NoSuchElementException: raised when no element was found under the
                specified locator.

        """
        try:
            element = wait.WebDriverWait(self.webdriver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            raise NoSuchElementException(
                f"Element {locator} was not visible after {timeout} seconds"
            ) from e

    def wait_for_button_clickable(
        self, locator: tuple[str, str], timeout: int = 120
    ) -> WebElement:
        """Wait for a button to be visible and clickable If not found,
        NoSuchElementException is raised.

        Args:
            locator: A tuple of (By, locator) to find the element.
            timeout: The amount for time to wait for the element pointed
                by the locator to be visible. Default to 120.

        Returns:
            WebElement: The button identified by locator

        Raises:
            NoSuchElementException: raised when no element was found under the
                specified locator.

        """
        try:
            element = wait.WebDriverWait(self.webdriver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException as e:
            raise NoSuchElementException(
                f"Element {locator} was not clickable after {timeout} seconds"
            ) from e

    def cleanup(self, errno=0):
        """Cleanup every reserved resources."""
        if self.webdriver:
            self.webdriver.close()
            self.webdriver.quit()
            self.webdriver = None

        if errno:
            sys.exit(errno)

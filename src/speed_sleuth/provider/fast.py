# coding: utf-8
# Disable broad-except for now, will refine later.
# pylint: disable=broad-except
"""Fast.com concrete implementation of the provider class."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from speed_sleuth.driver import DriverInterface
from speed_sleuth.provider import Provider


@Provider.register
class Fast:
    """Represents the Fast.com service for conducting internet speed tests.
    This class provides methods to interact with the Fast.com website using a
    Selenium WebDriver, initiating a speed test, and capturing the results as a
    screenshot.

    The class is designed to work with a browser instance that complies
    with the BrowserInterface, allowing for flexibility in browser
    choice.

    Attributes:
        driver: A driver instance that adheres to the DriverInterface, used
            for web interactions with the browser.

    """

    def __init__(self, driver: DriverInterface):
        """Initializes the Speedofme provider with the specified browser.

        Parameters:
            driver: A driver instance that adheres to the DriverInterface, used
                for web interactions with the browser.

        """
        driver.get("https://fast.com/")
        self.driver = driver

    def run(self, filename: str = "fast-results.png"):
        # The test is started immediately, we don't need to interact
        code = 0
        try:
            # Wait until "more info" button is displayed
            more_info_btn = self.driver.wait_for_button_clickable(
                (By.CSS_SELECTOR, "#show-more-details-link"), timeout=30
            )
            more_info_btn.click()

            # Wait until the snipper stop been animated.
            # Typically, this will be done by adding the "success" class on the
            # spinner wheel, hence we just need to wait for this class to be set  # noqa: E501
            # and we will be done
            self.driver.wait_for_element(
                (
                    By.CSS_SELECTOR,
                    "#speed-progress-indicator.speed-progress-indicator.circle.succeeded",  # noqa: E501
                )
            )

            result_container = self.driver.wait_for_element(
                (By.CSS_SELECTOR, ".speed-controls-container")
            )
            print("[+] done, taking snapshot of the website results")
            if result_container:
                result_container.screenshot(filename)
        except NoSuchElementException as e:
            print(f"element {e} could not be found")
            code = -1
        finally:
            self.driver.cleanup(code)

    def parse_results(self):
        """Parses the captured results of the test.

        This method is intended for future implementation, where results
        obtained from the screenshot or directly from the page will be
        extracted and structured for further processing or analysis.

        Currently, this method does not perform any actions.

        """

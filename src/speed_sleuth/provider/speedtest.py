# coding: utf-8
# Disable broad-except for now, will refine later.
# pylint: disable=broad-except
"""Module for interfacing with speedtest.net for internet speed tests using
Selenium.

This module contains the Speedtest class, which inherits from a generic
Provider class and implements methods to configure, run, and capture
results of internet speed tests from speedtest.net. The class manages
browser interactions, including dismissing notifications and accepting
necessary agreements, to ensure the test runs smoothly.

Dependencies:     - traceback: For error logging and debugging.     -
selenium: For automating web browser interaction.

"""

import traceback

from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By

from speed_sleuth.driver import DriverInterface
from speed_sleuth.provider import Provider


class Speedtest(Provider):
    """A provider class for conducting internet speed tests using the
    speedtest.net website.

    The Speedtest class extends the Provider base class, encapsulating
    methods specific to navigating and interacting with speedtest.net.
    This includes accepting privacy policies, dismissing advertisements
    or notifications, initiating the speed test, and capturing the
    results as screenshots.

    Attributes:
        driver: A driver instance that adheres to the DriverInterface, used
            for web interactions with the browser.

    """

    def __init__(self, driver: DriverInterface):
        """Initializes the Speedtest provider with a browser instance.

        Parameters:
            driver: A driver instance that adheres to the DriverInterface, used
                for web interactions with the browser.

        """
        super().__init__(driver)
        self.driver.get("https://www.speedtest.net/")

    def __str__(self) -> str:
        """Provides a string representation of the Speedtest instance.

        Returns:
            str: A simple string representation for this provider.

        """
        return "speedtest"

    def setup(self):
        """Prepares the speedtest.net environment for testing.

        This method attempts to dismiss the cookie/license agreement
        modal and any other initial pop-ups to ensure the test page is
        ready for interaction.

        """
        try:
            eula_reject_btn = self.driver.wait_for_element(
                (By.CSS_SELECTOR, "button#onetrust-reject-all-handler"),
                timeout=5,
            )

            if eula_reject_btn:
                eula_reject_btn.click()
        except NoSuchElementException:
            # onetrust-accept-btn-handler
            eula_accept_btn = self.driver.wait_for_element(
                (By.CSS_SELECTOR, "button#onetrust-accept-btn-handler"),
                timeout=5,
            )

            if eula_accept_btn:
                eula_accept_btn.click()
        except Exception:
            pass

    def dismiss_notification(self):
        """Dismisses notifications or banners that may interfere with the test.

        This method ensures that no overlay elements prevent interaction
        with the test start button or the results.

        """
        try:
            dismiss_btn = self.driver.wait_for_element(
                (By.CSS_SELECTOR, "a.notification-dismiss")
            )
            if dismiss_btn:
                print("dismissing notification...")
                dismiss_btn.click()
        except NoSuchElementException:
            pass  # Silently ignore this exception which can occur.

    def run(self, filename: str = "speedtest-result.png"):
        """Executes the speed test on speedtest.net and captures a screenshot
        of the results.

        This method orchestrates the test execution, from setup to
        result capture, handling possible UI elements and exceptions
        along the way.

        Parameters:
            filename: The file path where the result screenshot will be saved.
                Defaults to 'speedtest-result.png'.

        """
        code = 0
        try:
            self.setup()
            self.dismiss_notification()
            start_test_btn = self.driver.wait_for_button_clickable(
                (By.CSS_SELECTOR, "#container div.start-button > a"), timeout=5
            )
            start_test_btn.click()
            print("[+] running speedtest.net, please wait")
            # Block until the result is displayed on screen.
            results = self.driver.wait_for_element(
                (
                    By.CSS_SELECTOR,
                    "div.result-container-speed.result-container-speed-active",
                )
            )
            print("[+] done, taking snapshot of the website results")
            # self.dismiss_notification()
            if results:
                results.screenshot(filename)
            # Dismiss speedtest modal.
        except ElementNotInteractableException as e:
            print("Did not find element: ", e)
            code = -1
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            code = -1
        finally:
            self.driver.cleanup(code)

    def parse_results(self):
        """Parses the captured results of the speed test.

        This method is intended for future implementation, where results
        obtained from the screenshot or directly from the page will be
        extracted and structured for further processing or analysis.

        Currently, this method does not perform any actions.

        """

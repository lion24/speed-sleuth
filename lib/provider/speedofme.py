# coding: utf-8
# Disable broad-except for now, will refine later.
# pylint: disable=broad-except
"""speedof.me concrete implementation of the provider class."""

import traceback

from browser import BrowserInterface
from provider import Provider
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Speedofme(Provider):
    """Represents the Speedof.me service for conducting internet speed tests.
    This class provides methods to interact with the Speedof.me website using a
    Selenium WebDriver, including accepting the end-user license agreement
    (EULA), initiating a speed test, and capturing the results as a screenshot.

    The class is designed to work with a browser instance that complies
    with the BrowserInterface, allowing for flexibility in browser
    choice.

    Attributes:     browser (BrowserInterface): An instance of a browser
    that implements the BrowserInterface, used to load pages and
    interact with web elements.

    """

    def __init__(self, browser: BrowserInterface):
        """Initializes the Speedofme provider with the specified browser.

        Parameters:     browser (BrowserInterface): An instance of a
        browser that implements the BrowserInterface. This browser will
        be used to navigate the Speedof.me site and perform tests.

        """
        super().__init__(browser)
        self.driver.get("https://speedof.me/")

    def setup(self):
        """Prepares the testing environment on the Speedof.me website.

        This involves accepting the End User License Agreement (EULA) if
        it is presented. Failure to find the EULA acceptance button is
        handled gracefully and logged.

        """
        try:
            eula_btn = self.driver.find_element(
                By.CSS_SELECTOR, "#cc-accept-btn > a"
            )
            self.wait_to_be_visible(eula_btn)

            print("Found eula accept btn")
            eula_btn.click()
        except NoSuchElementException as e:
            print("element not found: ", e)

    def run(self, filename="speedofme-results.png"):
        """Initiates the speed test on Speedof.me and captures the results. The
        test results are saved as a screenshot in the specified file.

        Parameters:     filename (str): The name of the file to save the
        screenshot of the test results.                     Defaults to
        'speedofme-results.png'.

        This method handles the full lifecycle of the speed test,
        including setup, starting the test, waiting for the test to
        complete, and capturing the results.

        """
        code = 0
        try:
            self.setup()
            self.driver.find_element(
                By.CSS_SELECTOR, "button#start_test_btn"
            ).click()
            print("[+] running speedof.me, please wait")
            retry_btn = self.driver.find_element(
                By.CSS_SELECTOR, "div.result-retry.result-color"
            )
            self.wait_to_be_visible(retry_btn)
            print("[+] done, taking snapshot of the website results")
            results = self.driver.find_element(
                By.CSS_SELECTOR, "#d3_pane > svg.download_svg"
            )
            if results:
                results.screenshot(filename)
        except Exception as exp:
            print(f"An error occured: {exp}")
            traceback.print_exc()
            code = -1
        finally:
            self.cleanup(code)

    def parse_results(self):
        """Parses the results of the speed test. This method is intended to be
        implemented in the future to provide functionality for extracting and
        interpreting the test results from the screenshot or the webpage
        directly.

        Currently, this method is a placeholder and does not perform any
        actions.

        """

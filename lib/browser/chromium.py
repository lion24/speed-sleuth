"""This module defines the ChromiumBrower class, which is an implementation of
the BrowserInterface for creating and configuring a Selenium WebDriver specific
to Chromium- based browsers. Currently, the implementation focuses on Google
Chrome, with the intention to extend support to other Chromium-based browsers
in the future.

Key Components: - BrowserInterface: An abstract base class that defines
a generic interface for browser subclasses. - ChromiumBrower: A concrete
class that implements the BrowserInterface for the Chrome browser,
providing a method to load and configure a Selenium WebDriver with
Chromium-specific options.

"""

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.remote.webdriver import WebDriver

from . import BrowserInterface

BINARY_PATH = "/snap/chromium/2805/usr/lib/chromium-browser/chrome"


@BrowserInterface.register
class ChromiumBrower:
    """ChromiumBrower implements the BrowserInterface to provide a method for
    loading and configuring a WebDriver instance specifically for Chromium
    browsers.

    This class currently supports Chrome browser, with plans to extend
    support to other Chromium-based browsers. It demonstrates how to set
    up a Selenium WebDriver with specific options tailored for a
    Chromium browser instance, including setting the binary location,
    window size, and disabling GPU acceleration.

    Methods:     load_driver(): Creates and returns a configured
    Selenium WebDriver instance                    for the Chromium
    browser.

    """

    def load_driver(self) -> WebDriver:
        """Initializes and returns a Selenium WebDriver instance configured for
        the Chrome browser.

        This method sets up a ChromiumService and configures ChromiumOptions
        to specify the binary location of the Chrome browser, set the window
        size, disable GPU acceleration, and set the browser language. These
        options ensure that the WebDriver instance is ready for web automation
        tasks with Chrome.

        Note: While this implementation currently supports Chromium, there is a
        plan to expand support to other browsers.

        Returns:
            WebDriver: A configured instance of Selenium WebDriver for the
            Chromium browser.

        Example:
            >>> chromium_browser = ChromiumBrower()
            >>> driver = chromium_browser.load_driver()

        """
        service = ChromiumService()
        options = ChromiumOptions()
        options.binary_location = BINARY_PATH
        # options.add_argument('--headless')
        options.add_argument("--window-size=1400x900")
        options.add_argument("--disable-gpu")
        options.add_argument("--lang=en_US")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
        # As using selenium api > 2.x, this call should block until
        # readyState is hit.

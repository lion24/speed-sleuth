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
from selenium.webdriver.chromium import options, service
from selenium.webdriver.remote.webdriver import WebDriver

from speed_sleuth.browser import BrowserInterface


@BrowserInterface.register
class ChromiumBrowser:
    """ChromiumBrower implements the BrowserInterface to provide a method for
    loading and configuring a WebDriver instance specifically for Chromium
    browsers.

    This class currently supports Chrome browser, with plans to extend
    support to other Chromium-based browsers. It demonstrates how to set
    up a Selenium WebDriver with specific options tailored for a
    Chromium browser instance, including setting the binary location,
    window size, and disabling GPU acceleration.

    Attributes:
        binary_path (str, optional): An optional location of the webdriver
            location. Default to None.
        headless (bool, optional): Run in headless mode, i.e., without a UI
                or display server dependencies

    Methods:
        load_driver(): Creates and returns a configured Selenium WebDriver
            instance for the Chromium browser.

    """

    def __init__(self, binary_path=None, headless=False):
        self.binary_path = binary_path
        self.headless = headless

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
            Initiate a chromium browser ready for testing:
            ```pycon
            >>> from speed_sleuth.browser.chromium import ChromiumBrower
            >>> chromium_browser = ChromiumBrower()
            >>> driver = chromium_browser.load_driver()
            >>> driver # doctest: +ELLIPSIS
            <selenium.webdriver.chrome.webdriver.WebDriver (...)>
            >>>
            ```

        """
        chrome_service = service.ChromiumService()
        chrome_options = options.ChromiumOptions()
        if self.binary_path:
            chrome_options.binary_location = self.binary_path
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1400x900")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--lang=en_US")
        return webdriver.Chrome(service=chrome_service, options=chrome_options)
        # As using selenium api > 2.x, this call should block until
        # readyState is hit.

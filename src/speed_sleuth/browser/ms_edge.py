from selenium import webdriver
from selenium.webdriver.edge import options, service
from selenium.webdriver.remote.webdriver import WebDriver

from speed_sleuth.browser import BrowserInterface


@BrowserInterface.register
class MSEdgeBrowser:
    """A class that provides an interface for interacting with the Microsoft
    Edge browser using Selenium WebDriver. It adheres to the BrowserInterface
    to ensure compatibility with the Speed Sleuth's browser handling.

    Attributes:
        binary_path (str): The file path to the Microsoft Edge browser
            executable.
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
        """Initializes and returns a Selenium WebDriver for Microsoft Edge with
        specified options.

        The method sets up the driver with a custom binary location for
        the Edge browser, window size, and language. It disables GPU
        acceleration to ensure compatibility across different systems.
        The driver is configured to wait until the page's readyState is
        'complete' before returning, ensuring that the page is fully
        loaded.

        Returns:
            WebDriver: An instance of Selenium WebDriver configured for
                Microsoft Edge.

        """

        edge_service = service.Service()
        edge_options = options.Options()

        if self.binary_path:
            edge_options.binary_location = self.binary_path
        if self.headless:
            edge_options.add_argument("--headless")
        edge_options.add_argument("--window-size=1400x900")
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--lang=en_US")
        return webdriver.Edge(service=edge_service, options=edge_options)
        # As using selenium api > 2.x, this call should block until
        # readyState is hit.

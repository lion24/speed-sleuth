"""Browser is the module handling the different browser logic and their
implementation in order to be used with selenium."""

import abc

from selenium.webdriver.remote.webdriver import WebDriver


class BrowserInterface(metaclass=abc.ABCMeta):
    """BrowserInterface is a generic interface each browser subclass will need
    to implement in order to correctly configure the selenium webdriver.

    This interface ensures that all subclasses provide a specific method
    to load and configure a Selenium WebDriver instance appropriate for
    the browser they represent.

    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "load_driver")
            and callable(subclass.load_driver)
            or NotImplemented
        )

    @classmethod
    @abc.abstractmethod
    def load_driver(cls) -> WebDriver:
        """Loads and returns a configured instance of Selenium WebDriver
        specific to the browser.

        This method must be implemented by subclasses to provide a
        ready-to-use WebDriver instance that is appropriately configured
        for the browser the subclass represents. The configuration may
        include setting browser options, capabilities, and webdriver
        paths.

        Returns:     WebDriver: An instance of a Selenium WebDriver
        ready for browser automation tasks.

        Raises:     NotImplementedError: If the subclass does not
        implement this method.

        """
        raise NotImplementedError

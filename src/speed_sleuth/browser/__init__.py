"""Browser is the module handling the different browser logic and their
implementation in order to be used with selenium."""

import abc
import platform

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


class OsNotFoundException(Exception):
    """Raised when OS cannot be detected."""


class BrowserFactory:
    """Factory class to create browser instances based on the user's default
    browser.

    This class is designed to abstract the process of detecting the
    default web browser on the user's system and instantiating a
    corresponding browser object that can be used within the
    application.

    """

    @staticmethod
    def get_browser():
        """Retrieves an instance of a browser object based on the user's
        default browser.

        The method first detects the default browser and its executable
        path by calling the `detect_default_browser` static method.
        Depending on the detected browser, it then dynamically imports
        and returns an instance of the corresponding browser class.

        Returns:     An instance of a browser object corresponding to
        the user's default browser.

        Raises:     ValueError: If the detected default browser is not
        supported by the factory.

        """
        default_browser, path = BrowserFactory.detect_default_browser()

        match default_browser:
            case "MSEdgeHTM":
                from speed_sleuth.browser.ms_edge import MSEdgeBrowser

                return MSEdgeBrowser(path)
            case _:
                raise ValueError(
                    f"No supported browser found for {default_browser}"
                )

    @staticmethod
    def detect_default_browser() -> tuple[str, str]:
        """Detects the user's default web browser and its executable path.

        This method attempts to identify the default browser set on the
        user's system. It utilizes the platform module to determine the
        operating system and then uses OS-specific methods to find the
        default browser and its path. For Windows, it accesses the
        system registry.

        Returns:     tuple: A tuple containing the identifier of the
        default browser and its executable path.

        Raises:     OsNotFoundException: If the operating system is not
        recognized or supported by this method.

        """
        browser = "chrome"
        path = "open"  # Fall back to default "open"
        osPlatform = platform.system()

        match osPlatform:
            case "Windows":
                try:
                    from winreg import (
                        HKEY_CLASSES_ROOT,
                        HKEY_CURRENT_USER,
                        OpenKey,
                        QueryValueEx,
                    )

                    with OpenKey(
                        HKEY_CURRENT_USER,
                        r"SOFTWARE\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice",  # noqa: E501
                    ) as reg_key:
                        browser = QueryValueEx(reg_key, "ProgId")[0]

                    with OpenKey(
                        HKEY_CLASSES_ROOT,
                        r"{}\shell\open\command".format(browser),
                    ) as reg_key:
                        browser_path_tuple = QueryValueEx(reg_key, None)
                        path = browser_path_tuple[0].split('"')[1]
                except Exception as e:
                    print(
                        "Failed to look up default browser in system registry: ",  # noqa: E501
                        e,
                    )

            case _:
                raise OsNotFoundException(
                    f"Your OS {osPlatform} is not yet implement."
                )

        return browser, path
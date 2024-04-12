""" TestBrowser: Test the generic methods that applied to all browsers

This also target the helpers defined in browser/__init__.py like the browser
factory for example
"""

from unittest.mock import MagicMock, patch

import pytest

from speed_sleuth.browser import BrowserFactory
from speed_sleuth.browser.chromium import ChromiumBrower
from speed_sleuth.browser.ms_edge import MSEdgeBrowser


class TestBrowser:
    @pytest.mark.parametrize(
        "os_platform, browser_name",
        [("Linux", "google-chrome"), ("Windows", "MSEdgeHTM")],
    )
    def test_detect_default_browser(self, os_platform, browser_name):
        with patch("platform.system") as mock_system:
            mock_system.return_value = os_platform

            if os_platform == "Windows":
                with patch(
                    "speed_sleuth.browser.BrowserFactory.detect_default_browser"  # noqa: E501
                ) as mock_query:
                    mock_query.return_value = (browser_name, None)

                    name, path = BrowserFactory.detect_default_browser()
                    assert name == browser_name
                    assert path is None

            else:
                with patch("webbrowser.get") as mock_get:
                    browser_instance = MagicMock()
                    mock_get.return_value = browser_instance

                    browser_instance.basename = browser_name

                    name, path = BrowserFactory.detect_default_browser()
                    assert name == browser_name
                    assert path is None

    @pytest.mark.parametrize(
        "browser_name, browser_instance, expected_exception",
        [
            ("google-chrome", ChromiumBrower, None),
            ("MSEdgeHTM", MSEdgeBrowser, None),
            (
                "UnexistantBrowser",
                None,
                ValueError("No supported browser found for UnexistantBrowser"),
            ),
        ],
    )
    def test_get_browser(
        self, browser_name, browser_instance, expected_exception
    ):
        with patch(
            "speed_sleuth.browser.BrowserFactory.detect_default_browser"
        ) as default_browser_mock:
            default_browser_mock.return_value = (browser_name, None)

            if expected_exception:
                with pytest.raises(ValueError) as exc_info:
                    instance = BrowserFactory.get_browser()

                assert str(exc_info.value) == str(expected_exception)
            else:
                instance = BrowserFactory.get_browser()
                assert isinstance(instance, browser_instance)

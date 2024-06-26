import os
import tempfile
import unittest

from selenium.webdriver.remote.webdriver import WebDriver

from speed_sleuth.browser import BrowserFactory
from speed_sleuth.provider import Provider
from speed_sleuth.provider.speedtest import Speedtest


class TestSpeedtest(unittest.TestCase):
    def test_speedtest(self):
        speedtest = Speedtest(BrowserFactory.get_browser())
        self.assertIsInstance(speedtest, Provider)
        self.assertIsInstance(speedtest.driver, WebDriver)

    def test_speedtest_run(self):
        speedtest = Speedtest(BrowserFactory.get_browser())
        speedtest.run(filename="test.png")
        self.assertTrue(os.path.exists("test.png"))

    def test_speedtest_run_in_loop(self):
        tmpdir = tempfile.mkdtemp()
        for i in range(3):
            speedtest = Speedtest(BrowserFactory.get_browser())
            speedtest.run("{}/test-{}.png".format(tmpdir, i))
            self.assertTrue(os.path.exists("{}/test-{}.png".format(tmpdir, i)))

    def test_speedtest_cleanup_raise_sysexit(self):
        s2 = Speedtest(BrowserFactory.get_browser())
        with self.assertRaises(SystemExit):
            s2.cleanup(-1)

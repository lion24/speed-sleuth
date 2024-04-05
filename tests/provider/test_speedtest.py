import os
import tempfile
import unittest

from browser.chromium import ChromiumBrower
from provider import Provider
from provider.speedtest import Speedtest
from selenium.webdriver.remote.webdriver import WebDriver


class TestSpeedtest(unittest.TestCase):
    def test_speedtest(self):
        speedtest = Speedtest(ChromiumBrower())
        self.assertIsInstance(speedtest, Provider)
        self.assertIsInstance(speedtest.driver, WebDriver)

    def test_speedtest_run(self):
        speedtest = Speedtest(ChromiumBrower())
        speedtest.run(filename="test.png")
        self.assertTrue(os.path.exists("test.png"))

    def test_speedtest_run_in_loop(self):
        tmpdir = tempfile.mkdtemp()
        for i in range(3):
            speedtest = Speedtest(ChromiumBrower())
            speedtest.run("{}/test-{}.png".format(tmpdir, i))
            self.assertTrue(os.path.exists("{}/test-{}.png".format(tmpdir, i)))

    def test_speedtest_cleanup_raise_sysexit(self):
        s2 = Speedtest(ChromiumBrower())
        with self.assertRaises(SystemExit):
            s2.cleanup(-1)

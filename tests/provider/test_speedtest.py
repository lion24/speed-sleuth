import unittest

from selenium.webdriver.remote.webdriver import WebDriver
from provider import Provider
from provider.speedtest import Speedtest

class TestSpeedtest(unittest.TestCase):
	def setUp(self):
		self.speedtest = Speedtest()

	def test_speedtest(self):
		self.assertIsInstance(self.speedtest, Provider)
		self.assertIsInstance(self.speedtest.driver, WebDriver)

	def test_speedtest_cleanup_raise_sysexit(self):
		self.s2 = Speedtest()
		with self.assertRaises(SystemExit):
			self.s2.cleanup(-1)

	def tearDown(self):
		self.speedtest.cleanup()
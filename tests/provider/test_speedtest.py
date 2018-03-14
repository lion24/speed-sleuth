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

	def tearDown(self):
		self.speedtest.cleanup()
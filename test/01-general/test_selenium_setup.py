import unittest

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class TestSeleniumSetup(unittest.TestCase):
	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		self.driver = webdriver.Chrome(chrome_options=options)
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

	def test_selenium_instance(self):
		self.assertIsInstance(self.driver, WebDriver)

	def tearDown(self):
		self.driver.close()